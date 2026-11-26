# Using AutoCAD Elevations for Customer Concept Images

## LinkedIn Summary

I take a screenshot of an exterior elevation from AutoCAD, paste it into Codex, and use OpenAI's image generation to turn it into a believable view of the design.

I keep the design palette in a JSON file, a structured text file that I can reuse with each prompt. That gives separate image generation sessions the same design reference and helps keep the results consistent without explaining the palette from scratch every time.

It's not 100% accurate. I still need to compare it with the drawing, but it's enough to get a conversation started with the customer about how the exterior could look.

## Overview

I use an exterior elevation from my AutoCAD design as the starting point for a generated concept image. A screenshot is enough to supply the visual reference for this workflow.

I paste that capture into Codex and use OpenAI's image generation to develop a believable view of the exterior. The purpose is to give the customer something visual to discuss early in the design conversation.

## Role

I provide the design, the elevation screenshot, and the saved design palette. The image generator interprets those inputs. I still need to judge how closely the result represents the drawing.

## Scope Of Work

The workflow covers exterior concept imagery from existing design elevations. It also carries a saved palette between separate prompts so the visual direction does not have to be recreated from memory each time.

## Key Actions

- Capture the relevant exterior elevation in AutoCAD.
- Paste the screenshot into Codex.
- Supply the saved JSON palette with the image request.
- Generate the concept image using the elevation and palette as references.
- Compare the result with the drawing before using it in the customer discussion.

## Important Features

The JSON file holds the palette as structured text. Reusing that file gives separate prompt sessions a common reference.

The consistency comes from supplying the same design information again. A new prompt still needs access to the file or its contents; saving a palette does not mean every future session automatically knows it.

## Constraints And Decisions

The result is not completely accurate. The saved palette helps keep the visual direction consistent, but it does not guarantee that the image will preserve every feature of the elevation.

I treat the output as concept imagery. The AutoCAD drawing remains the reference for checking what was actually designed.

## Deliverables

The workflow produces a generated exterior concept image and uses a reusable JSON palette alongside the original elevation screenshot.

No customer drawings, palette files, or generated images are included in this article.

## Outcome

In my experience, the images are believable enough to get the customer conversation started. They provide something to react to when discussing how the exterior could look.

## Tools And Methods

AutoCAD exterior elevations, screenshot capture, Codex, OpenAI image generation, and a JSON design palette reused across separate prompts.

## Evidence And Limitations

This record describes my workflow and assessment of the results. It does not claim exact geometric fidelity, identical images between sessions, or a measured accuracy rate.
