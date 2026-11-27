# A Two-Hour Construction Application: Concrete Quantities and Visualization Built from a Phone

**Public project ID:** PUB-0127

A client needed to determine how much concrete to order for a walkway surrounding an unusually shaped swimming pool. In approximately two hours, I used ChatGPT from my phone to develop a small browser application that calculated the estimated quantity and produced a visual explanation to accompany it.

The application served a specific construction question. Built with HTML, JavaScript, and CSS, it combined geometry, concrete-volume calculations, and a presentation that could be captured in screenshots and sent directly to the client.

This was an early experiment in **ephemeral construction software**: a purpose-built application that delivers value for a particular situation, even if it is never used again.

## An Irregular Shape with Limited Measurements

The pool consisted of three adjoining circular sections of different diameters, arranged into an approximate L shape. Curved transitions—fillets—connected the circular sections. The surrounding concrete walkway followed the pool’s outline at an offset, creating a corresponding outer perimeter.

That geometry made the task more involved than calculating a rectangular slab or a simple circular patio. The adjoining shapes and their transitions affected the area of the surrounding concrete.

The information supplied by the client included the diameter of each circular section, the desired walkway width, and the concrete thickness. It did not include the dimensions of the fillets connecting the circles.

Those missing dimensions mattered. The supplied measurements supported a modeled estimate, but they did not fully define the exact perimeter. Any representation of the connecting curves necessarily involved assumptions. That distinction belongs alongside the calculation: the application could estimate the concrete required for the modeled shape, while the exact quantity depended on how closely that geometry represented the intended construction.

## Why Use AI for This Task?

AutoCAD was an available route. The shape could have been drawn, its geometry resolved, and the resulting area used to calculate concrete volume.

For this assignment, however, the desired output included more than a quantity. The client also needed a clear visual representation and light documentation explaining the information.

ChatGPT provided a way to develop those elements together. The calculation and the accompanying illustration could be handled within a small browser-based tool, without building a larger drafting package around the request.

The objective was straightforward: turn a limited set of measurements into useful estimating information and make the result easy to communicate.

## Building the Application from a Phone

The work took place from my couch, using ChatGPT on my phone.

Through that conversation, the pool configuration and walkway requirements became a small application running in the browser. HTML provided the document structure, CSS controlled the presentation, and JavaScript handled the calculations and visualization.

The application modeled the pool and surrounding walkway, calculated the concrete area, and used the specified thickness to estimate volume in cubic yards—the quantity relevant to ordering concrete for the pour.

The visualization gave the calculation a visible reference. Rather than sending an isolated number, the output showed the shape being represented and the surrounding concrete being estimated.

Screenshots captured the information for delivery to the client. The client received the useful output without needing to install software or work through the application’s implementation.

From the initial problem to the client-facing material, the process took approximately two hours.

## Software Sized to the Assignment

The application’s value came from its fit to the immediate problem.

There was no requirement to develop a general-purpose concrete estimating platform, create customer accounts, or establish an ongoing software service. The task called for a particular calculation, a visual explanation, and information that could be shared.

Once those outputs were delivered, the application had fulfilled its purpose. Future reuse would have been a benefit, but it was not necessary to justify creating it.

That changes the economics of small software tools. A construction problem can be too specific to justify commissioning conventional software, yet still benefit from a custom interface and calculation. AI-assisted development makes it practical to consider building that tool within the time available for the assignment itself.

## Construction Knowledge Defines the Problem

The construction experience remained central to the work.

The useful questions were about the geometry being measured, the width and thickness of the concrete, the relationship between the pool and walkway, and the information needed for an order. Recognizing the missing fillet dimensions was also part of understanding the limits of the available measurements.

AI helped translate that problem into executable software and a visual deliverable. The application expressed the construction problem in a form that could calculate and communicate an answer.

The distinction is especially relevant when inputs are incomplete. A polished visualization does not supply measurements that were never provided. The estimate remains connected to the geometry and assumptions used to produce it.

## A Practical Example of Ephemeral Applications

This project demonstrated a useful role for small, temporary applications in construction.

Some assignments need the capabilities of software without needing a permanent software product. A custom calculator, diagram, or browser-based explanation can address a narrow question and produce a durable deliverable, even when the tool itself has a short working life.

In this case, a phone, ChatGPT, and approximately two hours were enough to create a concrete-estimating application and supporting visuals for a client.

The lasting result was the information delivered: a modeled concrete quantity and a clearer explanation of the proposed work.
