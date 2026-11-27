# Job Brain: Finding a Simpler Way to Organize My Business

**Public project ID:** PUB-0124

## Overview

Job Brain was an early attempt to use AI-assisted software development to organize the information behind my construction and drafting business. The goal was to capture daily notes, connect them with jobs and people, keep track of tasks and commitments, and make that information available through a simple interface.

At the time, building an application seemed like a natural way to apply AI to the business. Instead of repeatedly handling the same administrative work, I could develop software that understood the information and helped manage it.

The application developed into a substantial project, with a mobile interface, AI requests, hosted data, authentication, indexing, and retrieval. I shifted my focus from Job Brain to a lighter workflow built around Markdown, reusable skills, and scripts. Developing the application helped clarify what the business needed and how much of it could be handled with simpler tools.

The business requirements remained. They were eventually handled through a lighter system built around Markdown files, reusable skills, and scripts, with Obsidian and Codex providing the working environment.

## The Business Problem Behind the Application

Running the business generated information throughout the day: site observations, measurements, conversations, changes in scope, materials to collect, appointments, and promises to follow up.

Much of that information crossed several categories at once. A single note could concern a particular job, mention a subcontractor, record a decision, and create something that needed attention later. Capturing the words was only the beginning. The information also needed to remain connected to the work it described.

Job Brain was intended to handle that organization behind a straightforward interface. Text or voice could be captured without requiring every detail to be manually filed first. The system would preserve the original input, identify useful relationships, and retrieve relevant information when asked.

## What Was Built

The implemented application used a mobile-first daily-notes and chat interface. Notes provided a dated source record, while chat and voice capture offered ways to add information and ask questions about it.

Behind that interface, the system maintained several related layers:

- Original notes, chat history, and raw inputs.
- Jobs, entities, and extracted knowledge.
- Job summaries, timeline events, and open commitments.
- Searchable note sections and semantic retrieval.
- Answer traces and references to supporting source material.

Preserving the original material was an important design decision. An extracted summary could organize information, but the underlying note needed to remain available so an answer could be checked against its source.

The retrieval work also became more involved. The application distinguished immediately relevant job context from broader background material and combined structured records with searches across the notes. The objective was to answer questions using the business's recorded history rather than relying on an AI model to reconstruct missing context.

## The Technology Behind the Interface

Job Brain used Next.js, React, and TypeScript for the application. Supabase provided authentication, a PostgreSQL database, and file storage. OpenAI APIs and the Vercel AI SDK supported the AI request and response workflow, with additional work on voice capture and transcription.

The database held both original information and derived structures. Search combined text matching with embeddings, allowing retrieval to work with wording and meaning. Backend processes handled ingestion, indexing, and the connections between notes and job memory.

Testing became another part of the project. A scenario-based harness could supply contractor-style notes, run the processing workflow, ask follow-up questions, and inspect whether answers contained the expected facts and sources.

Each of these components addressed a real application concern. Together, they created a significant system to develop, connect, test, and maintain before the simple interface could reliably do its job.

## Reconsidering the Amount of Software Required

As development continued, more attention went into the application infrastructure: how information should be stored, how records related to one another, how the AI should retrieve them, and how the interface should communicate what was happening.

For a solo business, that effort had to be considered alongside the work the system was supposed to support. The underlying requirement was practical: capture information, retain its context, find it again, and carry out recurring procedures consistently.

Those requirements did not all require a dedicated application with its own frontend, backend, database, and hosted services. Much of the useful behavior could be expressed through readable records and clear operating instructions, with small scripts handling the parts that benefited from predictable execution.

That realization changed the direction of the work. Job Brain had become overengineered for my needs, and continuing to build it was no longer the most useful way to improve the business workflow.

## The Workflow That Replaced It

The current system keeps its working history in Markdown files. Jobs, people, companies, decisions, and related material remain readable in Obsidian and can be linked directly to supporting documents.

Codex helps capture and organize information, retrieve context, and execute established procedures. Reusable skills describe how a particular task should be handled: where its information comes from, which record is authoritative, what checks are required, and where the result belongs.

Scripts handle operations that benefit from explicit inputs and repeatable behavior. Structured files support tasks, schedules, and business documents where stable identifiers or calculations are useful. Markdown remains the readable context around those records.

This gives the workflow room to expand incrementally. A recurring administrative task can become a skill or a focused script without first becoming a new screen, database feature, or application service.

The records and supporting tools run from the local working environment and can be backed up or versioned through Dropbox and private GitHub repositories as appropriate. The AI services are still part of the workflow, but keeping the business records useful does not require maintaining a separate custom web application around them.

## What Carried Forward

Several ideas from Job Brain carried forward into the lighter workflow: preserve the original input, keep decisions connected to their jobs, distinguish recorded facts from interpretation, and make answers traceable to supporting information.

Those principles carried into the file-based workflow. The implementation became lighter, while the attention to source material and context remained.

Job Brain also changed how I evaluate new automation ideas. Before starting another application, I consider whether the requirement can be handled by an existing tool, a clearer record, a reusable skill, or a small script. A dedicated application remains an option when the work justifies it.

## Outcome

I shifted my focus from Job Brain to the lighter workflow used in my business. The development work clarified what the business actually needed and helped shape the lighter system used instead.

The useful result was a different approach to systematizing the work: start with the information and procedures, use the simplest implementation that serves them, and add application infrastructure when there is a practical reason for it.

Related commentary: [Obsidian skills and business automation](../../workflows/PUB-0008-obsidian-business-automation.md) · [Keeping job conditions and notes](../../workflows/PUB-0117-job-conditions-and-notes.md)
