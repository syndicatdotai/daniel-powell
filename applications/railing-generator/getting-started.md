# Getting Started With Railing Generator

This guide introduces the browser workflow. Begin with a fictional practice job and a traditional drawing before trying a complex configuration.

## 1. Start With the Layout You Want to Describe

Identify the parts of the railing before entering measurements: the stair flight, any upper or lower landing, the intended post arrangement, and the rail and infill style.

The initial values in the application are defaults. Replace the relevant values with the measurements for your example, and keep a record of anything you have intentionally left at its default.

Use **New drawing** and choose **Traditional drawing** for an ordinary layout. **Connected landings** starts a more advanced, experimental workflow with linked elevations.

## 2. Enter the Stair Measurements

Use **Number of steps**, **Step run**, and **Step rise** to describe the stair flight. The current drawing inputs use inches. Read the field labels carefully so per-step measurements are not confused with the overall flight dimensions.

The application also displays total stair run and rise controls. For a first drawing, work with the individual step inputs and check the totals against the intended flight before exploring held totals or more involved adjustments.

If the real stair is irregular, do not represent it as uniform simply to fit the first example. Review whether the supported configuration describes the condition before using its output for a job.

## 3. Add the Landings That Are Actually Present

Configure the upper and lower landings as required. A second flight can be added through **Bottom landing**, then **Lower stairs**; the original bottom landing becomes the intermediate landing, and the lower flight has its own measurements.

For a pitched landing, **Out of level** means the total vertical difference across that landing, not a rate per unit of length. Select whether the outside edge is higher or lower than the stair-side reference.

The controls for following the landing surface are separate for the top and bottom rails. Check which are enabled and inspect the resulting elevation rather than assuming that both rails will follow the pitch.

## 4. Review Posts, Rails, and Infill

Select the intended configuration and review the generated post positions, rail heights, offsets, and infill. Pay attention to the reference used by an offset: a post center, post face, or stair reference is not interchangeable with another.

Automatic layout is a calculation based on the current settings. Manual choices should be checked against the dimensions and the actual job requirements.

The 2D sheet is the main reference for dimensions and notes. Where available, the 3D view helps explain spatial relationships; it does not replace the dimensioned drawing.

## 5. Add Job Information and Commentary

Job name, shop information, address, date, and title capitalization are shared at project level. Use fictional information in a demonstration.

Drawing commentary belongs to the individual drawing. For a note tied to a labeled post, start with the actual marker, such as `[H]`, followed by the note. Match the label shown on that drawing rather than copying a marker from an unrelated example.

Notes communicate information. They do not independently add brackets, move posts, or change the geometry.

## 6. Save the Editable Project

Use **Save project** to retain the editable design as JSON. **Save project as** provides a separate file destination. Depending on browser support, saving uses a file picker or a download.

To continue later, use **Open project**. If an external workflow revises the same saved project, **Reload project data** is a deliberate way to bring the revised file back into the viewer. It is not automatic synchronization.

Keep browser recovery and saved files distinct. Changes in a tab do not necessarily change a previously downloaded JSON file, and clearing browser storage can remove recovered workspace data.

Saved projects should be reopened in a compatible application build. Older builds may reject newer project formats; retain a copy before changing versions.

## 7. Export and Check the Result

Open **Export drawing**, select the required formats, and press **Export**. DXF is selected initially. Multiple formats download separately unless **Download as ZIP** is selected.

- **DXF:** CAD continuation, with annotated and clean geometry views.
- **SVG:** vector drawing sheet.
- **PNG:** image for review or sharing; the browser also offers print-quality output.
- **Editable drawing JSON:** a portable project containing the selected drawing, or the source drawings and connection for a connected sheet.

Saving the entire project remains separate from exporting one drawing. Preserve the full project when other drawings or settings need to remain together.

Check the exported file as well as the browser preview. Confirm the job information, measured dimensions, post references, notes, and overall sheet legibility before treating the output as a deliverable.

[Introduction](introduction.md) · [Field workflow](field-to-drawing-workflow.md) · [Worked example](example-project.md)
