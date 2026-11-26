# Using Obsidian, GitHub, and Dropbox for Notes and Project Files

## LinkedIn Summary

I've been using Obsidian since 2021 to keep my notes and project information organized. I also use GitHub to keep track of changes to my Markdown files.

Obsidian is where I keep my notes and project information. GitHub gives me a history of the changes, so I can look back at earlier versions rather than only having the latest copy.

I use Dropbox for syncing files across devices and as an additional backup layer. It's mainly where I keep my notes, working documents, and the outputs from the scripts I use.

I've had to be deliberate about keeping highly active development projects outside Dropbox. Node.js servers, their dependencies, and complicated scripting environments stay in separate local workspaces. The files those tools produce can then go back into the appropriate project folders.

I still want the finished document or output available across my devices. I just don't need Dropbox trying to sync everything happening inside an active development environment.

## Overview

I've used Obsidian for my notes since 2021. My setup also includes GitHub for version control and Dropbox for syncing files across devices and additional backup.

Obsidian, GitHub, and Dropbox serve different purposes in my setup. Obsidian is where I work with notes and project information. GitHub keeps a version history. Dropbox helps make files available across devices and provides an additional backup layer.

## Role

I maintain the notes and project records, decide what belongs in the synced folders, and separate active software development from the documents and outputs I want available across devices.

## Scope Of Work

The system includes Markdown notes, project information, working documents, and files produced by scripts. It also includes a boundary between those records and the active development environments that generate some of them.

## Key Actions

- Maintain notes and project information in Obsidian using Markdown files.
- Use GitHub to retain a history of changes to those files.
- Use Dropbox to sync notes, documents, and script outputs across devices.
- Keep highly active development projects and Node.js environments in separate local workspaces.
- Place the relevant outputs back into the appropriate project folders.

## Important Features

Markdown keeps the notes in a text format I can work with directly. GitHub adds the ability to inspect changes and refer to earlier committed versions rather than relying entirely on the latest file.

Dropbox handles another part of the workflow: access to the files across devices. The documents and outputs I need remain in the synced folders, even when the software that produced them runs elsewhere on the computer.

## Constraints And Decisions

I keep Node.js servers, dependency folders, and complicated scripting environments outside Dropbox. These highly active workspaces contain files that can change repeatedly while the software is running or being developed.

I want Dropbox focused on my notes, working files, and useful outputs. Keeping the development environment separate avoids asking it to sync all of that internal activity along with my project records.

Version control, syncing, and backup have different roles. GitHub records committed versions; Dropbox keeps copies synchronized. I use Dropbox as an additional backup layer, while recognizing that a synced edit or deletion can also propagate to other devices.

## Deliverables

- Markdown notes and project records maintained in Obsidian.
- Version history retained through GitHub.
- Notes, documents, and script outputs available through Dropbox syncing.
- Separate local workspaces for active development.

## Outcome

I can keep using Obsidian for my notes while maintaining a history of changes and accessing the relevant files across devices. The outputs of my scripts can sit with the project records without placing the entire development environment in the same synced folder.

## Tools And Methods

Obsidian for working with Markdown notes, GitHub for version control, Dropbox for syncing and additional backup, and separate local workspaces for Node.js and other active development environments.

## Evidence And Limitations

This describes how I organize my notes, version history, and synced files. It does not claim that every file is version controlled or that syncing alone is a complete backup strategy.
