# Developing Browser Automation with AI for Business Research

Business research often involves a repetitive sequence of actions: opening a listing, finding the relevant information, expanding additional details, recording the result, and moving to the next organization. When the research covers many businesses, the collection process becomes a significant part of the work.

I used ChatGPT and Cursor to develop custom tools for collecting and organizing public business information. The objective was to turn information spread across business listings and websites into structured records that could support research, comparison, written summaries, and web publishing.

This involved translating a research task into software: define the information needed, identify where it appeared, build a way to collect it, and save the results in a consistent format.

The development included JavaScript running directly inside an open browser and Python tools controlling a browser through Playwright. Each approach addressed a different level of complexity, from extracting visible results to managing a sequence of interactions and saving structured records.

## Defining the Information Before Automating the Browser

The work began with deciding what a useful business record needed to contain.

Depending on the project, that included the business name, category, website, operating hours, rating, and other publicly displayed information. Establishing those fields gave the automation a defined purpose and the later processing tools a consistent structure to work with.

The development problem was to translate information displayed through a website into records that software could process consistently. A useful collection tool needed to preserve the relationship between an organization and its information while preparing that information for the next stage of work.

That required attention to both the source interface and the intended output. Some information appeared in a search result. Other details required opening a business panel, expanding a section, or waiting for more content to load.

## Using JavaScript Inside an Open Browser

One approach used JavaScript executed through Chrome's developer console. This placed the script in the context of a page already open in the browser.

The simpler implementation collected basic information from the search results themselves. It identified listing elements, extracted the relevant text and links, and prepared a downloadable JSON file. For a defined collection task, this kept the tool close to the information being examined.

A more detailed implementation handled additional interactions, including opening business details and collecting information from expanded sections. Configuration settings controlled the collection limit and the amount of detail requested.

The larger script also included controls to pause, resume, check progress, and save collected results. Those controls made the collection process easier to supervise while it was running.

This was an accessible way to develop a focused tool around an existing browser session. The output could then move into separate processing steps rather than remaining as information scattered across open pages.

## Developing a Python and Playwright Implementation

The project also included a Python implementation using Playwright to control browser navigation and interaction.

That implementation brought the collection process into a local software environment with explicit configuration, structured data models, logging, and file output. The configuration included a starting position, a business limit, navigation timeouts, and a choice between a visible browser and background operation.

Visible operation provided a way to observe what the browser was doing. Background operation offered another execution mode for the same collection logic. Having both options made browser visibility a configuration decision within the tool.

The Python implementation used BeautifulSoup to process captured HTML and Pydantic models to define the shape of the business records. Together, these components connected browser interaction with structured data processing.

The browser performed the navigation. Parsing logic extracted information from the resulting page content. Data models organized the fields. File-writing routines preserved individual records and aggregate results in JSON.

## Handling the Details of an Interactive Website

A browser automation task involves more than repeating clicks.

The tools needed to identify the relevant page elements, wait for content, and account for differences in how information appeared. The Python code included alternative selectors for several fields, while the collection logic handled sections such as operating hours separately from the initial page information.

Those details shaped the development work. A useful result depended on selecting the correct information and preserving its meaning as it moved into a record.

Logging and progress reporting made the process inspectable. They recorded navigation, extracted fields, missing information, and errors, providing a way to examine where the workflow needed attention.

These were practical requirements for process improvement: understand what the tool did, identify where a problem occurred, and adjust the relevant part of the workflow.

## Keeping Collection Separate from Later Processing

Structured output made the collected information useful beyond the browser session.

The broader body of work included separate tools for data cleanup, comparison, summarization, and website generation. Saving records in JSON created a connection between those stages without requiring every operation to happen inside one script.

This separation also kept different responsibilities visible. Extraction preserved information from the source interface. Later processing could reorganize that information or prepare written summaries for a particular use.

The browser automation therefore became one component of a larger information-management workflow. Its job was to collect and save defined inputs in a form the next tool could use.

## Choosing an Approach Around the Task

The experiments produced several implementations with different levels of interaction and configuration.

A console script suited a focused task within a browser page already in use. A Python application provided more room for structured configuration, logging, validation, and organized file handling. The appropriate approach depended on the collection task and the surrounding workflow.

This is where the work connected software development with business operations. Defining the required information, the collection boundaries, the review process, and the output format was as important as generating the code.

ChatGPT and Cursor supported development of the tools. My contribution was shaping the task, determining what information mattered, and working through how the components should fit together.

## Applying Software Development to a Research Process

This work documents how I used AI-assisted development to build purpose-specific research tools. It brought together requirements definition, browser automation, data processing, and decisions about how information should move between stages.

The resulting work included browser-console scripts, a configurable Python collector, structured business records, and supporting processing tools. It developed experience turning a repetitive information-gathering process into a series of explicit software operations.

The methods have applications in areas such as supplier research, business prospecting, and collecting background information about organizations. Each presents a similar operational question: how should information be gathered, organized, reviewed, and prepared for use?

The central contribution was defining a repeatable research operation and building software around it: identify the information, choose an execution method, collect it into a consistent structure, and preserve it for the next stage of work.
