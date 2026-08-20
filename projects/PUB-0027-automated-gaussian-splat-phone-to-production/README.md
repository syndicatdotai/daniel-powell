# Automating Gaussian Splats from Phone Capture to Production

## LinkedIn Summary

One of the more technical systems I have built is an end-to-end workflow for producing Gaussian splats.

I can record a high-resolution video on my phone, let Dropbox transfer it to my computer, schedule the work, and give Codex the source file. From there, the agent orchestrates a pipeline built from open-source components: FFmpeg for inspection and frame extraction, COLMAP for camera-pose reconstruction, Brush for 3D Gaussian splat training, SplatTransform for delivery conversion, and SuperSplat for the browser viewer.

The workflow checks the capture and camera solve before committing GPU time to training. It then trains and validates the model, prepares a web-ready asset, builds the viewer, publishes it through Codex Sites, verifies the production deployment, and prepares the link for client handoff.

For a suitable capture that passes the quality gates, the full path from raw video to a live interactive scene can now be completed in about 30 minutes.

Getting here took many hours of installation, failed runs, troubleshooting, script repair, testing, and browser QA. The process looks simple now because that complexity has been moved into a repeatable workflow. Once I initiate the job, Codex can carry it through the automated production pipeline while I retain review of the final model and delivery.

#GaussianSplatting #3DGS #ComputerVision #AIAgents #OpenSource #Codex

## Overview

This record documents a repeatable, agent-orchestrated workflow that turns a suitable phone video into a validated Gaussian splat and a production browser viewer. Daniel records a high-resolution source video, transfers it to his computer through Dropbox, schedules the processing work, and gives Codex the source. Codex then runs an established pipeline assembled from open-source reconstruction, training, conversion, and viewing components.

The important result is not only model generation. The workflow carries the source through inspection, camera reconstruction, training, validation, delivery conversion, viewer construction, production publication, browser QA, and client handoff. For a suitable capture that passes the quality gates without recovery work, the path from raw video to a live interactive scene can be completed in about 30 minutes.

## Role

Daniel designed, tested, and maintains the workflow. He developed the operating sequence, selected the toolchain, resolved installation and compatibility problems, established the quality gates, tested failed and successful configurations, and created the reusable Codex instructions that govern each stage.

For each production run, Daniel records and transfers the source, identifies the intended job, initiates the workflow, reviews the final reconstruction and viewer, and controls delivery to the client. Codex acts as the orchestration layer across the local tools and the hosted production stage.

## Scope Of Work

The workflow begins with source intake and preservation. The original video remains unchanged while a project-specific working copy is created. The media is inspected, frames are extracted, and the capture is reviewed for coverage, blur, motion, exposure changes, reflective surfaces, weak texture, and insufficient parallax.

Camera reconstruction follows through feature extraction, matching, mapping, model analysis, and undistortion. Full GPU training does not begin until the camera registration and scene geometry pass the defined gate. Brush then performs a short smoke test followed by the selected training mode and retained checkpoints.

The trained model is evaluated from known source-camera views. Once accepted, it is converted into a web-delivery asset, loaded into an interactive viewer, checked against hosting limits, published through Codex Sites, and verified in production before the client link is handed off.

## Key Actions

The pipeline uses FFmpeg to inspect the source and extract an ordered image sequence. COLMAP reconstructs the camera poses and sparse scene geometry. Automated analysis checks whether the solve is coherent enough to justify training. This prevents a technically completed but incorrect camera model from consuming the full training run.

Brush trains the 3D Gaussian representation after a smoke test confirms that the data and toolchain are functioning. Checkpoints and held-out renders provide evidence for selecting a model rather than assuming that the last or largest output is best.

SplatTransform prepares the validated reconstruction for browser delivery. SuperSplat Viewer supplies the interactive presentation layer. The site is preflighted, published, and checked for correct asset loading, initial framing, interaction, and browser errors before delivery.

## Important Features

- Phone-to-computer source transfer through Dropbox.
- Scheduled, Codex-initiated processing.
- Open-source reconstruction and delivery toolchain.
- Immutable source preservation and separate run folders.
- Capture inspection before expensive computation.
- Camera-solve quality gate before full training.
- GPU smoke test before the main optimization run.
- Held-out render validation and checkpoint comparison.
- Separate full-detail local model and web-delivery asset.
- Production payload preflight and browser verification.
- Agent orchestration with human review and release control.

## Constraints And Decisions

The automated path depends on suitable source material. Gaussian splat reconstruction expects a substantially static scene, coherent camera movement, useful overlap, adequate texture, and sufficient parallax. Motion, blur, reflective surfaces, repeated patterns, weak coverage, and camera-solve fragmentation can require a recapture or an exception workflow.

The timing describes the steady-state production path, not the original engineering effort and not a guarantee for every scene. Higher-quality training modes, failed camera gates, difficult cleanup, hosting limits, or production-viewer issues can add time.

Automation does not remove quality control. Daniel still selects the source, reviews the reconstruction, handles exceptions, and authorizes client delivery. No client identity, project location, production hostname, private storage path, pricing, or dimensions are included in this public record.

## Deliverables

The production deliverables include a preserved source, processing logs, camera reconstruction, validated Gaussian splat, retained checkpoints, web-delivery asset, interactive browser viewer, verified production deployment, and a client-ready access link. Full-detail local outputs are preserved separately from any optimized web asset.

## Outcome

The system converts a process that originally required repeated manual setup, troubleshooting, tool changes, failed experiments, script repair, and browser debugging into a repeatable production workflow. The setup consumed many hours because each stage had to be understood and validated independently.

That engineering effort is now embedded in the reusable pipeline. Once Daniel supplies a suitable video and initiates the job, Codex can coordinate the open-source tools from ingestion through production delivery. A passing capture can become a live interactive scene in about 30 minutes while preserving quality gates and final human review.

## Tools And Methods

The workflow uses Dropbox for source transfer, Codex for agent orchestration, FFmpeg for media inspection and frame extraction, COLMAP for camera reconstruction, Brush for 3D Gaussian splat training, held-out render comparison for validation, SplatTransform for browser conversion, SuperSplat Viewer for interaction, Codex Sites for hosted delivery, and browser-based production QA.

The system also uses immutable project folders, work logs, stage-specific exit checks, smoke testing, checkpoint retention, payload preflight, and production readback. These controls make the automation repeatable without treating every completed command as a successful reconstruction.

## Evidence And Limitations

This record is based on Daniel's direct description and the validated Gaussian Splat Video Pipeline operating record. Supporting evidence includes successful room and object reconstructions, camera-gate testing, held-out render checks, browser-delivery conversion, production viewer QA, and documented failed attempts that informed the current safeguards.

The approximately 30-minute result applies to the established steady-state mode when a suitable capture passes its gates. It does not include the many hours originally spent installing tools, researching version changes, diagnosing failed models, repairing scripts, comparing training settings, refining mobile delivery, and building the reusable workflow. It should not be interpreted as a guaranteed processing time for every capture or as an unattended release process.
