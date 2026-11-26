# Updating my schedule remotely with a local calendar record

## LinkedIn Summary

I use Codex Remote from my phone to make changes to my schedule and Google Calendar while I'm out on the road.

My main schedule is stored locally on my computer, with a readable version in Markdown that stays in sync with Google Calendar. Codex can read the local schedule directly instead of having to reach out through the calendar connection every time.

That connection breaks from time to time. When it does, I still have my schedule on my computer and can keep updating it through Codex Remote. The Google Calendar updates can be applied once the connection is working again.

## Overview

I use Codex Remote from my mobile device to update my schedule while I'm away from my computer. The schedule is stored locally, presented in readable Markdown, and mirrored into Google Calendar.

Keeping the local record gives Codex access to the schedule even when the Google Calendar connection is unavailable.

## Role

I tell Codex what needs to change. Codex updates the local scheduling records and applies the corresponding Google Calendar changes through the calendar connection.

## Scope Of Work

The workflow covers reading the existing schedule and making changes such as adding work, moving dates, or updating scheduled commitments. The local scheduler holds the main record, while Google Calendar provides another place to view that schedule.

## Key Actions

- Send a scheduling request through Codex Remote from my phone.
- Have Codex read the existing local schedule for context.
- Update the local schedule and its readable Markdown views.
- Apply the corresponding Google Calendar changes and check the resulting events.

## Important Features

Codex can consult files on my computer without fetching the same schedule information through the Google Calendar connection for every request. The Markdown views also let me read the schedule as an ordinary document.

The local record remains available when the calendar connection breaks. A connection problem does not remove the schedule from my computer.

## Constraints And Decisions

The local scheduler is the authoritative record. Its underlying schedule data is stored in JSON, with Markdown views generated from those records. Google Calendar is synchronized from that local state.

If the calendar connection is unavailable, local changes can be preserved while the external updates remain pending. Google Calendar is only considered synchronized after the changes have been applied and the resulting events checked.

## Deliverables

- Updated local scheduling records.
- Readable Markdown schedule views.
- Corresponding Google Calendar updates when the connection is available.

## Outcome

I can make scheduling requests from my phone while I'm out working. Codex has the local schedule available to work from, and I retain access to that record during interruptions to the Google Calendar connection.

## Tools And Methods

Codex Remote provides access from my mobile device to the session working on my computer. The local scheduler maintains structured records and readable Markdown views. The Google Calendar synchronization workflow maps those records to calendar events and verifies external changes by reading the events back.

## Evidence And Limitations

This describes my existing workflow and its documented synchronization rules. It does not claim that Google Calendar remains current during a connection outage or that every event created separately in Google Calendar is automatically copied into the local scheduler.
