# Archive Structure

The archive groups articles by their main subject. Each article has one canonical location, listed in [catalog.json](catalog.json) and the [complete index](INDEX.md).

- Single articles use descriptive Markdown filenames within a subject folder.
- Existing publication records retain their `PUB-0000` identifiers in filenames or catalog entries.
- Applications use a dedicated folder with `overview.md` as the main document, leaving room for related technical commentary.
- Section navigation lives in `index.md`. The root `README.md` is the archive landing page.
- Images use `assets/PUB-0000/` so their locations can remain independent of article filenames.
- Background and workshop pages without publication numbers keep descriptive filenames and catalog references.

The catalog includes earlier public paths for moved records. Those paths document the migration; they are not redirects. Use each record's `path` for its current location.

[About Daniel Powell](ABOUT.md) · [Complete index](INDEX.md)

## Discovery summaries

[SUMMARY.md](SUMMARY.md) provides a short overview of every canonical content document, grouped by subject. The catalog stores summaries, search tags, optional role and period information, word counts, and content hashes. Use this overview to select relevant articles, then read their full text for detailed claims.

Summaries are maintained with article revisions and generated from the catalog. See [summary maintenance](scripts/ARCHIVE_SUMMARIES.md) for the format and validation commands.

## AI Experiments

[AI Experiments](ai-experiments/index.md) collects experiments in AI roles, automation, and evaluation. Each account describes the method, outputs, and development status.
