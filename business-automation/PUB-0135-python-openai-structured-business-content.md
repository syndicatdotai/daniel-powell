# Using Python and the OpenAI API to Generate Structured Business Content

A business reference resource needs several ways to present the same underlying information. A listing needs a short introduction. A detailed profile needs a fuller description. A question-and-answer section needs concise responses organized around the subjects readers are likely to ask about.

I used ChatGPT and Cursor to develop a Python workflow that sent prepared business records to the OpenAI API and saved the resulting content in structured files. The work connected collected source information with the written components used to assemble business profiles and related web content.

The objective was to make content preparation part of a repeatable software process. Instead of producing one block of prose at a time, the tool requested a defined set of related outputs and organized them for subsequent use.

## Starting with a Defined Source Record

The processing stage began with a compact JSON record containing collected business information and supporting material.

That record supplied the context for the writing task. It gave the model a defined input rather than an open-ended instruction to research and describe a business independently.

The script passed the complete compact record into the request. Collection and preparation happened in separate stages, leaving this tool responsible for turning the supplied information into a particular set of written outputs.

This separation made the information flow clear: source material entered the request, the model returned content, and Python prepared that response for storage and later processing.

## Defining the Content Before Generating It

The output requirements were established in advance.

The request included a short summary, longer descriptive sections, an article-style summary, question-and-answer items, and promotional text. Each component had a different role in the eventual presentation.

A brief introduction needed to communicate the subject quickly. A longer section had room to develop the description. FAQs required a question and an answer as separate values. Promotional text occupied its own field rather than being mixed into the main description.

The prompts included length guidance, tone instructions, paragraph-formatting requirements, and directions to avoid repeating distinctive language across sections. They also defined the subjects the FAQs should address.

Those choices made the request an editorial specification as well as a software operation. The intended use of each field shaped what the model was asked to produce.

## Requesting Several Related Outputs Together

The tool was designed to request the related content fields together from the same source record.

That put the short description, longer narrative, FAQs, and other components in a shared context. The request could specify how they should differ while keeping them connected to the same underlying information.

The implementation defined a JSON schema for the expected response. It described named text fields, arrays, and objects, including separate question-and-answer values. The request attempted schema-constrained output, with a plain-JSON request as a compatibility fallback.

The important design decision was the response contract. The surrounding software expected a collection of named components that it could retrieve and place separately.

This made the model response an input to another program, with a defined place for each part of the writing.

## Setting Boundaries for the Writing Task

The prompt instructed the model to use facts from the supplied record and supporting review text. It also directed the model to acknowledge information that was not provided rather than inventing business details.

That established the intended relationship between the source and the generated copy. The writing task was to organize and describe the supplied material.

Factual review remained a content decision. A response could contain all the requested fields and still require examination against its source. The workflow therefore involved two different questions: whether the response had the structure the software needed, and whether its statements accurately represented the available information.

Keeping those questions distinct is part of designing a useful AI processing stage. The prompt establishes the writing requirements; the output still needs to be understood in relation to the source.

## Processing the Response in Python

The script extracted the returned text, parsed it as JSON, and passed the resulting fields through local processing routines.

Those routines addressed formatting, placeholder text, repeated sentences, and the shape of lists such as FAQs. They also checked text lengths and expected item counts.

The implementation included local repair and fallback routines for incomplete responses. These operated separately from the model request, placing some output handling in ordinary Python rather than asking the model to perform every adjustment.

That division gave the workflow two kinds of instructions. The prompt described the writing task, while Python expressed mechanical processing rules. Changes to field formatting or file handling could be made in code; changes to the requested emphasis or tone belonged in the content instructions.

## Saving Content for the Next Stage

The processed response was saved as a separate JSON file associated with its source record.

Named fields made the output available to downstream tools. A publishing script could retrieve a short summary for one location and a longer description or FAQ list for another.

Saving the generated content also separated generation from presentation. The model produced the written components, while later tools handled where those components appeared in the reference resource.

This created an inspectable intermediate output between the API request and a rendered page. The collected record and generated content remained separate files with different roles in the workflow.

## Supporting Batch Processing and Targeted Rewrites

The tool included a watch mode that looked for prepared records without corresponding summary files. It processed pending inputs in bounded groups, then checked for additional work.

Configuration controlled the processing limit, polling interval, and idle shutdown. An expected-total setting provided another completion condition for a defined collection.

A separate rewrite mode selected a configured number of source records and regenerated their associated summaries. That provided a way to revisit outputs when the content instructions changed.

These controls extended the work beyond an isolated API request. They addressed how the processing stage would discover inputs, identify existing outputs, limit a run, and revisit selected material.

## Connecting Editorial Decisions with Software Development

My contribution involved defining both the content requirements and the surrounding workflow: what information the model received, what fields it returned, how the response was processed, and how another tool would use the saved result.

ChatGPT and Cursor supported development of the Python implementation. The OpenAI API supplied the language-model processing inside that implementation.

The work developed practical experience with prompt design, structured output requirements, local post-processing, batch execution, and content organization. It connected AI implementation with a specific business-information publishing need.

The same design questions apply to other content workflows: define the source, establish the required outputs, separate writing instructions from mechanical processing, and preserve an intermediate result that can be reviewed and reused.
