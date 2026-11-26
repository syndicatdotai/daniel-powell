# Using a fresh context for contract revisions

## LinkedIn Summary

One practical lesson I've learned using AI on contracts: a long revision thread can get confusing.

A lot of my contracts are created while I'm on the road using remote voice Codex. That works well for getting a first draft or a targeted change into the workflow, but repeated revisions to finely worded language can leave several versions and instructions mixed together.

You can have the current clause, an earlier clause, and several instructions that differ by a few words all sitting in the same context window. At that point, the model may blend versions or carry forward wording you thought you removed.

When that happens, I start a new chat with the current document, the rules that still apply, and one exact change request. It gives the revision a more limited set of inputs to work from.

I still compare the output against the source document. Contracts need human review, and sometimes legal review. The AI is helping with drafting and diffing, not deciding what the contract means.

#AI #Codex #ConstructionTechnology #Contracts

## Overview

Many of Daniel's contracts are created while he is on the road using remote voice Codex. That works well for getting a first pass or a targeted change into the workflow, but repeated revisions to a finely worded contract can leave several versions and instructions mixed together. The conversation may contain the original language, several edited versions, instructions that were later replaced, and new requests that differ by only a few words. At some point, the task is no longer just editing the contract. It is also asking the model to determine which version and which instruction should control.

When the thread starts to feel confused, start a new chat using the current document, the rules that still apply, and one clearly stated change request. That gives the revision a more limited set of inputs to work from.

## Role

Daniel decides which document is current, which terms and instructions remain active, and what the requested revision is supposed to accomplish. He compares the result against the current source and decides whether the wording is acceptable or needs legal review.

Remote voice Codex helps Daniel capture drafting instructions while he is away from the desk. Codex can then rewrite, compare, summarize, and identify changes. It can also help prepare a short handoff for a new chat. It is not the source of truth for the contract and does not decide whether the document is legally sufficient.

## Scope Of Work

This workflow covers remote voice capture and AI-assisted revision of construction contracts and other finely worded documents where small language changes matter. It focuses on managing conversational context, isolating the active version, and making revisions easier to compare.

It does not provide legal advice, determine enforceability, approve a contract, replace an attorney, or guarantee that a new chat will produce a better draft.

## Key Actions

- Notice when the conversation contains too many similar versions or repeated corrections.
- Use remote voice Codex to capture a first draft or targeted revision when working away from the desk.
- Save or identify the current document before starting another revision.
- Open a fresh chat when the accumulated thread is making the active wording unclear.
- Provide the current document, the rules that still matter, and the exact requested change.
- Ask for a focused revision or a change list rather than another free-form rewrite.
- Compare the result against the current document and check that removed language is actually gone.
- Send consequential contract language for the appropriate human or legal review.

## Important Features

- **Remote voice capture:** voice input can move drafting work into the workflow while Daniel is on the road.
- **New revision thread:** a separate chat can limit the active inputs to the current document and instructions that still apply.
- **Current-document handoff:** the active contract is supplied again instead of relying on conversational memory.
- **Instruction cleanup:** only the rules that still apply are carried forward.
- **Change isolation:** one revision request is easier to inspect than a long chain of loosely related edits.
- **Version comparison:** the result is checked against the current source rather than accepted because it sounds fluent.
- **Human control:** the person responsible for the document decides whether the revision is usable and whether legal review is required.

## Constraints And Decisions

- A larger context window does not mean that every detail in the context will be used equally well. Liu et al. found position-sensitive performance in controlled long-context retrieval and question-answering tasks, including weaker performance when relevant information appeared in the middle of the input.
- Voice capture improves access to the workflow but does not remove the need to identify the current source document and active instructions.
- That research is useful caution, not a contract-editing benchmark. The public claim here is based primarily on Daniel's workflow observation.
- A new chat is not automatically isolated. Project files, instructions, or other context may still be available depending on the tool and workspace configuration.
- AI may preserve obsolete wording, omit a requested change, introduce a new error, or misunderstand which version controls.
- The current contract document remains the source of truth until a person accepts a reviewed revision.
- Contract language can carry legal consequences and may require attorney review.

## Deliverables

- The current document or clearly identified source version.
- A voice-captured or typed revision request with enough context to identify the intended change.
- A short handoff stating the goal, active rules, current state, and requested change.
- A focused revised draft or proposed change set.
- A comparison against the current document.
- A list of unresolved questions or language requiring human or legal review.

## Outcome

The useful tactic is to notice when the thread contains too many near-duplicate versions and start again from the current document. That makes the revision easier to inspect while keeping drafting accessible from the road.

A narrower revision pass is easier to inspect, especially when the requested changes are small and the earlier versions are very similar. Responsibility for the contract still stays with the person reviewing it.

## Tools And Methods

The workflow uses remote voice Codex for mobile capture, the current contract document, a concise handoff prompt, and a comparison or diff-oriented review. A useful handoff states the goal, source document, active rules, current state, expected output, and anything the new chat must not change.

The technical caution is informed by [Liu et al., *Lost in the Middle: How Language Models Use Long Contexts*](https://aclanthology.org/2024.tacl-1.9/), which studied long-context retrieval and question answering. The context-management distinction is also consistent with [OpenAI's Projects documentation](https://help.openai.com/en/articles/10169521-projects-in-chatgpt), which describes chats, files, and project instructions as sources of context.

## Evidence And Limitations

This record combines Daniel's direct observation from repeated contract revisions with the private Context Transfer and Chat Handoff and contract-workflow notes. The academic research supports the narrower point that long inputs can be used unevenly; it does not prove that every model will mishandle a contract revision or that starting a new chat will always improve the result.

The public record contains no contract text, client information, project identifiers, legal conclusion, or claim of completed legal review. The workflow is a practical context-management tactic, not a substitute for document control, professional judgment, or legal advice.
