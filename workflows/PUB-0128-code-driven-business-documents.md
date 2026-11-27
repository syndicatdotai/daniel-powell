# Designing Business Documents with Code: A Flexible System for Estimates, Invoices, and Contracts

**Public project ID:** PUB-0128

I develop document-generation systems that use structured records, HTML, CSS, JavaScript, and PDF libraries to produce the documents used in my construction business.

Instead of building every estimate, invoice, or contract through manual formatting in a word processor, I maintain reusable instructions and scripts that assemble the information, apply the appropriate layout, and generate the finished document.

This approach gives me direct control over both the content and its presentation. A document can be tailored to a particular assignment, revised as the scope changes, and reproduced from its underlying records.

The result is a flexible document-production workflow that connects business information with custom client-facing output.

## Separating the Information from the Page

The foundation of the system is a distinction between the information a document contains and the way that information is displayed.

A construction estimate might contain scope descriptions, quantities, prices, alternates, assumptions, and exclusions. An invoice adds billing and payment information. A contract introduces agreement-specific terms, payment schedules, and signature sections.

Those details are maintained in structured records, commonly JSON files. The record holds the information the system needs to produce the document, while a separate template or rendering script determines its appearance.

That separation makes revision more manageable. A scope change can be made in the underlying record and carried into a regenerated document. A presentation change can be made in the template without requiring the business information to be re-entered.

The PDF is the deliverable. The structured record and editable layout preserve the ability to produce it again.

## Using Web Technologies for Document Design

HTML and CSS provide a practical environment for designing business documents.

HTML defines the structure: headings, paragraphs, scope sections, tables, totals, terms, and signature areas. CSS controls typography, spacing, borders, alignment, page dimensions, and print layout.

JavaScript supports the export process. In the contract workflow, a script opens the HTML through a browser automation tool and generates a PDF using the browser’s print engine. The export includes defined paper dimensions, margins, printed backgrounds, and page numbering.

This makes document design similar to developing a small, purpose-built web page. The layout remains editable, and changes can be expressed directly through code.

For my workflow, that is an accessible way to create custom documents. I can describe the desired adjustment to Codex, have it modify the source, inspect the result, and refine it further.

The adjustment might involve reorganizing a scope, changing the hierarchy of headings, improving a pricing table, or making a signature section fit more naturally on the page.

## Choosing the Appropriate PDF Renderer

The system supports more than one route to a finished PDF.

Contracts use an HTML-to-PDF workflow. Estimates and invoices also have a Python rendering path built with ReportLab, a PDF-generation library.

Both approaches serve the same underlying objective: generate a consistent document from maintained information and reusable presentation rules.

The HTML route offers direct control through web layout and print styling. The PDF-library route supports programmatic construction of paragraphs, tables, spacing, and page elements from document records and template settings.

Keeping those options available makes the system more adaptable. A particular document does not have to be forced through one rendering method when another is better suited to its layout or existing workflow.

## Skills Turn the Tools into a Repeatable Process

The scripts handle specific operations. The skills explain how those operations fit into the business workflow.

A skill is a reusable set of instructions that tells the AI how to approach a task: which records to read, which document type to use, what information is required, how to validate it, and where the finished output belongs.

My client-document skill distinguishes ordinary pricing documents from contracts and signed obligations. It directs Codex to verify the associated job, update the structured source, validate the information, and use the appropriate rendering tools.

It also defines what belongs in the customer-facing document. Internal research, source references, working notes, and operational details remain separate from the presentation delivered to the client.

This captures the production method alongside the code. The next document starts with an established workflow rather than a fresh set of instructions reconstructed from memory.

## Tailoring Documents to the Assignment

Construction documents vary considerably in scope and complexity.

A straightforward service invoice may need a concise description, a charge, and a balance. A larger estimate may need several scope sections, optional work, adjustments, exclusions, and acceptance information.

The estimate and invoice system includes different presentation templates, including compact proposals, formal proposals, field tickets, and plain service invoices. Template settings control presentation details, while the document record supplies the content.

That allows the output to follow the assignment.

A short document can remain short. A more detailed proposal can accommodate the information needed to explain the work. Contract layouts can organize scope, payment terms, exclusions, and signatures around the agreement being prepared.

The templates provide a starting point that can be extended as recurring needs emerge.

## Validation Before Presentation

The workflow includes checks before a document is treated as finished.

The scripts validate required fields and calculate financial information from the structured records. Depending on the document type, that includes line-item amounts, adjustments, payments, totals, and balances.

The contract workflow checks the information required for a final document, including the parties, scope, payment terms, and relevant contact details.

These checks help catch omissions and inconsistencies before they become part of a polished PDF. The underlying business decisions—what work is included, what it costs, and which terms apply—still come from the project information and my direction.

Automating the document does not change who makes those decisions.

## Reviewing the Rendered Result

A document also needs visual review.

Correct information can still produce a poor page: a table may become crowded, a heading may separate from its text, or a signature area may fall awkwardly across a page break.

The workflow therefore includes inspection of the rendered output before replacing the current PDF. The editable HTML remains available where it is used as the layout source, allowing further revisions without reconstructing the document from its exported form.

The system also distinguishes working drafts from documents that have already been issued, approved, signed, or paid. Ordinary iterations can replace earlier previews, while record-bearing versions are preserved.

That supports a cleaner working environment without losing meaningful document history.

## Connecting Documents to the Business

The finished documents remain associated with their verified jobs.

Estimates and invoices have central records and indexes, with current PDFs copied into the relevant job folders. Changes to amounts, payments, or status feed back into the tracking system.

Contracts maintain their structured information alongside the project, with the customer-facing documents kept separate from backend production material.

This gives the document a place in the wider business workflow. It can be found through the job, revised through its source, and tracked through the appropriate records.

## Extending the System Through Use

One of the main benefits is the ability to improve the system incrementally.

When a recurring document needs a better layout, an additional field, or a more useful validation check, that improvement can become part of the reusable workflow. A problem solved for one assignment can inform the next.

Some changes belong to a particular document type. Others—such as better source handling, rendering checks, naming, or storage—can improve several related workflows.

This is how I use software development within everyday business operations: identify a recurring need, build a manageable tool around it, and refine the system through actual work.

For estimates, invoices, and contracts, the combination of structured records, editable layouts, rendering scripts, and AI skills gives me a document-production environment that I can shape around the business.
