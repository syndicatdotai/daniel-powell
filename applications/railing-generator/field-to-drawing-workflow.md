# From Field Measurements to a Reviewed Drawing

Railing Generator is one part of a larger workflow. The site visit establishes the conditions; the project file records the design inputs; the application calculates the drawing; and review connects that output to the job being delivered.

## Capture the Condition Before Choosing the Configuration

On site, I record stair run and rise, landing lengths, and any landing that is out of level. The field description also identifies the arrangement of flights and landings, the desired rail style, and comments that need to appear on the drawing.

The reference behind a measurement matters. A landing's total vertical difference is different from its pitch expressed as a rate. A dimension to the face of a post is different from one to its center. Those distinctions need to be resolved before the drawing is treated as a representation of the site.

## Use Voice to Prepare the Inputs

I send Codex a voice memo describing the measured condition and the configuration I want. Codex converts that instruction into an editable project and invokes the supported application workflow.

That division of responsibility is important. Codex interprets the instruction; the application's shared geometry model performs the railing calculations. The result is not a drawing guessed from a verbal description.

Unspecified settings remain application defaults until they are deliberately chosen or replaced. Ambiguous measurements need clarification. Commentary is retained as commentary, rather than being silently converted into an extra piece of railing.

## Generate From a Known Project Revision

The saved project is the handoff between browser work and command-driven output. The local command-line workflow can inspect, validate, and export a project file without operating the drawing interface.

A URL to the application is not the current job data. An unsaved browser drawing is also not the same thing as the last saved JSON file. Before exporting, the workflow identifies which project revision is being used.

The supported command-line operations are explicit. They do not provide unrestricted natural-language editing of every control or automatic access to an open browser tab. File revisions are deliberately reopened or reloaded when continuing in the viewer.

## Review the Drawing Against the Site

The drawing is reviewed for stair and landing relationships, post positions, offsets, rail heights, infill, and the notes needed by the shop. Sloped landings and transitions deserve particular attention because the choices affect several dimensions together.

Document review also includes the presentation: dimension labels should be readable, commentary should remain inside the frame, and numbered summaries should stay clear of the geometry. Viewing the whole sheet at phone size tests a different aspect of usability from zooming into a detail.

The displayed stair-reference angles describe the geometry. They should not be read automatically as compound miters, half-angle cuts, or complete saw settings. Fabrication decisions still depend on the actual connection and manufacturing method.

## Keep the Deliverables Together

The editable project preserves the choices behind the drawing. DXF supports AutoCAD continuation; vector and image sheets support review and sharing; component information supports the shop's interpretation of the generated geometry.

PDF preparation and uploading files to the manufacturer's CRM are further steps in my authorized production workflow. The browser drawing application does not, by itself, connect a visitor to those services.

## Decide Whether a New Condition Belongs in the Software

When a job presents an unsupported detail, the next decision is whether to draw it manually or extend the application. A condition likely to recur can justify development time: define its adjustable inputs, work through placement and dimensioning, and retain the capability for later jobs.

A one-off detail can still be completed in AutoCAD. The goal is to make recurring work reusable while preserving the ability to handle a project that needs individual treatment.

[Introduction](introduction.md) · [Getting started](getting-started.md) · [Worked example](example-project.md)
