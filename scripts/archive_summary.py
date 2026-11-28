"""Maintain public discovery metadata without changing article text (stdlib only)."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

FIELDS = ('summary', 'tags', 'role', 'period')


def normalized(text):
    return text.replace('\r\n', '\n').replace('\r', '\n').lstrip('\ufeff')


def content_hash(text):
    return hashlib.sha256(normalized(text).encode('utf-8')).hexdigest()


def word_count(text):
    text = re.sub(r'<!--.*?-->', ' ', text, flags=re.S)
    text = re.sub(r'!?\[([^\]]*)\]\([^\n)]*\)', r'\1', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'https?://\S+', ' ', text)
    return len(re.findall(r"[^\W_]+(?:['’\-][^\W_]+)*", text))


def safe_path(root, relative):
    if not isinstance(relative, str) or not relative or '\\' in relative or ':' in relative:
        raise ValueError('Invalid relative content path')
    path = (Path(root) / relative).resolve()
    if not path.is_relative_to(Path(root).resolve()):
        raise ValueError('Content path escapes archive')
    return path


def metadata_errors(record):
    errors = []
    summary = record.get('summary')
    if not isinstance(summary, str) or not summary.strip() or '\n' in summary:
        errors.append('summary must be a nonempty single paragraph')
    tags = record.get('tags')
    if not isinstance(tags, list) or not 3 <= len(tags) <= 8 or any(
        not isinstance(t, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', t) for t in tags
    ):
        errors.append('tags must contain 3–8 lowercase hyphenated terms')
    elif len(tags) != len(set(tags)):
        errors.append('duplicate tags')
    for key in ('role', 'period'):
        if key in record and (not isinstance(record[key], str) or not record[key].strip()):
            errors.append(f'{key} must be a nonempty string when present')
    prose = ' '.join(str(record.get(k, '')) for k in FIELDS)
    if re.search(r'[A-Za-z]:[\\/]|\[\[|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', prose):
        errors.append('private path, wiki link, or email in discovery metadata')
    return errors


def metadata_fingerprint(record):
    return hashlib.sha256(json.dumps({k: record[k] for k in FIELDS if k in record},
                                    sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()


def stamp(record, text):
    errors = metadata_errors(record)
    if errors:
        raise ValueError('; '.join(errors))
    record['wordCount'] = word_count(text)
    record['contentSha256'] = content_hash(text)


def section_records(catalog, section):
    """Keep curated application priorities independent of publication numbers."""
    records = [r for r in catalog['records'] if r['section'] == section]
    if section != 'applications':
        return records
    return sorted(records, key=lambda r: (r.get('displayOrder', 5),
                  -int(r['id'][4:]) if re.fullmatch(r'PUB-\d+', r['id']) else 0))


def render(catalog):
    lines = ['# Archive Summary', '',
             'A searchable overview of Daniel Powell’s work. Start here to select relevant articles, then read the linked full text for detailed claims.', '',
             '[Complete index](INDEX.md) · [Machine-readable catalog](catalog.json) · [About Daniel Powell](ABOUT.md)', '',
             '<!-- Generated from catalog.json. Edit catalog summaries, then regenerate. -->', '']
    for section in catalog['sections']:
        lines += [f"## {section['title']}", '', section['description'], '']
        for record in section_records(catalog, section['key']):
            lines += [f"### {record['id']} — [{record['title']}]({record['path']})", '', record['summary'], '']
    return '\n'.join(lines)


def validate(root, catalog, check_overview=True, content_overrides=None):
    root = Path(root)
    errors = []
    ids, paths = set(), set()
    sections = {s['key'] for s in catalog['sections']}
    for record in catalog['records']:
        ident = record.get('id', '<missing>')
        if ident in ids or record.get('path') in paths:
            errors.append(f'{ident}: duplicate identity or path')
        ids.add(ident)
        paths.add(record.get('path'))
        if record.get('section') not in sections:
            errors.append(f'{ident}: unknown section')
        if 'displayOrder' in record and (type(record['displayOrder']) is not int or record['displayOrder'] < 0):
            errors.append(f'{ident}: displayOrder must be a nonnegative integer')
        errors += [f'{ident}: {e}' for e in metadata_errors(record)]
        try:
            source = safe_path(root, record['path'])
            text = (content_overrides or {}).get(record['path'])
            if text is None:
                text = source.read_text(encoding='utf-8')
        except (ValueError, OSError, KeyError) as exc:
            errors.append(f'{ident}: {exc}')
            continue
        if record.get('contentSha256') != content_hash(text):
            errors.append(f'{ident}: stale content hash; review metadata before refreshing')
        if type(record.get('wordCount')) is not int or record['wordCount'] != word_count(text):
            errors.append(f'{ident}: incorrect word count')
    # Discover substantive pages in all catalog sections, including application supplements.
    infrastructure = {'README.md', 'INDEX.md', 'STRUCTURE.md', 'SUMMARY.md', 'AGENTS.md',
                      'PUBLICATION_RULES.md', 'PROJECT_TEMPLATE.md', 'PROJECT_INDEX.md'}
    expected = {p.name for p in root.glob('*.md') if p.name not in infrastructure}
    for section in catalog['sections']:
        folder = safe_path(root, section['key'])
        expected.update(p.relative_to(root).as_posix() for p in folder.rglob('*.md')
                        if p.relative_to(root).as_posix() != section['index'])
    errors += [f'Uncataloged content: {p}' for p in sorted(expected - paths)]
    if check_overview and not errors:
        dest = root / 'SUMMARY.md'
        if not dest.exists() or normalized(dest.read_text(encoding='utf-8')) != render(catalog):
            errors.append('SUMMARY.md is missing or stale; run build')
    return errors


def write_catalog(root, catalog):
    path = Path(root) / 'catalog.json'
    temp = path.with_suffix('.json.tmp')
    temp.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    temp.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['check', 'build', 'refresh'])
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--reviewed', action='append', default=[], help='Record ID whose metadata was reviewed against current text')
    args = parser.parse_args()
    catalog = json.loads((args.root / 'catalog.json').read_text(encoding='utf-8'))
    if args.command == 'refresh':
        if not args.reviewed:
            parser.error('refresh requires explicit --reviewed ID (repeat for multiple records)')
        selected = set(args.reviewed)
        if selected - {r['id'] for r in catalog['records']}:
            parser.error('Unknown reviewed record ID')
        for record in catalog['records']:
            if record['id'] in selected:
                stamp(record, safe_path(args.root, record['path']).read_text(encoding='utf-8'))
    errors = validate(args.root, catalog, check_overview=args.command == 'check')
    if errors:
        raise SystemExit('\n'.join(errors))
    if args.command == 'refresh':
        write_catalog(args.root, catalog)
    if args.command in ('build', 'refresh'):
        (args.root / 'SUMMARY.md').write_text(render(catalog), encoding='utf-8', newline='\n')
    print(f"PASS: {len(catalog['records'])} records; {word_count(render(catalog)):,} overview words")


if __name__ == '__main__':
    main()
