# Daniel Powell Public Archive Agent Rules

- Treat this repository as public. Never copy raw private notes, research packets, correspondence, source drawings, contracts, invoices, or unreviewed media into it.
- Read `PUBLICATION_RULES.md` before adding or materially revising a record.
- The private research and approval layer remains outside this repository and must never be described by local path in public files.
- Use stable `PUB-0000` identifiers that do not match internal job numbers.
- Preserve the exact approved LinkedIn commentary under `## LinkedIn Summary` when a record originates from the LinkedIn publishing queue.
- Expand project records only from documented evidence or direct user confirmation. Do not infer project-specific facts from general capabilities.
- Separate Daniel's role from overall project scope and state completion status precisely.
- Remove names, direct addresses, contact information, private companies, identifiers, local paths, private filenames, wiki links, credentials, and identifying combinations of facts.
- Add only sanitized derivative images after metadata stripping, OCR, visual inspection, and explicit approval.
- Require a passing privacy audit and Daniel's separate explicit approval for the expanded record. LinkedIn approval alone is insufficient.
- Review `git diff`, repository status, commit identity, and remote output before publication.
- For approvals granted after 2026-08-06, Daniel's explicit approval of the expanded GitHub record authorizes its immediate scoped production commit and push unless he explicitly requests a hold. LinkedIn approval remains queue-only and does not authorize GitHub by itself.
- For media-first posts, commit and push only an explicitly approved sanitized asset, verify its direct public URL, and return that URL to the LinkedIn workflow for final payload review.
- Stage only approved record, index, and media paths. Never include unrelated dirty-worktree changes; stop if unrelated edits overlap a file the approved publication must modify.
- Confirm the target remote and branch before production publication; the current production target is `origin/main`.
- After every push, verify the live Markdown page and each direct media URL before reporting production success.
