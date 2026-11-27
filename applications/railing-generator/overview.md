# Railing Generator

*PUB-0080 · Application development · Daniel Powell · November 25, 2026*

## LinkedIn Summary

A railing manufacturer in Connecticut hired me to take field measurements and prepare shop drawings. I used to spend 45 minutes to an hour in AutoCAD drawing a railing after I had the measurements. I’ve been developing Railing Generator for about nine months now. For a configuration it already handles, I can get that drawing out in about 30 to 90 seconds.

I send Codex a voice memo with the stair run and rise, the lengths of the upper and lower landings, and the pitch of any landing that’s out of level. In the same memo I can give it the rail configuration, the style, and any comments I want printed on the shop drawing.

Codex enters those measurements into an editable project and runs the application. The same drawing model runs whether I dictate the measurements from my phone or enter them in the browser. I built the spacing and height rules into that model. If a landing measurement changes, the generator can lay out the spindles across the revised span and update the dimensions. I can reopen that project and generate the AutoCAD drawing and cut sheet from the same revision.

On a straightforward railing, I can finish measuring, send the voice memo, and have the drawing ready before I get back to my truck. I can review the elevation while I’m still standing there looking at the actual railing location. Once I’m satisfied with it, I can have Codex upload the AutoCAD file and exported PDF to the manufacturer’s CRM.

I still get jobs with details the application doesn’t cover. A bracket at the end of a railing is a good example. I could spend the next hour drawing it in AutoCAD. If I think I’ll see it again, I’d rather spend that hour building in the bracket, deciding which dimensions can change and how to locate it against the post. The next time I measure one, I can give it the new dimensions by voice. If it’s a detail I only expect to draw once, I’ll do it in AutoCAD.

## Try the Application

[Open Railing Generator](https://railing-generator.vercel.app/)

Railing Generator is a specialist drawing application in ongoing development. Start with a practice project to understand how its measurements, configuration choices, and exports relate.

- [Introduction to the application](introduction.md)
- [Getting started](getting-started.md)
- [From field measurements to delivery](field-to-drawing-workflow.md)
- [A worked example](example-project.md)

The public application is the drawing tool. My voice-directed Codex workflow, production project records, and manufacturer CRM handoff are described separately in these guides.

## Overview

A railing manufacturer in Connecticut hired me to take field measurements and prepare shop drawings. I see the job twice in a sense. On site, I’m looking at the stair, the landing, and where the railing needs to go. At the drafting stage, I have to turn what I measured into an elevation the shop can use. Doing both parts of the work has shaped how I built Railing Generator. I can describe a railing in the order I measure it and see how those measurements come together on the sheet.

As of November 25, 2026, I’ve been developing the application continuously for about nine months alongside that work. A shop drawing that used to take me 45 minutes to an hour in AutoCAD now takes me about 30 to 90 seconds to get out when the generator already supports the configuration. That’s from the point where I have the field measurements and know the layout. I dictate what I want, run the generator, and have a dimensioned drawing in front of me to review.

The jobs themselves have set the pace of development. Every so often I measure a condition I haven’t built into the application. I can spend the next hour drawing it in AutoCAD, or I can spend that hour adding a capability I’ll have on the next order. How likely I am to see that condition again has a lot to do with which way I go.

## Role

Drawing the railings myself first had a lot to do with how I built the application. Take a rail coming up a flight of stairs and meeting a post. When I drew that in AutoCAD, I knew which face of the post I wanted to dimension to, where the rail needed to finish, and what that left me for spindle spacing. On paper those look like separate details. When the post moves, they all change together.

## Scope Of Work

Those relationships are what I put into the software. I still choose where the post goes. The generator uses that choice to lay out the elevation and calculate the dimensions that depend on it. When I open the drawing, I can read it the same way I read one I drafted myself. If the dimension is taken from the wrong face, I know what needs to change. Since I’m also developing the application, I can make that correction in the calculation and carry it forward to the next drawing.

## Key Actions

### What I dictate in the field

I dictate the stair run and rise, then describe the upper and lower landings that are part of the job. I give the length of each landing. If a landing is out of level, I give its pitch so the drawing follows what I measured on site. In the same voice instruction, I can specify the rail configuration and style and dictate any comments I want printed on the shop drawing.

Codex puts those measurements and selections into the editable project and runs Railing Generator. That saves me from entering the same field measurements again in AutoCAD. I can go straight to the elevation and see how the stair meets each landing, how the rail follows the pitch, and whether the notes the shop needs are on the sheet.

On a straightforward railing, I can finish measuring, send Codex a voice memo, and have the shop drawings ready before I get back to my truck. I can review them while I’m still on site and have Codex upload the AutoCAD files and exported PDFs to the railing manufacturer’s CRM. That means I can leave the site with the drawings already on the manufacturer’s job record.

## Important Features

### How the spacing is calculated

Post spacing, spindle spacing, top rail height, and clearance under the bottom rail are all part of the layout. I built the applicable minimums and maximums into the drawing rules so I can adjust a configuration with the code constraints already accounted for in the calculation. For example, changing a landing length changes the span available for the infill. The generator uses its spacing rules to lay out the spindles across that span, which saves me from working out each opening by hand.

I review the resulting dimensions for the particular job, especially when I choose a manual post layout. The automatic layout gives me a starting point that reflects the rules I use for these railings.

## Tools And Methods

### How the drawing gets made

The browser was where I started. One of the more important changes during development was pulling the drawing calculations together so the preview and the exported files came from the same model. The application uses JavaScript and Maker.js for the two-dimensional geometry. Later, I added a Node.js command-line workflow that could read a saved project and run those same calculations. That gave Codex a direct way to use the application.

The division of work is fairly simple. Codex interprets what I say and prepares the inputs. Railing Generator calculates the railing. A landing pitch I dictate in the field goes through the same drawing logic as a pitch I enter in the browser. That means the work I put into getting a particular detail right in the visual editor is also available when I ask for it from my phone.

## Deliverables

I keep the editable project as JSON because I want to retain the decisions behind the sheet. From that project I can generate a DXF to continue working in AutoCAD, a dimensioned sheet to print or share, and a cut sheet listing the individual components. The sheet is laid out as vector artwork in SVG. When I need an image, Chromium renders that sheet to PNG. If I revise the project, I can generate the outputs from the revised inputs and keep the shop information together.

## Constraints And Decisions

### When I spend the hour on development

A bracket at the end of a railing is a good example of the kind of decision I face. For one drawing I can locate the bracket against the terminal post, draw it to size, and add its dimensions. To support it in the application, I have to think one job further ahead. Which measurements will I want to change on the next order? What should stay referenced to the post? Where will the dimension read clearly when the bracket size changes?

If I expect to see that condition again, I’m willing to spend the hour building it. I have an actual drawing in front of me to develop against, and I know what I need the shop to be able to read. By the time I use the feature on another job, I’ve already worked through the placement and dimensioning. I can give the new measurements by voice and get on with reviewing the sheet. If a condition is peculiar to one order, I’ll still draw it in AutoCAD and deliver it that way.

## Outcome

Some of the most useful changes have come from looking at the finished sheet. I tried increasing image resolution at one point. When I looked at the whole page on a phone, what needed attention was the space around the railing. A long note needed somewhere to wrap, and the dimensions needed to stay clear of it. I changed the layout so the note wraps to the width of the drawing and the frame accounts for the space the text takes up. That improvement now applies every time I generate a sheet.

I’ll keep developing Railing Generator as new conditions come up in the field. There are details it doesn’t cover yet, and measuring the next job is often how I find out which one is worth tackling. If I expect to encounter it again, I’ll use that job to work out what the application needs to accept, what the shop needs to see, and whether the generated drawing gets it right. The next time I measure a railing with that detail, I can call it out by voice and put the hour I already spent on development to work.

## Evidence And Limitations

These times come from my own drafting work on configurations the generator supports. Earlier commentary covers [how manual shop drawing informed the application](../../workflows/PUB-0009-manufacturing-knowledge-in-software.md) and [how I decide which features to build](../../workflows/PUB-0074-incremental-railing-development.md).

[Daniel Powell on GitHub](https://github.com/syndicatdotai) · [Public project archive](https://github.com/syndicatdotai/daniel-powell)
