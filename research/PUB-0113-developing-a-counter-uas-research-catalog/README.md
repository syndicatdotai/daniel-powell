# Developing a Counter-UAS Research Catalog

My interest in counter-UAS began around 2017. What fascinated me was the asymmetry of the problem. A small group with moderate technical capability can use commercially available drones to threaten, disrupt, or damage a much larger and better-resourced organization. The resources needed to create a disruption can be far smaller than those required to prevent it or respond.

That imbalance creates questions that extend beyond the aircraft itself. Technology, operating conditions, legal authority, and the consequences of disruption all shape the defensive problem. Understanding how those factors interact became the foundation of my research and the development of C-UAS Systems.

Counter-UAS research brings together several different questions. What activity has been reported? What evidence supports the report? Which technologies address the problem? What does a supplier actually claim its system can do, and which authorities govern its use?

C-UAS Systems grew from an effort to organize those questions into a useful research resource. The work began with collecting company information, incident reporting, definitions, and reference material. It developed into a structured catalog covering companies, incidents, news, legal authorities, and technical resources.

My role combines subject research, source evaluation, information architecture, and application development. The objective is to make the reasoning behind a record available alongside its summary, so a reader can follow a statement back to the material supporting it.

## Bringing different kinds of evidence together

The research examines counter-drone technology in the context of documented activity and the requirements of the places being protected. Public reporting covers airports, critical infrastructure, military facilities, prisons, and other environments. Those reports vary considerably in what they establish.

An incident record needs to distinguish a reported sighting from corroborated activity. A technology announcement needs to identify whether it describes a demonstration, a trial, a procurement decision, or a deployed capability. A company page needs to distinguish the supplier's statements from independently documented results.

That distinction shapes the catalog. Each type of record has its own research questions, while a common structure keeps the information readable across the collection.

## Developing the record structure

The implemented catalog uses typed records with stable identifiers, titles, summaries, dates, locations, topics, and direct source links. Expanded descriptions carry the detail that would be lost in a collection-card summary.

Separate fields hold facts, capability information, and interpretation. That structure gives the research a place to record what a source says and a separate place to explain its significance.

Dates are part of the evidence. A publication date, the period an event occurred, and the date information was captured can describe different things. Retaining that context helps a reader understand the age of the material being presented.

The application generates collection views and individual record pages from the same data. This keeps the expanded account and the browsing interface connected to a common record.

## Reading technology claims carefully

A company can describe several functions across its products, partners, and integrations. Researching the offering requires examining where each function comes from.

The catalog distinguishes native capabilities from integrated or optional capabilities. It also records when a function is not stated in the available documentation. Detection, classification, tracking, identification, command-and-control, and mitigation claims are considered according to the supporting source material.

This produces a more precise description of the offering. A capability available through a partner integration has a different place in the record from one supplied directly by the platform. Recording that relationship helps preserve the meaning of the original documentation.

## Connecting incidents with their documented outcomes

Incident research follows the sequence of what was reported and what was subsequently established. The affected location or mission, operational window, reported disruption, official response, and documented outcome all contribute to the account.

Later reporting can change how an earlier event is understood. An enforcement action, investigation result, or official statement may add evidence absent from the initial report. The research process therefore considers follow-up material alongside the first source.

The catalog's ingestion standard calls for independently useful corroboration when available. A second source earns its place by adding evidence, a later outcome, or material context. Direct links let a reader examine those sources themselves.

## Keeping legal material tied to its source

Legal and policy research is organized around the issuing body, jurisdiction, instrument, date, actors covered, and actions described. The record also captures stated limits, coordination requirements, and oversight provisions where relevant.

This is an important part of understanding counter-UAS material. A technology description and an authority to use it answer different questions. The catalog preserves the source context around both.

The research draws on statutes, regulations, official guidance, government publications, and decisions. Summaries are written around what those documents establish and link directly to the source.

## Using AI within a defined research process

AI assists with searching for candidate material, organizing findings, comparing records, and developing source-attributed descriptions. The documented automation workflow covers both new reporting and older material that adds context to the collection.

Candidate records are compared with the existing catalog using titles, organizations, products, source URLs, dates, locations, and official identifiers. That comparison determines whether the material adds a new record or improves one already present.

A small, coherent batch is the unit of work. The workflow allows a research run to end without a content change when the available sources are weak, inaccessible, or duplicative. That keeps the research directed toward additions with a documented basis.

## Building a research interface

The developed application brings the catalog into a searchable and browsable interface. Collection cards provide an entry point, while expanded records retain source links, facts, capability descriptions, and analysis.

The implementation includes expanded and compact reading modes, adjustable text size, and machine-readable descriptions for AI and indexing tools. Those presentation options use the same underlying records, preserving the content across different ways of reading it.

Rendered-page checks cover the research presentation as well as the application. The checks verify that records contain substantive expanded text and that the expected content appears on the generated pages. Static export tooling produces a publishable set of pages from the developed catalog.

## Preserving the research as it develops

Source collection, record structure, and publication tooling form parts of the same project. The work gives a finding a route from an original document into a traceable record and then into a readable research page.

This account describes the developed research catalog being prepared for public release. Its record structure, research standards, interface, and publication tools form the basis of that release.

C-UAS Systems is an application of research discipline to an evolving technical subject. Its central contribution is the organized connection between reported activity, technology documentation, legal sources, and the evidence supporting each account.

[Visit C-UAS Systems](https://www.c-uas.systems/)
