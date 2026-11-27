# Railing Generator: From Field Measurements to Shop Drawings

Railing Generator is a drawing application developed around field measurement and shop-drawing work for a railing manufacturer. It converts measured stair and landing conditions into editable railing layouts, dimensioned sheets, CAD geometry, and component information.

The application grew out of drawing these jobs manually in AutoCAD. Repeated decisions about post locations, rail heights, spindle spacing, landing transitions, and drawing annotations became relationships in the software. When an input changes, the generator recalculates the dependent geometry and dimensions through a shared drawing model.

Development continues alongside production work. Supported configurations can be generated quickly; unfamiliar conditions still require review, a new application capability, or additional work in AutoCAD.

## Explore the Application

The public-access draft is organized into three guides:

- [Getting started](getting-started.md): understand the workspace, create a simple drawing, save the editable project, and export the result.
- [From field measurements to delivery](field-to-drawing-workflow.md): how field observations, voice instructions, drawing review, and production handoff connect in my work.
- [A worked example](example-project.md): follow a fictional stair-and-landing job through a change and compare the resulting outputs.

[Open Railing Generator](https://railing-generator.vercel.app/)

These guides cover the drawing application. Access to my Codex environment, client records, and manufacturer CRM is not included.

## Understand the Three Parts of the Workflow

### The project is the editable design record

A project holds the job information and its drawings. Saving the project as JSON preserves the measurements, configuration choices, notes, and other authored settings needed to continue working.

Browser recovery helps retain a workspace, but it is separate from saving a portable project file. A drawing image or CAD export is also separate from the complete editable project.

### The drawing shows the selected configuration

A drawing brings together stair measurements, landings, posts, rails, infill, dimensions, and commentary. The application supports stair and landing layouts, including intermediate landings and lower flights. Landing surfaces can be described as out of level so supported rail configurations can follow the measured condition.

More involved connected-landing sheets are an experimental workflow. They should be explored after the ordinary single-drawing process is understood.

### Exports serve different purposes

DXF carries the drawing into CAD software such as AutoCAD. SVG preserves a vector sheet. PNG provides an image for review or sharing. The browser also offers an editable drawing JSON export, while saving the entire project remains a separate action.

Component information describes the generated parts. It must be read alongside the drawing and the intended fabrication method; drawn component lengths are not automatically stock-order lengths or complete fabrication instructions.

## How Voice Input Fits In

In my workflow, I dictate measurements and instructions to Codex. Codex prepares an editable project and runs the application. The railing geometry is calculated by Railing Generator using the same model that supports browser editing and exports.

Opening the application does not enable a built-in microphone assistant or connect someone else's browser to my production workflow. Voice interpretation, file preparation, review, and authorized delivery are separate steps around the drawing engine.

## Rules, Defaults, and Review

The drawing model contains spacing and height constraints used for the railing work it supports. These guide the generated layout, while the operator remains responsible for reviewing the configuration, field measurements, applicable requirements, and fabrication details for the job.

Application defaults are starting values. They are not measurements of the site. A generated sheet is ready for review when its inputs and assumptions are understood, not simply because it looks complete.

[Development commentary](overview.md)
