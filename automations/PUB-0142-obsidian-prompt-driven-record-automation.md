# Prompt-Driven Obsidian Automation for Work and Personal Records

## LinkedIn Summary

I use Obsidian to keep track of my work and personal information, with Codex helping me put it where it belongs.

A lot of this automation starts when I give it a prompt. I can describe several things together, and it separates the information, finds the existing records, and updates the appropriate files and folders.

Work is the biggest part of it. That includes creating jobs when I ask, keeping track of organizations and contacts, and recording information from phone calls, texts, and emails. I also use it for personal events, health and wellness notes, and sometimes keeping track of what I eat.

Behind that are reusable skills that tell Codex how to handle each kind of information. The job history belongs with the job. A follow up that needs action belongs in the task system. The daily note gives me a shorter account of what happened.

I use Markdown for the readable notes and JSON with Python scripts for things like task records, schedules, and the lists built from them. I have been developing the instructions and supporting tools around how I actually use the vault, so I can give an update in ordinary language without manually sorting every part of it first.

## Overview

I use Obsidian as a working record of both my business and parts of my personal life. Codex helps me maintain that information through an automation workflow that I can start with a prompt.

The input does not have to arrive already sorted into the structure of the vault. I can describe what happened, what changed, and what I need done. The workflow separates those subjects, finds the appropriate existing records, and carries the information into the files and folders that own it.

This is a more focused account of the intake process behind my broader [Obsidian skills and business automation system](../workflows/PUB-0008-obsidian-business-automation.md).

## Role

I define what I want recorded or changed and develop the reusable instructions around those needs. Codex interprets the request, reads the relevant context, and follows the workflows for the records involved.

The system has different rules for a job update, a contact, a task, a schedule change, and a personal note. Defining those distinctions is part of my work in building it.

## Scope Of Work

Business information makes up the largest part of the system. I use it for job creation, ongoing job history, organizations, contacts, decisions, and information from phone calls, texts, and emails.

The same vault also holds personal events, health and wellness notes, and occasional food tracking. Those entries can remain in their appropriate personal or daily-note context. They do not need to become business contacts, project records, or tasks simply because they appeared in the same conversation.

## Key Actions

### Start with the prompt

The on-demand workflow begins when I give Codex an instruction, including through voice dictation. A mixed update can contain facts to retain, something already completed, a future obligation, an uncertainty, and an action I want performed.

The intake instructions separate those items while preserving their meaning and sequence. Cleaning up dictated wording should not change a decision or turn a tentative statement into a commitment.

### Resolve the existing context

Before creating a new record, the workflow searches for the job, organization, person, or project already represented in the vault. Names, aliases, linked records, and surrounding context help establish the match.

Job creation follows an explicit request. An update to an existing job should extend its history rather than produce another job folder. When the identity is genuinely ambiguous, the uncertainty remains visible instead of being resolved by guessing.

### Route detail to its owner

The intake router passes each part of the request to the relevant specialized workflow. Job history stays with the job, organization and relationship information belongs in the appropriate entity record, and durable research goes into the knowledge area it concerns.

An actionable follow up goes through the task system. Dated work goes through scheduling. An observation or an idea does not automatically become a new obligation.

### Update the daily note last

Detailed records are updated first. Task and schedule records follow where needed, and the daily note receives a concise account afterward.

This keeps the daily note useful as an index of the day while the supporting history accumulates with the work it describes. Later updates about the same job can join the existing daily entry instead of creating repeated fragments.

## Important Features

### Readable notes and structured state

Markdown holds the human-readable notes and links. JSON supplies structured records where identifiers, status, dates, and consistent updates matter, including tasks, schedules, and supporting entity information.

Python helpers maintain those structured records, rebuild lists and indexes, and validate managed sections in related notes. For example, a task list or a schedule block can reflect the underlying record rather than becoming a separate list to maintain by hand.

### Reusable instructions

Skills are written instructions that tell Codex which source is authoritative, what information to preserve, what checks to perform, and where the result belongs. The intake router coordinates those skills rather than repeating every rule itself.

The AI handles interpretation and context. Supporting code handles defined operations such as numbering, record updates, validation, and rebuilding views. These parts work together around the files in the vault.

### Connections beyond the vault

The broader system also includes Gmail intake and Google Calendar synchronization. Gmail intake tracks processed message boundaries so later passes can identify new correspondence without repeatedly copying the same history. Dated scheduler changes pass through a calendar synchronization workflow that verifies the external result.

These are distinct connections with their own procedures. Keeping information from a phone call or text in my notes does not depend on an automatic feed from the phone.

## Constraints And Decisions

The automation described here is initiated by my request. Scheduled workflows also exist, but they are separate triggers within the broader system.

Completion has to retain its meaning. Finishing a task or a phase of construction does not automatically mean the entire job is complete. Similarly, a personal observation can be recorded without creating a task or scheduled event.

## Deliverables

A completed intake can produce updated job or organization notes, personal entries, task or schedule records, and a concise daily account. The exact outputs depend on what the prompt asks for.

Prompt-memory helpers also retain the request and a short task summary. They use duplicate checks, file locks, and a pending queue when another writer prevents a safe direct update. That provides a separate continuity record across conversations.

## Outcome

I can capture an update in ordinary language and have its different parts organized into the records I use afterward. Business history, personal notes, and actionable work remain connected without requiring every detail to live in the daily note or the original chat.

The workflow continues to develop through use. Improvements to routing instructions, validation, and supporting scripts become part of the reusable system.

## Tools And Methods

Obsidian, Codex, voice dictation, Markdown links, reusable skills, JSON records, Python command-line helpers, generated indexes and managed note sections, Gmail intake, Google Calendar synchronization, and local prompt-memory records.

## Evidence And Limitations

This account describes the implemented intake rules and supporting tools alongside my personal use of the vault. The information available in a particular run depends on the context I supply and the records or connected services available to that workflow. Private health details, correspondence, and individual job information remain outside this public account.
