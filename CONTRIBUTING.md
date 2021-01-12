# Contributing to Slack JSON Parser

Welcome and thanks for considering to contribute to Slack JSON Parser (commonly reduced to SlackJP).
This document outlines some general guidelines related to how to best contribute to the project.
When you're ready to contribute towards the project, please feel free to prepare a pull request.

#### Contents

- [Code of Conduct](#code-of-conduct)
- [Coding Conventions](#coding-conventions)
- [Submitting Code](#submitting-code)
- [Remarks](#remarks)

## Code of Conduct

Information about this project's [Code of Conduct](.github/CODE_OF_CONDUCT.md) can be found in the [.github](.github/) folder.
Alternatively, a general purpose guideline can be found in [my personal repository](https://github.com/brandtdamman/brandtdamman).
As a relative guideline prior to skimming through it, play well with others, be respectful, and facilitate open discussion with open arms.

## Coding Conventions

The coding conventions set here should be fairly quick to become accustomed with after viewing code.
Below is a gist of the conventions used.
When in doubt, aim for readability.

### Python

- Function names use `underscore_naming`
- Funciton parameters are `CapitalCase`
- Local variables are `camelCase`
- Global variables start with an `_` and are `camelCase`
- Indentation uses four spaces and not tabs.

### C

- Function names use `underscore_naming`
- Function parameters and local variables use `camelCase`
- Macros use `ALL CAPS`
- Indentation is should be four spaces or a single tab
- Braces are on the same line as the function declaration
- All function prototypes must be declared in a header file

### Markdown

All sentences should be on a newline, where possible.
This allows for quick _git diff_ of files and easier reading.
Embedded images or links should remain self-isolated.
While many resources online are helpful and often necessary, summaries are more accepted.
If an external link is required, then an [Internet Archive Wayback Machine](https://web.archive.org) link must be included as a secondary source.
A Wayback link is waived if related to the purposes of license information or other repositories within GitHub.

## Submitting Code

### Commit Messages

- Keep the first commit line to 50 characters, plus or minus 10 characters
- Emojis are acceptable but generally not used

Make sure to reference any open issue or related documents, where applicable, on following lines.

### Pull Requests

Except in extreme cases, pull requests will generally be reviewed within a seven-day window.
Make sure to state all chances and reference any issues and related documents where necessary.

## Remarks

Thank you again and happy coding!

-> Brandt Damman
