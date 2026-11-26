# How I Automate Reasoning on Site

## Overview

I built the Reasoning on Site production workflow across the first eight episodes. The first pass is manual. Once I figure out what needs to be done, then I automate the rest. I usually record one continuous file, including alternate takes and notes to myself. The workflow turns that recording into an edited audio master, a timed transcript, release material, and, when I request it, a portrait short with original illustrations.

## Role

I record and host the show, direct the edit and artwork, and decide when an episode is ready. I use Codex to run the workflow and work through editorial decisions with me. I keep the instructions in skills, reusable settings in named profiles, and the choices for each episode in its production record. The scripts handle operations I can specify precisely, such as decoding audio, applying a filter chain, or rendering a supplied timeline.

## Scope Of Work

The workflow covers recording intake, local transcription, editorial review, audio processing, final transcription, Spotify draft preparation, website episode pages, and Discord updates. A YouTube Short is an additional production path with its own edit, captions, shot plan, artwork, and render. Spotify publication is manual. Website production deployment also has a separate approval.

## Key Actions

### 1. Transcribe the original recording

I usually record the whole thing in one file. If I want another take, I can say something like “restart, three, two, one” and keep recording. I can speak an editing note or leave a placeholder the same way. Codex can read those phrases as editorial cues about the recording. Their role is to help identify what should be kept or removed from that file.

Intake verifies the episode number against the existing records and preserves the original. A source hash helps identify the recording on a retry. A Python script runs Faster Whisper locally with the English `medium.en` model, CPU inference, INT8 compute, voice activity detection, and word timestamps. This produces a transcript where I can locate a phrase in the recording by its time range.

### 2. Build a time-based edit from the transcript

The AI reads the transcript and identifies likely recording slates, countdowns, superseded takes, spoken placeholders, and unrelated interruptions. It can also look for long gaps. The production workflow checks proposed boundaries against voice activity and waveform energy so the cuts preserve the first and last sounds of words. An ambiguous phrase stays available for review.

I also use the transcript to work out the order. If I explain why a detail matters after I’ve already gone through the example, it may make more sense to put that explanation first. Sometimes that’s one sentence. Sometimes it’s a complete section. The continuity skill checks what the listener knows at each join and whether a move changes chronology, cause and effect, or the meaning of what I said. It can recover a connecting sentence from elsewhere in the recording.

The edit map stores the retained source ranges, their playback order, and the reason for a move. The audio is assembled from those source ranges. The original recording and source transcript stay available, and the assembled audio can be checked at the joins. The short gets a separate continuity pass because cutting down an episode can remove a setup that was clear in the full version.

### 3. Apply the audio profile and transcribe the result

I keep an unfiltered copy of the edit. The default profile measures the edited dialogue and applies a single constant-gain adjustment toward a true-peak target of −1.8 dBTP before cleanup. The adjustment depends on the recording. The filters and their order come from the profile.

FFmpeg applies `adeclick`, an 80 Hz high-pass filter, a 2.7 dB cut around 180 Hz, `deesser`, and `alimiter`, in that order. The workflow applies a pitch-preserving tempo change of 1.1×, then adds the intro and outro. The audio profile specifies 48 kHz stereo, a 24-bit PCM WAV, and a 128 kbps MP3. It saves the resolved settings with the episode and checks decoding, duration, levels, and the bookends.

A fresh transcription of the finished audio accounts for the cuts, reordered sections, speed change, and intro. This is the source of the timings for the full-episode transcript. The short has its own word timings based on the speech in that cut.

### 4. Prepare release material and update the existing records

The workflow prepares the Spotify title, description, links, and numbering. I use a three-digit bracketed number in the title and fill in Spotify’s dedicated season and episode fields separately. When supported access can create or update a draft, the workflow saves the audio and metadata there, verifies the saved values, and retains the draft reference. When that access is unavailable, the audio and upload instructions are prepared locally for the remaining step. I publish in Spotify myself.

The website is a static build generated by Node.js from content and metadata. The workflow adds the MP3, transcript download, and timed episode page to the local version. The build derives a transcript search index from the episode content. Browser JavaScript links a transcript passage to the corresponding playback position and supports searching published transcripts across episodes. Production builds exclude entries marked as drafts.

I organized the Discord into places for getting started, community discussion, work people are building, and show content. I use Discord’s native permissions and link filtering alongside separate administration and moderation processes. The Node.js bot project uses `discord.js` 14.28.1, `@modelcontextprotocol/sdk` 1.32.2, and Zod 4. The administration interface exposes typed tools through the Model Context Protocol. Moderation runs as a separate worker hosted on Railway.

An episode gets one Discord message. The workflow saves the message reference, along with the destinations that are still pending. The release update verifies the live Spotify or website destination and edits the same message to replace the corresponding coming-soon entry. It also updates the website’s Spotify destination. The saved production record lets a later run resume from the correct episode and update work that already exists.

### 5. Select and storyboard the short

I read the transcript again and look for a higher-impact point I can get to quickly, enough setup for a new listener, and a reasonable place to stop. The short can use multiple parts of the recording if they make sense together. The current render profile caps the entire piece at 179 seconds, including the title and closing card.

Each shot has a spoken interval, a subject, an action, and a proposed framing. I work out what needs to appear before applying the art direction. Some of the direction comes from drawings I made years ago. Field Notebook Orange carries over things like open paper, dark freehand ink, graphite, and selective orange. The artwork profile supplies the drawing instructions, while the shot brief supplies what happens in that particular image. I keep the approved still and its generation prompt with the shot.

When several images need to show the same location, I can make a measured 3D blockout first. The lightweight tool uses Python, NumPy, and Pillow to render different cameras as black-and-white linework from one model. I can check where someone can stand and how the space is used before generating the finished illustrations.

### 6. Build and render Signal Break

The video composition takes the edited WAV, still images, timed caption words, scene intervals, graphics, and effect cues. A Python staging step assembles the render inputs. HyperFrames renders the vertical MP4 at 1080 pixels wide and 1920 pixels tall, at 30 frames per second. GSAP drives the timeline and Three.js runs the artwork shader.

The shader samples the red, green, and blue channels at slightly different positions for chromatic aberration. It also applies edge fade, scan lines, grain, and perimeter blur. The shader supports bloom for glow, with its strength controlled by the profile. In the current version 3 profile, bloom is set to zero. The short horizontal tears are timed to the title handoff and selected scene changes. Captions are composed separately in JetBrains Mono ExtraBold, so they stay readable during the effects. The display uses lowercase words and leaves gaps blank between spoken cues.

For a shot that benefits from depth, I use an opaque background and one or two transparent layers registered to the same canvas. The foreground and background both move at different rates, and the camera can push in. A shared parallax profile supplies speed and travel. The shot record decides whether to use layers and which direction they move. I can adjust the shared profile once for future renders. The finished short uses the already processed speech at its selected speed.

## Important Features

- **Skills define the work.** The production skill calls the editorial continuity, audio cleanup, caption, artwork, and video instructions at the point each is needed.
- **Profiles store reusable choices.** Audio, art, video, and parallax can change independently. The resolved versions are saved with an episode or export so the settings used for an earlier render can be recovered.
- **The episode record stores state.** It tracks source identity, edit ranges, current artifacts, review state, publication references, and pending links. On a retry, the workflow checks that record before it repeats an upload or creates another Discord post.

## Constraints And Decisions

I decide what I’m trying to say, which edits preserve it, and when the episode is ready. Spoken notes supply editorial context for the recording. Publishing and backend changes require direction outside the recording and outside Discord. The review also checks that the captions match the exported speech, the images match the commentary, and construction scenes make physical sense.

## Deliverables

A full episode produces an original backup, an edit map, an unfiltered edit, final WAV and MP3, an aligned transcript, release copy, and a production record. A requested short adds the excerpt plan, shot list, stills and generation prompts, timed captions, profile snapshots, and a portrait MP4. Website and Discord artifacts retain the information needed to update their destinations as they go live.

## Outcome

I worked through eight episodes while building this process. The workflow now lets me reuse the tasks that stayed the same from episode to episode and pick up an existing draft or post when it needs an update. Each episode still has its own edit, set of images, and release state.

## Tools And Methods

| Part | Tools | What gets passed forward |
| --- | --- | --- |
| Transcription | Python and Faster Whisper | Source word timings, then fresh timings for the finished audio |
| Audio assembly and cleanup | Timestamped edit map and FFmpeg | Reviewed source ranges, episode master, WAV and MP3 |
| Website | Node.js, static HTML and browser JavaScript, deployed through Vercel | Episode metadata, audio, timed transcript and search index |
| Community | Discord, discord.js, MCP SDK, Zod and Railway | Episode message reference and pending-link state |
| Artwork and blockouts | AI image generation, reusable art profiles, Python, NumPy and Pillow | Selected stills, recorded prompts and optional spatial references |
| Short render | HyperFrames, GSAP and Three.js | Timed portrait composition and encoded MP4 |

## Evidence And Limitations

This describes the workflow I built and used during production of the first eight episodes. Settings are representative of the named production profiles. Individual episodes and experiments can use different versions. Draft creation depends on the supported Spotify access available for that run, and each platform has its own release state.
