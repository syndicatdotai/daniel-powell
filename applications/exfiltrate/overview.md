# Developing Exfiltrate: Remote Drones, Salvage, and Interacting Station Systems

## Project Summary

I'm developing Exfiltrate, a game about remotely operating a drone inside dangerous derelict installations, recovering salvage, and getting it back to a support station.

The original idea was closer to entering a maze and retrieving an important object. As I worked on it, the game became more about exploring an unfamiliar place, finding useful equipment and materials, and deciding how much risk to take before returning.

The drone's equipment, the information available to the operator, and the condition of the station all became parts of that decision. Development expanded into towing, storage, fabrication, power distribution, communications, sensing, and environmental effects.

I've also spent considerable effort on the tools and architecture used to develop the game with AI. The project now has a documented map of its systems, authoring tools, diagnostics, and a development history that records how the design changed.

## Overview

The player operates machinery from a distance. That creates a different relationship with the environment than directly controlling a person walking through a station.

The operator depends on the drone's observations and connection. Equipment can be damaged, cargo can affect movement, and the information on the screen does not have to reveal everything that exists in the world.

The game is being developed with mobile play in mind. The playable work runs in the browser, while the longer-term design includes possibilities for multiplayer expeditions and a shared persistent world.

## Role

I have been developing the game concept, directing the mechanics and interface, and using AI-assisted development to work through implementation, architecture, and iteration.

The work has included deciding which systems belong in the game, how those systems should interact, and what information the player should receive. It has also involved developing the tools needed to inspect, tune, and author those systems.

## Scope Of Work

Exfiltrate has grown across several connected areas:

- Drone movement, equipment, physical interaction, and towing.
- Salvage recovery, storage, fabrication, and support-station services.
- Power, communications, sensors, and environmental behavior.
- Player observations, remembered information, and visual presentation.
- World and content authoring, developer controls, diagnostics, and validation.
- Save behavior, runtime performance, and mobile presentation.

The implementation and research have progressed at different rates. The current article focuses on the documented playable and development systems, with broader shared-world plans identified separately.

## Key Actions

- Developed the remote-drone extraction concept into a salvage-oriented gameplay loop.
- Added physical cargo handling and systems for storing recovered items.
- Connected recovered resources to fabrication and equipment workflows.
- Developed station services and environmental systems with shared architectural rules.
- Separated the world's internal state from what the player could observe.
- Built developer tools for inspecting behavior and adjusting configuration.
- Established documentation that guides AI coding sessions to the relevant systems and tests.
- Recorded development milestones, performance experiments, and replaced approaches.

## Important Features

### Salvage creates a reason to decide when to leave

Moving beyond a single mandatory objective changed the structure of an expedition.

A station could contain useful machinery, components, equipment, and materials. Finding something worthwhile created a decision about continuing deeper or returning with what had already been recovered.

That direction shaped the development of cargo handling, storage, and fabrication. Recovering an object became part of a larger loop involving what the player could carry, preserve, use, or bring back into the world.

### Cargo and equipment have physical consequences

Towing became more than attaching a visual object behind the drone. The development work addressed mass, resistance, body footprints, collisions, and rotation from off-center contact.

The same attention extended to item ownership. An object in the world, an item in storage, and installed equipment needed clearly defined transitions. The inventory implementation includes checks intended to prevent the same item from occupying multiple locations at once.

These rules support the practical behavior of salvage: recovering something, moving it, storing it, and using it again.

### The support station became part of play

The Host, the game's support station, developed beyond a launch point into a place for handling cargo, charging, storage, and fabrication.

The fabrication system tracks resources and reserves storage capacity for the resulting equipment. That connects the act of collecting salvage with preparing for further activity.

Some progression work remains separate from the player-facing experience. For example, the retained Host upgrade documentation distinguishes implemented backend capability handling from deferred player interfaces and account progression.

### The station's systems interact

The environment developed beyond a static arrangement of walls and obstacles.

The development record describes work on electrical distribution, breakers, local generators, lighting, communications, sound, smoke, and thermal behavior. These systems needed to share the station's geometry and state without being reduced to one generic effect.

The architectural direction was to define reusable behavior and let authored objects participate in it. A portable object might have several capabilities, such as being towable, chargeable, or controllable, without every combination requiring a separate hard-coded exception.

### What exists and what the player knows are different

One of the project's standing rules separates world state from player knowledge.

A hidden object can exist in the simulation without appearing in the player's interface. Information has to reach the operator through the appropriate observation system, and remembered observations remain distinct from current sensing.

The project also separates visual, acoustic, thermal, and electromagnetic signals. Those channels are not treated as interchangeable versions of one stealth number.

Screen readability is another separate concern. Making the interface easier for a person to read should not accidentally grant the drone information it has not acquired.

## Development Cycle and AI

### Giving a new coding session a useful starting point

As the game grew, the development process needed a way for a fresh AI session to understand the relevant part of the application.

The repository includes a context entry point, a development thesis, a project atlas, subsystem documentation, and maps to source files and tests. A task starts with its target system and then follows the direct dependencies that could be affected.

That structure gives AI-assisted work a bounded starting point. Work on inventory should account for item ownership and persistence; work on sensing should account for acquisition and presentation.

### Defining shared rules before adding more exceptions

The development thesis distinguishes implementing a new capability from authoring a new combination of existing capabilities.

It also separates authored definitions, derived data, runtime state, player knowledge, and presentation. Those distinctions give coding work a consistent set of boundaries as features accumulate.

For example, moving an object during play should not silently rewrite the original level definition. A developer inspection tool should not expose hidden information through the normal player view.

### Building tools for iteration

The project includes a world editor, content-authoring tools, a workbench, runtime inspection, and developer controls.

Developer snapshots can capture configuration and diagnostic information as JSON for use in a development discussion. This provides a more specific reference than describing a visual effect or movement setting from memory.

The tools support work on the application itself: creating content, changing settings, inspecting behavior, and comparing the result with the intended design.

### Keeping the development history

The project retains a series of development snapshots covering changes in the game concept, architecture, and playable systems.

Those records include approaches that were replaced. They help preserve why a system took its current form and which assumptions had already been tested.

That history is useful when returning to a complex area of the game or giving an AI session context for the next change.

## Performance and Mobile Development

Mobile performance has influenced both the renderer and the simulation work.

The development history records several attempts to reduce the cost of moving lights before a broader change to the camera rendering path. It also separates rendering cost from other causes of interruptions, including repeated world queries, environment updates, scheduling, and diagnostic overhead.

A recurring approach was to retain useful computed results and update them when their inputs changed. Different systems could then read those results instead of repeatedly reconstructing the same information.

The work also addressed pause and resume behavior. Returning to a browser game after an interruption is part of its runtime behavior, alongside what happens during uninterrupted play.

## Constraints And Decisions

I have kept the playable local work separate from the larger shared-world ambition. Multiplayer and persistent expeditions influence the design, but the retained records do not establish a finished shared-universe service.

The project also distinguishes development experiments from release behavior. Its workflow separates ordinary integration from deliberate releases, while the documentation identifies current architecture, historical snapshots, and future plans.

The mobile focus requires continual attention to how much simulation and presentation work the device can reasonably perform.

## Deliverables

- A playable browser-based drone extraction and salvage prototype.
- Movement, towing, cargo, inventory, and fabrication systems.
- Support-station and environmental-system implementations.
- Observation and presentation rules that distinguish player knowledge from world state.
- World and content authoring tools, developer controls, and diagnostics.
- Architecture documentation, source and test maps, and a development chronicle.

## Outcome

Exfiltrate has developed from a relatively direct retrieval concept into a broader salvage game with interacting systems.

The work has produced both the game prototype and the tools used to keep developing it. The current direction combines physical recovery, equipment decisions, incomplete information, and station behavior that can affect an expedition.

## Tools And Methods

JavaScript, HTML, CSS, Canvas 2D, WebGL, Web Audio, JSON definitions and snapshots, Git version history, automated tests, browser inspection, and AI-assisted development.

The project uses documented system ownership, reusable capabilities, explicit state boundaries, and separate development and release workflows.

## Evidence And Limitations

This article describes work in progress. It is grounded in the retained application source, architecture documentation, development history, and project notes.

Historical snapshots describe the state of particular development periods; they are not treated as proof that every planned feature is finished. A full gameplay test, current mobile benchmark, and live deployment review were not performed for this article.
