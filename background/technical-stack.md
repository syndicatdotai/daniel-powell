# My Technical Stack: From Early Web Development to AI-Assisted Systems

My projects connect business operations, research, construction documentation, web applications, and digital media. The tools vary with the task: a local Python script can prepare a research file, a browser application can generate a drawing, and a hosted service can keep a community workflow running between local sessions.

My technical background began before the current generation of AI tools. Around 2005, I was working with HTML and CSS, followed by JavaScript, PHP, and some MySQL. That developed alongside interests in graphics, game development, 3D tools, music, and video.

This overview moves backward from my recent projects to those earlier foundations. The dates identify periods of use; several tools span more than one period.

Use this page to identify technologies and periods of experience, then follow the linked project records for the work performed with those tools.

## 2026 — My Current Working Stack and Recent Projects

The recurring core of my recent work is Python, JavaScript and TypeScript, HTML and CSS, Node.js, Git, and readable records in JSON and Markdown. ChatGPT, Codex, and Cursor support development around that foundation. Larger application frameworks, databases, and hosting services enter where the project needs them.

### AI-Assisted Development and the Working Environment

ChatGPT, Codex, and Cursor have supported different parts of my development process. I use AI to work through requirements, investigate technical approaches, develop scripts and application features, inspect results, and refine the implementation around the problem being solved.

The work includes both direct use of AI development tools and applications that call language-model APIs themselves. In the first case, AI helps develop or operate the software. In the second, model processing becomes part of the application's behavior.

Windows is my main local working environment. PowerShell and command-line tools support file handling, application startup, exports, validation, and repeatable operations. Some reconstruction experiments also involved WSL-based tooling before the workflow developed around a maintained native Windows toolchain.

Git and GitHub provide source history and project organization. Branches and worktrees allow implementation, review, and production work to proceed separately. Private repositories hold application source where appropriate, while the public archive presents selected project commentary.

### Languages and Information Formats

Several languages recur across the work, with different responsibilities:

| Language or format | How I have used it |
|---|---|
| Python | Research collection, data preparation, API processing, document generation, media preparation, and validation tools. |
| JavaScript | Browser applications, page extraction, drawing tools, interactive interfaces, games, and Node.js scripts. |
| TypeScript | Application development, typed interfaces, Discord integration tools, and larger React-based projects. |
| HTML and CSS | Websites, application interfaces, printable documents, page templates, and media compositions. |
| SQL and PostgreSQL | Structured application records and database-backed workflows, particularly in Job Brain. |
| PowerShell | Local orchestration, file operations, drawing exports, printer checks, and Windows automation. |
| AutoLISP | AutoCAD automation, including identifying drawing layouts for background export. |
| JSON, CSV, and Markdown | Application data, record exchange, configuration, readable working history, and reusable workflow instructions. |

### Python for Research and Information Processing

Python has been useful for connecting information collection with preparation and output.

The research tools have included **BeautifulSoup** for processing HTML, **Playwright** for browser interaction, and **Crawl4AI** in a website-crawling implementation. These performed different parts of the collection work: navigating pages, obtaining page content, extracting text, and following links within a defined scope.

**Pydantic** supplied structured models in a business-information collector. The **OpenAI Python SDK** connected prepared records with language-model processing. **Rich** provided progress reporting and readable terminal output during collection and processing runs.

Supporting scripts used Python's standard libraries for JSON and CSV handling, paths, regular expressions, timestamps, and file organization. Focused utilities selected fields, consolidated nested information, compared collected lists, and organized individual records.

The result was a collection of tools with defined responsibilities. Collection, preparation, model processing, and presentation could be developed as separate operations with saved files connecting them.

Related records: [Developing AI-Assisted Business Research Tools: From Browser Automation to a Reference Library](../business-automation/PUB-0134-browser-automation-for-business-research.md) · [Using Python and the OpenAI API to Generate Structured Business Content](../business-automation/PUB-0135-python-openai-structured-business-content.md).

### Web Applications and Frontend Development

Some applications use plain HTML, CSS, and JavaScript. Others use **React**, **Next.js**, and **TypeScript**, depending on their interface, data, and application requirements.

The Railing Generator illustrates the lighter approach. Its browser interface uses JavaScript and drawing libraries to turn measurements and configuration into geometry and exports. A shared command-line path also supports working with project files and generating drawing outputs locally.

Job Brain used a larger application stack: Next.js, React, TypeScript, hosted authentication, database records, storage, and AI-backed interactions. The architectural client-intake project also developed through versions using browser JavaScript and a later React/Next.js implementation.

**Tailwind CSS** appears in several React-based application projects. **Zod** is used in typed application and integration code, including the Discord tool layer. **Node.js** supports local build scripts, command-line utilities, application tooling, and bot services.

Related records: [Railing Generator](../applications/railing-generator/overview.md) · [Building an Architectural Client Intake Application](../applications/client-intake/overview.md) · [Job Brain: Finding a Simpler Way to Organize My Business](../applications/job-brain/overview.md).

### AI APIs, Application Data, and Hosted Services

The **OpenAI APIs** have supported generated summaries, application responses, and voice-related work. **The Vercel AI SDK** formed part of Job Brain's request-and-response implementation.

In Job Brain, **Supabase** provided authentication, a **PostgreSQL** database, and file storage. The application worked with original notes, jobs, entities, extracted information, and retrieval structures. Its search work combined text matching with embeddings.

That project also informed my use of lighter systems. My business workflow developed around Obsidian, Markdown, reusable skills, and scripts, with hosted AI services supporting the tasks that benefit from them. A dedicated application database remains useful for some projects; readable local records fit others.

Related records: [Job Brain: Finding a Simpler Way to Organize My Business](../applications/job-brain/overview.md) · [Using Python and the OpenAI API to Generate Structured Business Content](../business-automation/PUB-0135-python-openai-structured-business-content.md).

### Hosting, Deployment, and Local Servers

The projects have used several hosting environments, each for a particular purpose.

| Environment | Project use |
|---|---|
| **Vercel** | Personal website deployment and playable browser-game builds, including Blackout and Exfiltrate. |
| **Railway** | A separately hosted Discord moderation worker. |
| **Supabase** | Hosted authentication, PostgreSQL, and application storage in database-backed projects. |
| **IONOS** | Static-site publishing for the counter-UAS research website, with staged file transfers and release verification. |
| **Spaceship hosting and cPanel** | Publishing and restoring the construction-business website. |
| **Local Node.js and Python processes** | Development previews, research tools, build steps, document production, and local integrations. |

Cloudflare has also formed part of the website delivery environment, including cache handling during research-site releases. Some application projects contain Cloudflare-oriented development tooling such as Wrangler and Vinext; the deployment destination is established separately for each project.

The hosting workflow includes preparing the intended files, checking the build, preserving a release history, and verifying the published output. Local development and a live release remain separate states.

Related records: [Developing a Counter-UAS Research Catalog](../research/PUB-0113-developing-a-counter-uas-research-catalog.md).

### Discord Communities, Bots, and MCP Integrations

Discord has served as a community environment and a destination for publishing updates. The Reasoning on Site community includes discussion spaces, project sharing, and show content, supported by channel organization, permissions, and moderation workflows.

The integration work uses **Node.js**, **TypeScript**, **discord.js**, the **Model Context Protocol SDK**, and **Zod**. MCP provides a tool interface through which an AI client can interact with supported operations. The Discord projects draw on existing open-source components alongside configuration and adaptation for the workflow.

Community administration and moderation have separate responsibilities. Administration tools support structured operations, while a separately hosted moderation worker handles its own tasks. Episode and publication workflows retain message references so later changes can update an existing announcement.

A Discord community server, a local MCP server process, and a cloud-hosted worker are different parts of that arrangement. Together, they connect the community's organization with the software used to maintain it.

Related records: [How I Automate Reasoning on Site](../workflows/PUB-0077-podcast-production.md).

### Drawing, Geometry, and Document Production

**AutoCAD** remains central to my drafting work. Automation around it includes **AutoCAD LT Core Console**, **AutoLISP**, and **PowerShell** for background drawing export and PDF preparation.

The Railing Generator uses **Maker.js** for model generation and SVG/DXF output, with supporting libraries including **opentype.js** and **bezier-js**. Project JSON provides an editable record of the inputs and configuration used to produce the drawings.

Business-document work uses HTML and CSS for editable layouts and print styling, with browser-based PDF output where appropriate. **ReportLab** provides a Python route for programmatic document generation, including estimates and invoices. PDF-processing tools such as **pypdf** support page assembly and related document operations.

**QGIS** has supported a separate site-documentation project, combining available mapping and survey information into an informal planning document. It added a geospatial tool to the broader drawing and information-processing workflow.

These tools connect the technical system to practical deliverables: drawings, PDFs, client documents, and supporting project information.

Related records: [Preparing Drawing PDFs and Printed Documents Through Codex Remote](../workflows/PUB-0111-remote-drawing-export-and-printing.md) · [Designing Business Documents with Code: A Flexible System for Estimates, Invoices, and Contracts](../workflows/PUB-0128-code-driven-business-documents.md) · [Open-Source PDF Tools in an AutoCAD Workflow](../workflows/PUB-0020-pdf-tools-for-autocad.md).

### Games, Interactive Graphics, and Spatial Media

Game and visualization projects have provided a setting for working with interactive systems, rendering, movement, and interface design.

**Three.js** and **React Three Fiber** appear in the Mech Division work, alongside **Rapier** physics. Blackout used browser JavaScript and **PeerJS** for its multiplayer connection layer. Other browser-game work explored visual effects, lighting, controls, and interacting systems.

The 3D reconstruction workflow uses **FFmpeg** for video inspection and frame preparation, **COLMAP** for camera reconstruction, and **Brush** for Gaussian-splat training. **SplatTransform** and **SuperSplat Viewer** support delivery conversion and browser presentation.

Related records: [Mech Division: An Early Experiment in Automated Game Development](../applications/mech-division/overview.md) · [Building Blackout: A Cooperative Game with Two Different Views](../applications/blackout/overview.md) · [Developing Exfiltrate: Remote Drones, Salvage, and Interacting Station Systems](../applications/exfiltrate/overview.md) · [Automating Gaussian Splats from Phone Capture to Production](../workflows/PUB-0027-phone-to-gaussian-splat.md).

### Audio, Video, and Creative Production

The Reasoning on Site production workflow uses **Faster Whisper** for local transcription and **FFmpeg** for audio assembly, processing, and exports.

Illustrated short-video production uses **HyperFrames** with **GSAP** for timeline-driven animation and **Three.js** for artwork effects. Python prepares inputs and supporting records. **NumPy** and **Pillow** support image processing and measured visual blockouts used in illustration planning.

My broader audio and video background also includes **Audacity** and **DaVinci Resolve**. Both remain part of the software available in my current environment, alongside Blender. Their use extends back into earlier creative work, before the present podcast-production workflow.

Related records: [How I Automate Reasoning on Site](../workflows/PUB-0077-podcast-production.md) · [Musical Background and Production](../background/music.md).

### Testing, Validation, and Reusable Procedures

Testing tools include **Playwright** for browser checks and automated application scenarios, Python's **unittest** for focused script checks, and **ESLint** in JavaScript and TypeScript projects.

The checks vary with the output. A drawing requires geometry and export review. A document requires content and page-layout inspection. A website requires working routes, source links, metadata, and deployment checks. A media export requires examination of the finished audio or video.

Reusable skills capture how those operations should be performed: the required inputs, source records, processing steps, validation, and destination. Obsidian holds the readable working context, while scripts carry out defined operations. Dropbox and GitHub support synchronization, backup, and version history in their respective parts of the workflow.

The technical stack therefore includes the instructions and records connecting the tools. Those connections make it possible to reuse a process, inspect its output, and improve it through subsequent work.


## Earlier Generations — Web, Design, and Game Development

Earlier portfolio and resume material, including versions from 2020–2024, records a digital practice already spanning websites, games, visual design, modeling, and media production.

The web stack included **HTML, CSS, JavaScript, PHP, jQuery, and MySQL**, with **Notepad++** among the editing tools and **FileZilla** for file transfer. The work involved page structure, styling, browser behavior, server-side scripting, and some database work.

Game-development tools included **3D Game Studio**, **RPG Maker**, **Unity**, and **Construct**, alongside HTML5 and JavaScript prototypes. These represented different ways to build interactive behavior, from engine-based development to browser implementations. The older project history includes game prototypes from 2005 onward and an earlier Exfiltrate prototype recorded in 2020.

**Blender** formed part of the 3D toolset, while **Alibre Design** appears in the earlier modeling and design background. These sit alongside the drafting and physical-prototyping interests that later connected with browser geometry tools and reconstruction workflows.

The creative software included **Adobe Illustrator**, **Adobe Photoshop**, **Dreamweaver**, **Paint Shop Pro**, **Audacity**, and **DaVinci Resolve**. The tools covered vector graphics, image editing, web authoring, audio editing, and video work. These tools entered the work at different times and continued across overlapping projects.

### Graphics and Web Authoring

Illustrator and Photoshop were part of the earlier design toolset. Vector graphics and image editing supported the visual side of the work alongside code, layout, and interactive development.

Dreamweaver added a dedicated web-authoring environment to the simpler text editors. That history is relevant to the way I work now: page structure, CSS, images, and the rendered result were already connected parts of building something for the browser.

### Games and 3D Development

The earlier game work included 3D Game Studio and Blender, followed across different projects by other engines and browser-based approaches. It provided a sustained setting for working through movement, interaction, visual presentation, and game behavior.

## Songwriting and Music Production — 2005–2010 and Later Production Work

Between 2005 and 2010, I wrote approximately 150 songs. Recording and production were an important part of that musical work, with the setup developing from a physical multitrack recording device toward a more software-based environment.

**Cubase** was part of that progression. Over time, the software I used included **Cubase 5 and Cubase 7**, alongside **Native Instruments** sound libraries and production packages. These tools were central to my songwriting and digital music-production background, providing a working environment for developing arrangements and shaping the recorded result.

The progression connected live instrumental performance and physical recording equipment with a broader electronic production setup. Cubase provided the central software environment, while the Native Instruments collection expanded the available sounds and instrumentation.

From approximately 2016 to 2018, I also worked in a pro bono music-production role for a local organization. That assignment extended the recording and production experience developed through my own musical work.

Related records: [Musical Background and Production](../background/music.md).

## Around 2005 Onward — Early Web Development and Text-Based Tools

My early web work began with **HTML and CSS**. **Notepad**, followed by **Notepad++**, provided a direct way to edit the files and examine the result in a browser.

The stack expanded into **JavaScript**, then **PHP** and a smaller amount of **MySQL** work. That introduced browser-side interaction, server-side behavior, and storing information beyond a static page.

The working process was hands-on: edit source files, open or refresh the page, inspect the behavior, and make the next adjustment. Dreamweaver and the graphics tools became part of that broader web and creative background as it developed.

Game development also dates to around 2005. The preserved project history includes an early split-screen game from that year and later prototypes using different engines and browser technologies.

These earlier projects establish the foundation behind the present toolset. AI-assisted development expanded how I could build and connect software, drawing on an existing history of web development, interactive projects, visual tools, and digital production.
