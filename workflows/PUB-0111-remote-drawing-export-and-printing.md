# Preparing Drawing PDFs and Printed Documents Through Codex Remote

## LinkedIn Summary

I’ve used Codex Remote to finish documents and have them printed at the office while I’m on my way back for a meeting.

I give it instructions through hands free voice chat from my phone. We work through the wording, it prepares the documents on my computer, and I tell it to print them. When I get to the office, I can grab the papers and leave for the appointment.

I built a printing skill so Codex has a repeatable way to choose the physical printer, submit the document, and check the print queue. That means the printing step is available through the same remote connection I’m already using for the work.

I also developed a background export workflow for AutoCAD. Codex can take a saved drawing, identify its layouts, and export the requested sheet to PDF using AutoCAD’s own plotting tools. The drawing’s page setup carries through to the PDF, including the configured sheet size.

Those are two parts of the document workflow I can direct from my phone. The AutoCAD export prepares a drawing PDF. The printing skill handles an existing file that’s ready to print.

I’ve used remote printing under time pressure when I needed paperwork for an appointment. The documents were being finished during the journey, and they were printed by the time I returned to collect them.

## Overview

Remote document work extends from preparation through to a file or printed package. Two reusable workflows provide that connection on my office computer: background AutoCAD PDF exports and local document printing.

An urgent meeting provided a practical use for remote printing. Hands-free voice instructions through Codex Remote kept document preparation moving during the return journey. The papers were printed at the office, ready to collect before leaving for the appointment.

## Role

I developed the export workflow and printing skill around the tools used in my drafting and business administration. The work included establishing the export procedure, capturing the working settings in scripts and instructions, and defining how Codex selects and checks a physical printer.

## Scope Of Work

The AutoCAD workflow takes a saved DWG and a selected layout and produces a PDF. The printing workflow takes a prepared document and sends it to a local printer. Each can be directed through Codex Remote from a phone.

These operations also serve separate requests. A drawing export can prepare a file for review or distribution, while a print request can use an existing meeting document, invoice, contract, or other prepared file.

## Key Actions

AutoCAD LT Core Console runs the drawing export in the background. A PowerShell wrapper prepares a copy of the source drawing, and AutoLISP identifies its stored layouts. The plot sequence then exports the requested layout.

The printing skill identifies available devices, selects the appropriate physical printer, submits the prepared file, and checks Windows printer and queue status. Document creation and revision happen before the file enters that procedure.

## Important Features

The export retains the drawing layout’s configured PDF plotter and media. Testing established the importance of those settings: substituting a generic PDF configuration changed the output sheet size. The working export was checked against the intended architectural page size.

Printer selection also needs to be explicit. The printing skill distinguishes physical devices from virtual PDF destinations and checks whether Windows reports the printer offline or in an error state.

## Constraints And Decisions

The export works from a copy of a saved drawing. The source file and layout are identified directly, and the operation retains its own working files and logs.

The printing procedure operates on the file prepared for the request. Queue status provides feedback about submission and progress. Collecting the printed pages confirms the physical result.

## Deliverables

The development produced a reusable AutoCAD export script and runbook, plus a local printing skill with supporting file-submission scripts. The resulting outputs are drawing PDFs and physical copies of prepared documents.

## Outcome

Remote printing has been used to prepare paperwork for meetings under time pressure. Voice instructions covered the remaining document work during the journey, and the printed package was ready to collect on arrival at the office.

The background export workflow makes drawing PDFs available through the same remote interface, extending the document operations that can be requested away from the computer.

## Tools And Methods

Codex Remote, hands-free voice input, AutoCAD LT Core Console, AutoLISP, PowerShell, PDF plotting, reusable skills, and Windows printer and queue checks.

## Evidence And Limitations

The export procedure is grounded in the documented working AutoCAD LT setup and its checked PDF output. The meeting and remote-printing account comes from direct use. Printer-status checks describe the signals available from Windows.

[Daniel Powell’s public archive](https://github.com/syndicatdotai/daniel-powell)
