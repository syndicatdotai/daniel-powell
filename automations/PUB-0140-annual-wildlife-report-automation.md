# Developing an Automation for Annual Wildlife Activity Reports

Annual reporting is one of the administrative responsibilities attached to my nuisance-wildlife work. The information originates in individual assignments throughout the year, but the final deliverable is a concise government form with a fixed structure.

I developed an AI-assisted workflow to connect those two parts of the work. Field notes and photographs provide the history, structured records organize the report entries, and a Python renderer prepares the official Connecticut Department of Energy and Environmental Protection activity-report PDF.

Building that workflow involved repeated review and adjustment. The process developed through working with actual records, checking what the automation produced, correcting the interpretation or presentation, and carrying those improvements into reusable instructions and code.

## The Operational Problem

A wildlife assignment can involve an initial call, an inspection, several visits, observations, and handling outcomes recorded at different times. Those events need to remain connected to the same job while retaining their individual meaning.

The annual form asks for a smaller set of information: the job, when work began, the town, species, activity quantities, methods, and dispositions. Preparing the report means translating the detailed working history into those fields.

The objective was to reuse the information already captured during the work and produce a document that could be reviewed against its sources.

## Starting with Field Records

I dictate job updates and save photographs with explanatory context. AI helps organize that information into Markdown job records in Obsidian.

Those records preserve the sequence of work. A later update can add an outcome without discarding the earlier observation that explains it. Photographs and broader notes remain associated with the assignment even when they are not part of the state submission.

The reporting workflow starts from that history. It identifies the relevant activity and prepares a concise representation for the annual form.

## Developing the Automation Through Iteration

An initial generated report gives me something to inspect. It also exposes where the instructions, source interpretation, or rendering rules need more work.

The development process involved checking both the content and the presentation. Did an entry use the date work began? Were multiple species associated with the correct quantities? Did the recorded outcomes explain the totals? Was the result readable within the form's narrow cells?

When an output needed correction, the next step was to establish where that correction belonged. A missing fact required clarification of the source record. A recurring interpretation issue belonged in the reporting instructions. A layout problem belonged in the renderer.

That distinction made the development useful beyond a single PDF. The report could be corrected, and the preparation method could improve at the same time.

The resulting workflow includes instructions for selecting documented work, distinguishing inquiries from site activity, reconciling outcomes, and inspecting the finished form. Those instructions developed alongside the software through the review process.

## Separating Judgment from Document Assembly

AI supports finding and organizing information across the job records. I supply the field knowledge and resolve questions about what actually occurred.

The report entries are then represented in an editable JSON source. That source holds the reporting year, row values, activity counts, and totals separately from the document layout.

Python handles the repeatable operations: reading the report data, applying checks, populating the form, and saving the output. A correction to a row can be made in the source and carried through another render.

This gives each part of the system a defined responsibility. Job records retain the working history, report data expresses the selected entries, instructions guide interpretation, and code handles the document operations.

## Reconciling Activity Before Producing the Form

The preparation process distinguishes a request for service from recorded work. The start date comes from documented activity, and inspection-only assignments retain their meaning without implying that animals were handled.

Where animals were handled, the recorded quantities are checked against their dispositions. Incidental captures are considered where they form part of the activity. An unresolved outcome becomes a question to clarify before the report is finalized.

The renderer also checks the structured data. It requires consecutive report numbering, reconciles activity quantities with recorded outcomes, and compares supplied totals with the underlying entries.

Those checks turn recurring requirements into explicit rules. They provide a consistent way to catch particular discrepancies each time the report is generated.

## Working with the Official PDF

The document renderer uses the official fillable report as its template. **PyMuPDF** handles field population and formatting, while **pypdf** inspects the saved result.

The implementation checks the expected page dimensions and field structure before applying its layout rules. That provides a way to identify a changed template rather than silently placing information according to an older form.

The layout was refined around the practical constraints of the report: concise descriptions, readable dates, narrow columns, and aligned species and quantity information. Supporting more than one page required page numbering and distinct interactive field names across continuation pages.

These are small implementation details with a direct effect on the deliverable. The report needs to contain the intended information and present it clearly in the required format.

## Reviewing What the PDF Stores and Displays

Verification takes place at more than one level.

The renderer reopens the PDF and checks the page count and interactive fields. It compares the logical values with those attached to the visible widgets and verifies appearance information for populated fields.

Visual review then examines the rendered pages for clipping, alignment, crowded entries, and the placement of dates and species. This checks the document as it will actually be read.

The reusable workflow has also been checked with unsigned and multi-page outputs, and its validation rejects unreconciled counts. Signing remains a separate step performed with my direction.

## Preserving the Reusable System

The retained materials include the job history, the annual reporting record, editable report data, the applicable official forms, and the finished PDF.

The renderer is shared rather than copied into each reporting folder. Reusable instructions explain how to prepare and verify the report, while the annual source holds the information specific to that period.

That structure lets a future report reuse the method without inheriting an earlier year's activity. Changes to the form, the source information, or the reporting process can be addressed in the appropriate part of the workflow.

## What This Automation Demonstrates

The workflow has produced a completed annual report from retained job records and my clarifications. Final submission to DEEP follows a separate review and decision.

The development work illustrates how I approach business process automation: work from an actual recurring requirement, define the inputs and output, inspect the generated result, and improve the instructions and implementation through use.

The useful system is the combination of source records, judgment, structured data, code, and review. Each correction can improve the next run when it is captured in the part of the process responsible for it.

## Tools and Related Records

Voice dictation, AI-assisted organization, Obsidian, Markdown, JSON, Python, PyMuPDF, pypdf, official PDF forms, data reconciliation, and visual document inspection.

- [From Field Voice Notes to Annual Wildlife Reports](../workflows/PUB-0081-wildlife-reporting.md)
- [Obsidian Skills and Automation Systems for a Solo Operator](../workflows/PUB-0008-obsidian-business-automation.md)
- [Designing Business Documents with Code](../workflows/PUB-0128-code-driven-business-documents.md)
- [Technical Stack and Development History](../background/technical-stack.md)
- [Connecticut DEEP reporting information and forms](https://portal.ct.gov/DEEP/Wildlife/Nuisance-Wildlife/Information-for-Licensed-NWCOs)
