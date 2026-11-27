# Mech Division: An Early Experiment in Automated Game Development

## Project Summary

I started Mech Division in April 2026 as a top-down mech shooter. The idea had some connection to Splitshooter, a game I had made in 2005, but this project became a test of a different development process.

I wanted to see how far a game could develop through an automated loop. I set out a small set of instructions in an ordered process, gave the system a feature roadmap, and let it repeatedly work through the next piece of the game.

The result was playable. It had levels, progression, combat, unlocks, and a complete campaign structure. I consider it a partially successful test. The process produced a functioning game, but the models I used at the time did not handle the repeated development loop well enough to produce the overall result I wanted.

## My Role

I established the game concept, directed the features, and organized the instructions for the recurring development process. I also made adjustments as the experiment progressed, including changes to the environments, combat presentation, and feature priorities.

The automated runs handled successive implementation tasks. My involvement was in setting the direction, revising the instructions, and evaluating what the accumulated changes actually produced.

This was a test of whether I could delegate an ongoing development process, with the system continuing from its previous work instead of requiring a new conversation for every feature.

## How the Development Loop Worked

I began running the automated development loop around May 3–4, 2026. Initially, I described it as an hourly process. The schedule changed during the experiment; the final saved configuration used a three-hour interval.

Each run was instructed to check the project’s current state, read the development rules and working memory, and select the highest-priority unfinished task that could fit into one run.

It would then implement that task, run validation, record what it had completed, and identify the next recommended task. If the checks passed, it could commit the change and push it to GitHub.

The working memory carried the results forward: completed features, validation results, blockers, and recommendations for the next pass. That gave the following run something concrete to continue from.

The final automation configuration used GPT-5.3-Codex with high reasoning effort. It was instructed to make bounded changes and preserve existing work. The loop also had instructions about where gameplay logic, interface code, and editor behavior belonged, so new features would have an established place in the project.

I continued feeding the process additional requirements. Early additions included more building shapes and terrain. Later priorities covered enemy behavior, animation pacing, effects, sound, and mobile controls.

## What the Game Contained

Mech Division developed into a solo-first arcade campaign with five missions:

1. **Ember Drop** introduced the campaign and unlocked double jump.
2. **Ash Corridor** continued the progression and unlocked dash.
3. **Iron Reservoir** unlocked the shield ability.
4. **Relay Blackout** included a hold-the-relay objective and unlocked overdrive.
5. **Citadel Core** ended the campaign with a boss objective.

The target was a compact campaign of roughly 15–20 minutes. That was the design and pacing target, rather than a claim that every player would finish in that time.

The game included mission briefings, level selection, locked and unlocked stages, pause screens, mission completion, campaign completion, and game-over states. Progress was saved locally, including completed missions, unlocked features, and best times.

Combat included drones, scouts, bruisers, artillery enemies, and a boss. Dash, shield, and overdrive had active controls and resource behavior. Repair and energy pickups supported the later missions.

These systems made the result more than a single combat scene. There was a sequence to play through and a progression of capabilities as the player advanced.

## Building the Levels and Supporting Tools

The project included a world editor and support for loading custom worlds. The environments used buildings, trees, crates, boxes, grass, and other terrain details to give the levels more structure.

Because the camera looked down over the action, environmental detail had to remain readable without hiding the player. I directed the work toward low buildings and terrain shapes that could add variety while preserving the view.

One specific requirement was that enemies should not be able to see or shoot the player immediately at mission start. The campaign used sheltered starting areas, with cover positioned to protect the spawn until the player moved out into the level.

Enemy work expanded into patrol routes, detection, pursuit, searching, and movement around obstacles. The game also retained co-op skirmish support, although the automated campaign work prioritized solo play.

## Presentation and Game Feel

The development included camera behavior, projectile height, muzzle flashes, enemy silhouettes, movement speed, and animation timing.

Later work added or refined impact effects, explosions, screen shake, mobile vibration, sound effects, and music. The mobile interface used touch controls, with icon-only combat buttons to keep the playfield clear.

There were also practical behavior fixes. Completing a mission needed to stop combat, rather than leave the player firing or enemies updating behind the completion screen. Pause and game-over screens needed to remain readable on a small display.

These were parts of making the game function as a complete experience, alongside adding new mechanics.

## Testing Inside the Loop

The automation was instructed to run lint and production-build checks before publishing changes. The project also accumulated Playwright tests covering campaign progression, abilities, mobile interfaces, enemy behavior, spawn protection, and other gameplay systems.

Development controls allowed automated tests to start missions, inspect game state, and supply player input. Telemetry tracked behavior such as ability use and campaign events, giving the loop information it could check between iterations.

The tests helped the process verify specific behavior. They did not, by themselves, establish that the game was enjoyable or that the next automated task was the most valuable development choice.

## Where the Experiment Reached Its Limits

The loop kept producing work. The more difficult part was getting that repeated work to become a game I considered useful as a finished result.

One example appears at the end of the development sequence. A change replaced sustained music tones with sequenced musical pulses. Subsequent runs added a history of scheduled notes and then increasingly specific checks of how those notes behaved during higher-pressure combat.

That work addressed real implementation details, but it also shows how the process could continue deep into a narrow area through its own next-step recommendations. The ability to generate another task and complete another check was not the same as evaluating the game as a whole.

My assessment is that the models available to me during this test were not yet good enough at the looping nature of the instructions. They could implement features and continue the sequence, but the overall output still needed more direction and judgment than I wanted to provide for this experiment.

## Outcome and Development Status

Mech Division was a partially successful automation experiment. It produced a functioning game with a five-mission campaign, progression, abilities, enemy variety, an editor, and supporting tests.

It did not produce a finished game that I wanted to take forward as-is. Its value to me was in testing the development loop itself and seeing where repeated autonomous implementation worked and where it needed intervention.

The latest commit currently on the GitHub main branch is dated **May 11, 2026**. The final gameplay-related changes concerned combat music behavior and its validation, followed by an update recording the publication status. The development automation is paused.

## Tools and Methods

Next.js, React, TypeScript, Three.js, React Three Fiber, Playwright, GitHub, local progress storage, a browser-based world editor, and scheduled AI-assisted development with persistent working memory.
