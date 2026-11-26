# Archive summary maintenance

`catalog.json` is the source for discovery metadata. `SUMMARY.md` is generated from it. Read summaries to select relevant documents, then read their canonical full text for detailed claims.

Each substantive content record has `summary`, `tags`, `wordCount`, and `contentSha256`. Optional `role` and `period` describe only information present in the article. Existing IDs, paths, and `legacyPaths` remain authoritative. `summaryVersion: 1` enables this additive contract without changing the existing catalog schema or layout versions.

Summaries usually contain 40–70 words, explaining the subject, contribution, and outcome or stage. Shorter text is appropriate for small articles. Tags contain 3–8 distinct lowercase hyphenated terms. Prefer specific activities and techniques over promotional language. Keep summaries grounded in public prose; review them with the document they describe.

## Commands

From the repository root, using Python 3.10 or later:

```text
python scripts/archive_summary.py check
python scripts/archive_summary.py build
python scripts/archive_summary.py refresh --reviewed PUB-0088
python scripts/archive_summary.py refresh --reviewed background:career --reviewed background:about
python -m unittest discover -s scripts -p "test_*.py"
```

`check` is read-only and verifies coverage, metadata, content hashes, word counts, and overview freshness. `build` regenerates the overview only when the catalog matches the articles. `refresh` requires explicit reviewed IDs, recalculates their computed fields, validates the catalog, and regenerates the overview. It does not write summaries or determine whether prose is factually accurate. Review unchanged summaries against edited articles before refreshing hashes.

The SHA-256 covers complete Markdown with line endings normalized to LF and an optional initial byte-order mark removed. Word counts include headings, table text, IDs, and link labels; exclude Markdown link destinations, HTML tags/comments, and bare URLs. Hyphenated words and contractions count as one. Counts are for discovery and are not model-token estimates.

## Coverage and changes

Substantive Markdown within every catalog section, including application supporting pages, must have a record. ABOUT.md is also included. Section indexes, root navigation, this maintenance documentation, scripts, generated SUMMARY.md, and assets are infrastructure, not article summaries. New root Markdown pages outside the named navigation and authoring infrastructure are also checked for catalog coverage. Add substantive pages to the catalog or place them in a subject section.

New categories are discovered from `sections`; no hardcoded subject list is required. Moves preserve IDs and refresh links; removals require removing the intended entry and checking inbound links. Add substantive application supplements with descriptive stable references when a PUB identifier is not appropriate. Preserve existing publication-number allocation rules.

Change catalog metadata and generated SUMMARY.md together. Publish them with the approved article and affected indexes. Existing article bodies and LinkedIn summaries are independent of this generated discovery layer.
