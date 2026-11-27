# Worked Example: A Stair Flight With an Upper Landing

This walkthrough describes a fictional practice job. It introduces the workflow without copying a customer's measurements, job information, or manufacturing instructions.

## Establish the Starting Condition

Begin with one stair flight and an upper landing. Use a traditional drawing and give the project a clearly fictional name, such as **Demonstration entrance**.

Before changing the design, identify the step count, individual run and rise, upper landing length, post arrangement, and intended rail style. The measurements for a downloadable sample will be selected and reviewed separately; the application's starting values should not be mistaken for a measured example.

## Build the First Drawing

Enter the stair measurements and upper landing length. Review the total rise and run, then inspect the relationship between the stair rail, landing rail, and shared post.

Save the complete project as JSON. Export an SVG or PNG sheet to establish the first review version. Keep the editable file and drawing output distinct.

## Change One Input

Increase the fictional landing length while retaining the other chosen settings. Compare the updated landing geometry, post arrangement, infill, and dependent dimensions with the first drawing.

This illustrates the application's central purpose: the operator changes a design input and the shared model recalculates the relationships affected by it.

Save the revised project and export a second review sheet. Reopen the saved project to confirm that the intended input change was retained.

## Add a Pitched-Landing Variation

For a second exercise, enable **Out of level** on the upper landing. Specify a total height difference and identify whether its outside edge is higher or lower than the stair-side reference.

Review the top-rail and bottom-rail follow controls independently. Compare the elevation when a rail follows the landing with the version where it remains level at its reference height.

This step demonstrates why entering a pitch and choosing which rails follow it are separate decisions.

## Compare the Deliverables

Open the exported DXF in suitable CAD software and compare it with the generated sheet. Inspect the difference between the annotated and geometry-only views.

Review the component information alongside the drawing. Confirm which lengths describe generated geometry and which fabrication decisions still need to be made for the intended assembly.

The completed exercise should leave an editable project and review outputs that can be traced to the same design revision. A later revision should remain distinguishable from the first, rather than relying on an image to reconstruct the inputs.

[Introduction](introduction.md) · [Getting started](getting-started.md) · [Field workflow](field-to-drawing-workflow.md)
