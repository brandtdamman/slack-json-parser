# Slack JSON Parser
### Table of Contents

- About
- Usage
- License


## About

The Slack JSON Parser is a multi-function parsing tool that automates various tasks for exported workspaces.  Generall, the workspace exports from Slack are difficult to parse by glancing eye and would benefit from rerepresentation or reduction of manual labour.  This project was born due to the lack of "download all attachments" option when exporting Slack workspaces.  Instead of actual files, links are given.

This program should work with private messages, so long as they were exported.  No official testing of this has occurred to date.

## Usage

Slack JSON Parser can be used as the following:

- [Coming Soon] Download All Files in Messages
- [Coming Soon] Textify All Channel Messages

### Installation

The program can be compiled/installed by building the C program file `src/main.c` to `slackjp`.

### Running

Sample usage of Slack JSON Parser for downloading all attached files:

```text
./slackjp -d -R /path/to/root/dir
```

## License

Follows GNU Affero General Public License v3.0.  See LICENSE file for details.