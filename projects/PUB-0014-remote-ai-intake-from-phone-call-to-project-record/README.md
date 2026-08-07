# Remote AI Intake from Phone Call to Project Record

## LinkedIn Summary

AI becomes most useful to me when it closes the gap between a field conversation and an organized project record.

After a call with a new customer, I may still be at a jobsite or traveling between projects with no laptop available. Through the Codex remote connection, I can send one plain-language message containing the information I just received. Purpose-built skills then route that information through my local operating system.

The entity workflow searches existing records first to prevent duplicates, then creates or updates the customer record with the available contact and project information. Job intake determines whether the work belongs to an existing project or needs a new one, creates the standard folder structure and canonical project note, and connects the customer, property, and initial job facts. Incomplete or conflicting information is placed into review instead of being guessed.

If the call includes a follow-up meeting or site visit, the scheduler creates the internal record and the Google Calendar connection projects a sanitized event with the relevant operational notes.

I do not currently use a conventional CRM. The source of truth is stored locally in readable Markdown with structured data supporting the automations. It is synchronized through Dropbox and versioned in a private GitHub repository, giving me redundancy, history, and control over the records.

The value is not simply remote text entry. A short field prompt can activate a repeatable workflow across customer intake, project creation, contact organization, scheduling, and calendar coordination. Office review still matters, but the administrative setup no longer has to wait until I am back at a computer.

The same architecture is adaptable to a conventional CRM. With the appropriate MCP or API connector, the validated structured information could be routed into an existing platform while preserving the same matching, review, and privacy rules.

#ArtificialIntelligence #ConstructionTechnology #Codex #FieldOperations #Automation

## Overview

Daniel Powell uses a local-first, AI-assisted workflow to turn information received during a customer phone call or text exchange into organized business records while he is still in the field. A plain-language instruction sent through a remote Codex connection can initiate customer resolution, project setup, contact organization, scheduling, and calendar coordination without requiring immediate access to a laptop.

The system is not a conventional CRM. Human-readable Markdown is the primary record, while structured data and purpose-built Codex skills provide deterministic routing, validation, duplicate checks, and projections into other systems. The working vault is synchronized through Dropbox and versioned in a private GitHub repository.

| Record field | Public information |
|---|---|
| Public record ID | PUB-0014 |
| Period | 2026 |
| Operating context | Field and remote administration |
| Primary interface | Plain-language instruction through a remote Codex connection |
| Source of truth | Local Markdown notes with supporting structured records |
| Core workflows | Entity intake, job intake, scheduling, calendar projection, and review queues |
| Synchronization | Dropbox |
| Version history | Private GitHub repository |
| CRM status | Local-first system; no conventional CRM currently used |
| Extension path | Validated records could be routed through MCP or API connectors |

## Role

Daniel designed and operates the workflow around the way customer and project information arrives during field work. He provides the initial facts in natural language, reviews uncertain matches or incomplete information when necessary, and remains responsible for the business decisions represented by the records.

Codex functions as the intake and orchestration layer. The individual skills define how customer entities, project folders, schedule records, and calendar projections are resolved and maintained. The automation reduces repetitive entry but does not remove review or authorize the system to invent missing facts.

## Field Intake Context

A new inquiry may arrive while Daniel is on a jobsite or traveling between projects. The initial call or text can include a customer name, contact information, property location, a short description of the requested work, and a proposed follow-up date. Without a remote workflow, that information would remain in temporary notes until he returned to a computer and entered it into several places.

The remote Codex connection allows the same information to be submitted as one plain-language instruction. The prompt does not need to reproduce a database form. The skills interpret the request, search the existing system, and route each supported fact to the record that owns it.

## Workflow Architecture

1. **Remote input:** Daniel sends a concise natural-language summary of the completed call or text exchange.
2. **Entity resolution:** The entity-intake workflow searches existing customers, contacts, aliases, jobs, and recent context before deciding whether to update an existing record or create a new one.
3. **Project resolution:** Job intake checks whether the work already exists. When the instruction confirms new work, it creates the standard job folder, canonical project note, and appropriate supporting structure.
4. **Information routing:** Available contact fields, property information, initial scope facts, and relationship context are placed in their appropriate private records.
5. **Schedule creation:** A confirmed meeting or site visit becomes a structured scheduler record linked to the appropriate project.
6. **Calendar projection:** Codex applies the sanitized schedule plan to Google Calendar through the connected calendar interface. Internal evidence, raw prompts, and private automation identifiers stay out of the event.
7. **Review handling:** Incomplete, conflicting, or weakly matched information is placed into a review queue instead of being silently guessed.

## Scope Of Work

The current workflow supports:

- Remote intake after customer calls and text exchanges.
- Duplicate-aware customer and contact resolution.
- Creation or update of private entity records.
- Standardized job-folder and project-note creation for confirmed new work.
- Connection of customers, properties, and initial project facts.
- Structured scheduling of meetings and site visits.
- Sanitized Google Calendar projection.
- Dropbox synchronization of the working vault.
- Private GitHub version history and recovery support.
- Human review for ambiguity and incomplete records.

## Key Actions

- Converted a field conversation into one structured intake instruction.
- Used entity matching before creating a customer record.
- Routed contact and project facts to their canonical records.
- Created repeatable project scaffolding for confirmed new work.
- Connected dated follow-up work to the vault-native scheduler.
- Projected approved operational information into Google Calendar.
- Preserved review gates for uncertain or conflicting data.

## Important Features

- Natural language as the field-facing interface.
- Purpose-built skills rather than one unrestricted automation prompt.
- Local ownership of the primary business records.
- Human-readable Markdown combined with structured automation data.
- Search-before-create rules to reduce duplicates.
- Explicit ownership boundaries between customer, job, schedule, and calendar systems.
- External calendar entries sanitized separately from private source records.
- Synchronized working files and private version history.
- A connector-ready architecture that is not tied to one CRM vendor.

## Constraints And Decisions

The workflow intentionally keeps the local vault as the source of truth. Google Calendar is an external projection, not the only schedule record. Dropbox provides synchronization, while private version control provides change history and recovery. These layers serve different purposes and are not treated as interchangeable.

Automation is allowed to organize supported facts, but it is not allowed to guess customer identities, addresses, project relationships, dates, or missing scope. Strong matches can be processed directly; weak matches are held for review.

Customer details remain private. Public documentation describes the schema and workflow but does not expose real contact information, project addresses, repository identifiers, access methods, credentials, or calendar records.

## Deliverables

For a confirmed new inquiry, the workflow can produce a resolved or newly created customer record, a canonical project folder and note, linked initial project facts, a structured schedule entry, and a sanitized Google Calendar event when a meeting has been confirmed.

It also produces the less visible operational records needed for reliability: structured metadata, source references, run logs, review items, and version history.

## Outcome

The system shortens the delay between receiving information and organizing it. Administrative setup can begin while Daniel is still in the field, reducing dependence on memory, loose notes, or a later session at a laptop.

Office review remains part of the process, especially when the initial information is incomplete or a matching decision is uncertain. The improvement is that the basic project record, relationships, and follow-up schedule can already be organized before that review occurs.

## CRM And MCP Adaptability

The workflow separates natural-language intake from the storage destination. Today, the validated information is routed into local Markdown and structured records. If an organization already uses a CRM, the same intake and validation layer could map the approved fields into that platform through an MCP connector or conventional API.

That extension would change the destination, not the operating principles. Duplicate checks, explicit field mapping, review queues, privacy controls, and human approval would still be required.

## Tools And Methods

- Codex remote connection
- Purpose-built Codex skills
- Natural-language intake
- Markdown knowledge base
- Structured JSON records
- Entity matching and classification
- Canonical job scaffolding
- Vault-native scheduling
- Google Calendar connector
- Dropbox synchronization
- Private Git version control
- Review queues and validation rules
- MCP and API integration patterns

## Evidence And Limitations

This record is based on Daniel's direct description of his current operating method and the reviewed local workflow documentation. The entity, job, scheduler, calendar, synchronization, and private version-control components are documented. No customer record or live project data was copied into this public account.

The record describes the workflow's supported behavior, not a guarantee that every intake can be completed without clarification. Source quality matters. A short prompt can initiate the process when it contains enough reliable information, while ambiguous or incomplete cases require review.

The CRM discussion describes architectural portability. It does not claim that a production CRM integration is currently active. Any future connector would require platform-specific authentication, field mapping, permission controls, testing, and audit rules.
