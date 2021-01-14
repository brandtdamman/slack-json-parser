# Slack JSON Parser
### Table of Contents

- About
- Usage
- License


## About

The Slack JSON Parser (commonly shortened to SlackJP) is a multi-function parsing tool born from the lack of "download all attachments" option when exporting Slack workspaces.
Generally, the workspace exports from Slack are difficult to parse by glancing eye.
Additinoally, various bookkeeping tasks for exported workspaces, such as conversion to non-JSON format, downloading (specific) files, and so forth are non-trival tasks.
By incorporating 

This program should work with private messages, so long as they were exported.  No official testing of this has occurred to date.

## Usage

Slack JSON Parser can be used as the following:

- Download all files
- Download specific files by filetypes
- [Partially Implemented] Write all links to file
- [Coming Soon] Export JSON to text files
- [Coming Soon] Export JSON to HTML

### Compilation

#### Python

Setup a virtual environment for Python 3.9+ and use the included [requirements.txt](requirements.txt).
From there, simply run the following command:

```text
pyinstaller -F ./src/python/slackjp.py
```

#### C

Presently, the C version of SlackJP is still underdevelopment and cannot function to the same capacity as the Python version.
As such, consider its functionality to be experimental.

The program can be compiled/installed by building the C program file [src/c/slackjp.c](src/c/slackjp.c) to `slackjp` (or desired executable name).
Below is a sample compilation command:

```text
gcc -pthread -o slackjp slackjp.c commands.c exception.c
```

For simplier compliation, a Makefile has been included in root directory, which will also install the TROFF page (in the near future).

### Running

Sample usage of Slack JSON Parser for downloading all attached files:

```text
./slackjp -d -R /path/to/root/dir
```

Several switches and functionality are readable via the [TROFF page](docs/slackjp.1).

## License

Follows [GNU Affero General Public License v3.0](https://www.gnu.org/licenses/agpl-3.0.html).
See [LICENSE](LICENSE) file for details.
