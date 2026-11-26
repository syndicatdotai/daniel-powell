# Automating site context at project kickoff with Codex

## LinkedIn Summary

I have been building a small but useful automation into my project kickoff workflow.

When I start a new Connecticut project, Codex uses the address and the existing project context to gather location references automatically. It checks the site, captures a clean map view, pulls the publicly available CT ECO 2023 aerial imagery, and can add a topographic view derived from the same year's LiDAR data.

That means the project starts with visual context already attached: the building, surrounding access, neighboring conditions, terrain, and the wider site relationship. I am not waiting until later to remember to go find it.

The interesting part is not just that AI can retrieve an image. The value comes from connecting the image to the right project, saving it in the right place, naming it consistently, and carrying the context forward into the notes and future work.

For Connecticut construction and property research, the state GIS resources are an excellent foundation. Codex makes them part of the workflow instead of another tab I have to remember to open.

#ArtificialIntelligence #Codex #GIS #LiDAR #ConstructionTechnology #WorkflowAutomation

## Overview

This record describes a project-kickoff workflow for Connecticut construction and property research. When a new project has an address and enough working context to identify the site, Codex can coordinate the location-imagery steps and prepare visual references for the project record.

The Connecticut source combines a clean map reference, publicly available CT ECO 2023 aerial imagery, and an optional topographic reference derived from 2023 LiDAR elevation data. The goal is to make site context available at the beginning of the work instead of leaving it as a later manual task.

## Role

Daniel designed and maintains the workflow around his construction and project-documentation needs. He defines the source requirements, decides what context is useful, reviews the resulting references, and controls how the information is used in the project.

Codex acts as the natural-language orchestration and execution layer. It uses the project address and available context, coordinates the supported capture and retrieval steps, and prepares the resulting references for review.

## Scope Of Work

The workflow covers initial site-context preparation for Connecticut projects. It can check the site, capture a standard map view, retrieve the relevant 2023 aerial reference, and add a topographic view when terrain or grade context matters.

The output is intended to support early construction planning, property research, access review, surrounding-site understanding, and future project conversations. It is not a boundary, title, engineering, or field-survey workflow.

## Key Actions

- Read the project address and existing context from the project record.
- Check the site before capture so the framing fits a residential, commercial, or larger property.
- Capture a clean map reference through browser automation.
- Retrieve the official CT ECO 2023 aerial source for Connecticut.
- Generate or retrieve a clean topographic reference from CT ECO's 2023 LiDAR-derived elevation data when needed.
- Save the resulting references with consistent, searchable naming and attach them to the project record.
- Avoid repeating captures when the expected location references already exist.

## Important Features

- Source-aware imagery: the Connecticut path uses a known state GIS source rather than an unspecified map screenshot.
- Multiple views: map, aerial, and topographic context answer different early-project questions.
- Context-aware framing: larger sites can receive wider surrounding context so access, adjacent roads, parking, and neighboring conditions remain visible.
- Project linkage: the files are connected to the project record instead of remaining loose downloads.
- Repeatability: the same intake pattern can be reused as new projects are created.
- Storage discipline: photo-like aerial references are compressed for practical vault storage, while source details remain available in the supporting record.

## Constraints And Decisions

- The statewide Connecticut aerial and LiDAR products referenced here are from 2023; they are not live imagery.
- Public availability does not automatically grant permission to redistribute raw imagery. Source attribution and reuse terms should be checked for client-facing or commercial work.
- LiDAR-derived topography and aerial imagery provide useful context but do not replace a survey, boundary research, engineering analysis, field verification, or professional judgment.
- Leaf-off aerial imagery can reveal ground and structure relationships clearly while representing vegetation differently from a summer capture.
- The workflow distinguishes the verified Connecticut source from non-Connecticut fallbacks; it does not describe another state's fallback imagery as confirmed 2023 data.
- Automation prepares the starting context, but Daniel reviews what is attached and how it is used.

## Deliverables

- A clean map reference centered on the project site.
- A Connecticut aerial reference from the 2023 CT ECO source.
- An optional LiDAR-derived topographic reference using shaded relief and contour information.
- Consistently named location-reference files connected to the project record.
- A concise record entry that makes the source and purpose of the imagery understandable later.

## Outcome

New Connecticut projects can begin with useful visual context already attached to the working record. The workflow reduces the chance that the map, aerial, and terrain references will be forgotten during a fast project intake, and it makes the initial site relationship easier to understand before later research, planning, or field work.

The larger lesson is that the value is not only in retrieving an image. The useful system connects the source to the right project, applies consistent handling, and carries the context forward into the rest of the work.

## Tools And Methods

The workflow uses Codex for orchestration, browser automation for map capture, the official CT ECO 2023 aerial image service for Connecticut imagery, and CT ECO LiDAR-derived elevation data for topographic context. Project records are maintained in Markdown, with image references attached to the relevant project context. Photo-like aerial outputs use compressed JPEG derivatives for practical storage.

Source references:

- CT ECO 2023 Aerial Imagery and Elevation: https://maps.cteco.uconn.edu/data/flight2023/
- CT ECO 2023 Ortho Image Service: https://cteco.uconn.edu/ctraster/rest/services/images/Ortho_2023/ImageServer

## Evidence And Limitations

The workflow details are grounded in the Job Location Imagery automation note, the Connecticut aerial-imagery research note, the local job-location-imagery skill, and Daniel's direct description of the project-kickoff behavior in the current Codex conversation.

The public record describes the intended and documented workflow, not a claim that every project is processed without review or that every state has the same source quality. The imagery is historical site context, not live observation. CT ECO's aerial and LiDAR-derived products should be paired with current field information and appropriate professional sources before conclusions are made about boundaries, grade, drainage, structures, or legal conditions.
