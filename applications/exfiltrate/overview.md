# Developing Exfiltrate: Remote Drones, Salvage, and Interacting Station Systems

*Updated November 26, 2026.*

## Play Exfiltrate

[Open the live browser game](https://exfiltrate-ashen.vercel.app/)

Exfiltrate is a browser-based game in active development, with a public production build hosted on Vercel. The interface is designed around mobile play, with touch controls for movement, aiming, tools, and instrument views.

## Project Summary

I'm developing Exfiltrate, a game about remotely operating a drone inside dangerous derelict installations, recovering salvage, and returning it to a support station called the Host.

The original idea was closer to entering a maze and retrieving an important object. It developed into a broader exploration and recovery game: discovering an unfamiliar station, assessing what is worth recovering, and deciding how much risk to accept before returning.

<a href="https://github.com/syndicatdotai/daniel-powell/releases/download/exfiltrate-screenshots-2026-11-26/exfiltrate-overview.jpg"><img src="https://github.com/syndicatdotai/daniel-powell/releases/download/exfiltrate-screenshots-2026-11-26/exfiltrate-overview.jpg" alt="Four Exfiltrate screenshots showing the drone camera, Host fabrication, Host operations, and a tethered power cell." width="480"></a>

*Four views from the live build: drone camera, Host fabrication, Host operations, and power cell recovery. Select the image to view it full size.*

The project combines physical cargo handling, equipment, fabrication, power, communications, and sensing. Its central design problem is making those systems work together so that a recovery expedition involves more than following a route to an objective.

Development also includes the architecture, authoring tools, diagnostics, and documentation needed to keep expanding the game with AI-assisted implementation.

## Operating Through a Drone

The player experiences the station through machinery. A camera, map, operation console, battery display, and equipment controls form the working interface between the operator and the environment.

Movement and observation have separate controls. The live interface provides a movement pad and a look pad, allowing the camera and light to be aimed independently of travel. Light, scanning, clamping, and contextual interaction are available alongside the instrument display. Keyboard movement is also supported.

The controls expose practical tradeoffs. Turbo provides faster movement at greater movement-power cost. Quiet drive reduces speed and emitted sound. A scan gathers information, while battery use makes continued operation a resource decision.

This remote perspective shapes the game. The operator has to act on the information the drone acquires, manage its equipment, and account for the station's condition. The interface is part of that experience: it presents observations and operating feedback rather than an unrestricted view of everything in the simulation.

## Salvage as a Physical Problem

Recovering equipment requires a model for how objects occupy and move through the station.

The towing implementation accounts for the relationship between load mass, towing force, and the mover's mass. Objects have physical footprints, and clearance through a doorway depends on their actual shape. Contact, resistance, and rotation matter when moving cargo through constrained spaces.

That work turns salvage into a handling problem as well as a collection system. A useful object can change how the drone moves and which route is practical. The decision to recover something therefore connects exploration, equipment, geometry, and the return journey.

The same object also needs a consistent identity as it changes location. A physical item in the world, an item in Host storage, and an installed module are different states of an item. Transfers check the destination before committing the change, with rules that prevent an item from existing in multiple places at once.

## The Host: Storage, Fabrication, and Preparation

The Host provides a support point for the expedition. Its player interface includes fabrication, inventory, and maintenance sections, with resource and storage information visible together.

Fabrication connects resources to usable equipment. A blueprint identifies the output, Scrap cost, and production time. Storage reservations account for the space the completed item will need, so fabrication and inventory capacity remain connected.

The live production review included a complete Basic Power Cell fabrication cycle. Starting fabrication deducted two Scrap; the completed cell then appeared in Host inventory and increased the stored-item count. Inventory offered actions to eject the cell into the world or intentionally scrap it.

This provides a concrete connection between the game's economy and its physical environment. Equipment can be produced, stored, and returned to the world as cargo, rather than remaining only an abstract menu entry.

Host development also includes a separate upgrade backend. Its implemented foundation handles capability definitions, prerequisites, resource transactions, and mission-save state. The player-facing upgrade interface and account or campaign progression remain future work; they are separate from the fabrication and inventory screens available in the public build.

## A Station Built From Interacting Systems

Exfiltrate's environment extends beyond walls and obstacles. Development includes electrical distribution, breakers, generators, lighting, communications, sound, smoke, and thermal behavior.

These systems share the station's geometry while retaining their own rules. A wall can matter to movement, an observation path, and an environmental process without those concerns becoming the same calculation.

Equipment is assembled from reusable capabilities. An object can participate in physical handling, charging, control, or other systems according to its definition. New combinations of existing capabilities can then be authored as content; adding a genuinely new behavior requires implementation in the system that owns it.

That distinction is central to the project's direction. Expanding the equipment and station vocabulary should not require a growing collection of exceptions for every named object and tool pairing.

## Information, Detection, and Player Knowledge

The simulation distinguishes what exists from what an observer has detected and what the player remembers.

A hidden object can exist without appearing on the map. Information must pass through an appropriate sensing system before it becomes available to the operator. Remembered observations remain separate from current sensing, so a display does not automatically receive the live position of an object simply because it was seen earlier.

The game also separates visual, acoustic, thermal, and electromagnetic detection signatures. Those channels describe different characteristics and use their own propagation and acquisition rules. A signature value alone does not establish that an observer has detected the drone.

Screen readability is another distinct concern. Adjusting the interface so a person can see the controlled drone should not silently change the drone's detectability or reveal hidden information. This separation keeps presentation decisions from changing the simulation's rules.

## Developing the Application With AI

My role includes the game concept, mechanics, interface direction, and decisions about how the systems should interact. AI-assisted development supports implementation, testing, refactoring, documentation, and investigation of runtime behavior.

As the application grew, effective AI work required more than describing the next feature. The project needed a reliable way to identify the relevant system, understand its responsibilities, and find the tests and dependencies affected by a change.

The repository therefore includes a context entry point, development thesis, project atlas, subsystem documentation, and source and test maps. These give a new coding session a bounded starting point. Inventory work follows ownership and persistence rules; sensing work follows acquisition, memory, and presentation boundaries.

The architecture separates authored definitions, derived geometry and indexes, runtime state, player knowledge, and presentation. Moving an object during play must not rewrite its original placement definition. Developer inspection must not leak hidden world information into ordinary player displays.

The project also includes a world editor, content-authoring tools, a workbench, runtime inspection, and developer controls. JSON diagnostic snapshots provide concrete configuration and session information for an implementation discussion. Retained development records preserve decisions, experiments, and replaced approaches so later work can build on what has already been learned.

## Browser Performance and Release Discipline

The application uses JavaScript, HTML, and CSS, with Canvas 2D, WebGL, and Web Audio supporting its presentation and effects. Mobile use influences both the interface and the amount of work performed by the simulation and renderer.

Performance development has addressed moving lights, repeated world queries, environmental updates, scheduling, and diagnostic overhead. A recurring approach is to retain derived results and update them when their inputs change, allowing multiple systems to reuse them.

Pause and resume behavior also matters. A browser game must account for interruptions and returning to the page alongside continuous play.

Development integration is separated from production release. The public Vercel deployment runs a released main-branch build, while ongoing implementation can continue independently. The article's production descriptions and screenshots were checked against that deployed version rather than assuming the newest development work was already public.

## Current Direction

Exfiltrate has grown from a retrieval concept into a systemic drone-salvage game, with a playable public build and a substantial supporting development environment.

The work centers on physical recovery, equipment preparation, incomplete information, and station systems that affect an expedition. Multiplayer and a shared persistent world remain longer-term design possibilities. The public build presents the current browser-based experience, while development continues to expand the systems and tools behind it.
