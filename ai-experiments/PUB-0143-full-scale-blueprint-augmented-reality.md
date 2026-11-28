# Walking Through Blueprints in Augmented Reality Before the Tools Were Ready

One of my earlier AI-assisted software experiments was an augmented reality (AR) blueprint viewer designed to run in a phone's web browser. The goal was to upload an architectural drawing, place it over the real surroundings at full building scale, and use the phone to walk through the proposed layout before construction.

The idea came from my own drafting work. A floor plan could become a full-size overlay on the ground, with room boundaries and doorway locations occupying the space they would represent in the finished building. The phone would provide a viewing window into that drawing as someone moved around the physical environment.

The project was ahead of what I could reliably develop with the AI tools and phones I was using. Over a few weeks, enough of the browser prototype came together to experiment with loading, scaling, and viewing blueprints, while AR placement and stable tracking remained difficult. Development involved almost constant debugging. Getting a drawing onto a screen was achievable. Keeping it correctly scaled and positioned in the real surroundings while someone walked around was much harder.

## From a drawing to a space someone could walk

A floor plan communicates dimensions, relationships, and circulation. Reading those marks and imagining the resulting space is familiar work for someone who drafts or builds. A client may have a harder time judging how a room or passage will feel from the same sheet.

The experiment connected those two ways of understanding a project. My own drafting supplied the drawings. The application was intended to let someone upload a blueprint, position it in a virtual environment, adjust its scale, and attempt to place it into the real surroundings through augmented reality.

At full scale, the drawing would occupy the footprint of the space it described. Someone could move along a room boundary or through a doorway location instead of relying entirely on the reduced drawing.

The approach centered on flat blueprint imagery. Building a convincing three-dimensional environment around a plan would have been a further development task.

## AI helped build the prototype, but struggled with the whole system

AI was part of the software-development process. It helped turn the idea into code, work through implementation questions, and attempt fixes as problems appeared.

The difficulty was getting those pieces to behave together. Document loading, scale, phone movement, camera orientation, and placement in physical space all affected the same experience. A change could appear reasonable in isolation and still leave the overall application behaving incorrectly.

The retained development material includes repeated work on coordinate systems, rotation, calibration, and drift. One set of notes describes disabling rotation while the correct axis was being investigated. Another addresses a viewport that continued moving after the phone had stopped.

Those were consequential failures for this particular idea. If the drawing moves when the person stops, or responds to a tilt in the wrong way, it becomes difficult to trust the relationship between the plan and the room.

For the development task I was attempting, the AI assistance available to me was not reliable enough to carry most of that complexity without sustained intervention. Much of the time went into debugging rather than advancing the product.

## The browser route and Google's AR technology

The preserved code shows several approaches across the project's revisions. These include PDF.js for rendering blueprint documents, Three.js for browser graphics, phone motion-sensor experiments, and WebXR code for augmented-reality sessions and surface placement.

The Android AR path connects to Google's ARCore through the browser. Google documents that WebXR uses ARCore in Chrome on supported Android devices. That is the Google technology associated with this approach, rather than a separate Google application that automatically turns a drawing into a finished walkthrough. [Google's WebXR and ARCore documentation](https://developers.google.com/ar/develop/webxr/arcore-comparison).

The saved project also contains later revisions. Their more developed features should be kept separate from what the first few weeks of experimentation achieved.

## A phone was accessible, but a difficult viewing window

The phones available for the original experiment did not deliver the experience I wanted. Tracking and alignment needed work, and the viewing angle created a separate limitation.

A blueprint placed flat on the floor can be at the intended scale while still being awkward to understand through a small handheld screen. Looking down shows a limited portion of the layout. Changing the phone angle changes what is visible, but does not automatically provide a useful sense of the entire space.

The experience also ran into problems with seeing the virtual content in relation to the real surroundings, including pass-through behavior. A person needed enough awareness of both the drawing and the physical space to move comfortably and understand what they were looking at.

AR or VR glasses might have provided a better viewing experience. The headset options I was considering brought other problems: bulk, cumbersome equipment, and, in some cases, a connection to a computer. Outdoor use was another limitation in the experience I was trying to achieve. The phone remained attractive as a portable route, even though its screen and tracking introduced their own compromises.

## Walking into architecture firms with the idea

The project also became a small exercise in customer discovery. It was a potential addition to the work offered through my business, so I took the developing idea to architects.

These were cold walk-ins. I went into roughly six architecture firms, explained my work and the prototype under development, and asked whether they might have an interest in using something like it.

About three showed interest. The others were not interested or did not have time for the conversation. That was a useful response from a small set of encounters, without treating it as evidence of wider demand or a commitment to purchase.

Some feedback pointed beyond the original proposal. A few people were more interested in an augmented three-dimensional environment than a flat plan placed at full scale. Others indicated that different architectural software might be interesting if that was the direction I intended to pursue.

That distinction mattered. A walkthrough of drawing linework and an immersive representation of the proposed building offer different experiences. Talking to potential users exposed that difference before more development went into one interpretation of the product.

## An experiment worth retaining

The work remained an experiment rather than a finished commercial offering. It connected my drafting capabilities with browser graphics, augmented reality, AI-assisted development, and direct conversations with potential users.

The main limitation was the combined development and hardware experience. The idea could be demonstrated in parts, but the amount of debugging and the practical viewing problems prevented it from becoming the reliable walkthrough I wanted.

It is still a project I may revisit as AI development tools, mobile hardware, and browser-based AR and VR become more capable. The earlier work provides a useful starting point: a clearer understanding of the interaction, a record of the technical problems, and feedback about what some architects would actually want to see.

## Related commentary

- [From Hand Drafting to AutoCAD and AI](https://github.com/syndicatdotai/daniel-powell/blob/main/background/PUB-0083-drafting-from-handwork-to-ai.md)
- [Watching Wearables and AI in Construction](https://github.com/syndicatdotai/daniel-powell/blob/main/research/PUB-0069-wearable-field-interfaces.md)
