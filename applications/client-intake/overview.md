# Building an Architectural Client Intake Application

## LinkedIn Summary

I built software for my architectural clients to work through a detailed design program before getting too far into the drawings.

The intake covers the spaces they want, but it also asks how they actually use their home. Do they cook regularly or mostly prepare quick meals? Do they entertain in the kitchen? Do they work from home and need a private office or a shared workspace? Are there children, pets, hobbies, or outdoor activities that need to be accounted for?

There are questions about things like a workshop, pantry, guest suite, mudroom, or outdoor living area. Clients can select what applies and add their own comments. Other sections cover architectural styles, materials, finishes, site conditions, accessibility, energy goals, budget, and scheduling.

I built in progress tracking and saved responses so the intake can be worked through over time. The answers stay organized under the individual client.

From there, the AI summary workflow brings the completed answers and any additional notes I select into a written design brief. I can generate a short overview or a more detailed version while still referring back to the original responses.

The application also includes a visualization workflow that develops an image prompt from the summary. I can edit that prompt, choose a visual style, and generate an exterior concept image to discuss with the client alongside the written program.

## Overview

I built an architectural client intake application to collect the information that shapes a design program: what the client wants to build, which spaces they need, how they intend to use them, and the conditions the project needs to work within.

The application brings a detailed questionnaire, saved client records, written summaries, and concept visualization into the same workflow. It gives the early design discussion a structured record that can be reviewed as a whole or revisited question by question.

## Role

I developed the software around the information I wanted to collect from my architectural clients. I organized the intake topics, defined the questions and response options, and connected the collected information to AI summaries and an exterior visualization workflow.

The questionnaire reflects both the physical requirements of a project and the client's day-to-day use of the building.

## Scope Of Work

The intake covers project basics, site conditions, required spaces, household members, aesthetic preferences, sustainability, budget, scheduling, regulatory considerations, and additional client priorities.

It includes selectable responses for common requirements and written fields for details that do not fit a predefined choice. Clients can record their preferences without having to describe the entire project in one long response.

## Key Actions

- Organized the intake into sections covering the major parts of the design program.
- Added specific questions about room requirements, household activities, work, hobbies, and outdoor use.
- Included site, accessibility, material, energy, budget, and schedule considerations.
- Built client records with intake progress and saved responses.
- Connected completed answers and selected supplementary notes to concise and detailed AI summaries.
- Included Markdown and plain text summary outputs.
- Connected the written summary to an editable image prompt and exterior concept visualization workflow.

## Important Features

### Rooms and the activities they support

The program section includes spaces such as a mudroom, pantry, home office, guest suite, workshop, studio, laundry room, and outdoor living area.

Other questions add context to those selections. The cooking section asks whether the client enjoys cooking, bakes frequently, entertains in the kitchen, or mainly prepares quick meals. The work section asks about working from home and the type of workspace needed, including a private office or shared workspace.

Hobby questions cover uses such as woodworking, art, music, fitness, and reading. Outdoor questions include gardening, outdoor cooking, and other activities. Household questions capture children, pets, and any particular requirements associated with them.

These answers help describe what the requested spaces are expected to accommodate.

### Design preferences and project conditions

The intake collects preferred architectural styles, materials, finishes, and roofing preferences. It also includes sustainability and energy goals.

Site questions address existing structures, utilities, topography, and known constraints. Separate sections gather schedule expectations, budget information, accessibility requirements, and known zoning or permitting considerations.

Collecting those topics alongside the room list keeps the desired design and the practical project conditions in the same record.

### Saved progress and individual responses

The application includes client records, progress tracking, and saved intake responses. The questionnaire can be worked through over time and revisited as additional information becomes available.

The individual answers remain available by section. A written summary can be read alongside the underlying responses when a particular preference or requirement needs closer review.

### AI summaries with selected context

The summary workflow collects answered questions, groups them by their intake section, and includes supplementary notes that I select for AI review.

There are two summary formats: a compact overview and a detailed version. The implementation supports Markdown and plain text outputs and saves the summaries with the client record.

For example, the underlying intake can contain both a home office selection and more specific answers about working habits. The summary workflow brings those responses together in one brief for review.

### An editable path to concept imagery

The visualization workflow uses the written summary to develop a prompt describing the proposed exterior. The prompt remains editable before image generation, and the application includes visual style choices such as a sketch or a more realistic rendering.

This creates a visual interpretation of the collected preferences that can be discussed alongside the written program. The intake answers and summary remain available when reviewing how closely the image reflects the client's requested direction.

## Constraints And Decisions

I used a combination of structured choices and written comments. The choices make common requirements straightforward to record, while the comments provide room for unusual requests and additional explanation.

The workflow also keeps the original answers, summaries, and generated imagery as separate records. Each serves a different purpose: the answers retain the client input, the summary organizes it for review, and the image provides an early visual concept.

The generated exterior is a discussion image. Detailed design decisions remain part of developing the drawings from the program.

## Deliverables

- An architectural intake application with individual client records.
- A detailed questionnaire covering spaces, lifestyle, preferences, and project conditions.
- Progress tracking and saved responses.
- Concise and detailed summary generation using questionnaire answers and selected notes.
- Markdown and plain text summary outputs.
- An editable image prompt and exterior concept visualization workflow.

## Outcome

I built a workflow that connects detailed client input to a written design brief and an exterior concept image.

The collected information can be reviewed at different levels: individual answers, a short overview, a detailed summary, or a visual interpretation. That gives me several ways to work through the same design program with a client.

## Tools And Methods

An earlier version used browser-based JavaScript. A later version used Next.js, React, and TypeScript, with Supabase for stored records and integrations for AI summaries and image generation.

The form structure defined the sections, question types, and response options. The summary workflow assembled the completed responses and selected notes, while the visualization workflow handled prompt development, editing, image generation, and storage.

## Evidence And Limitations

This account is grounded in my description of the project and the retained application source. The source supports the questionnaire structure, summary workflow, and visualization integration described here. Current hosted availability and live integrations were not retested for this article.
