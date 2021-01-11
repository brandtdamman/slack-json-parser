import argparse

# Written by Brandt Damman
_verNumber = '0.2.6'

class SlackJPArgs:
    """Defines the CLI argument parser for SlackJP.
    """

    def __init__(self):
        """ Initialize the argparse variable.
        """
        global _verNumber

        # Argument Parser Setup
        self._parser = argparse.ArgumentParser(description='Slack JSON Parser', epilog='Further \
            information can be found via "man slackjp".', add_help=False)

        required = self._parser.add_argument_group('Required')
        required.add_argument('directory', type=str, help='Root directory of JSON files')

        general = self._parser.add_argument_group('General Options')
        general.add_argument('-h', '--help', action='help', help='Prints this help screen')
        general.add_argument('-R', '--recurse', action='store_true', help='Tells SlackJP to \
            recursively traverse from the root directory.')
        general.add_argument('-F', '--filetype', type=str, nargs='+', help='Download only \
            specified filetypes (requires -d or -l).')
        general.add_argument('-f', '--force', action='store_true', help='Forces all prompts \
            without regard.')
        general.add_argument('--version', action='version', version='%(prog)s ' + _verNumber)

        behavior = self._parser.add_mutually_exclusive_group(required=True)
        behavior.add_argument('-d', '--downOutput', type=str, help='Download files \
            from Slack Workspace export and save to directory.')
        behavior.add_argument('-l', '--linkOutput', type=str, help='Find links from Slack \
            Workspace export and save to file.')
        behavior.add_argument('-t', '--textOutput', type=str, help='Turns all messages in a \
            channel into a text file.')
        behavior.add_argument('-p', '--htmlOutput', type=str, help='Parses messages in a \
            channel into an HTML file.')

    def get_args(self):
        """ Obtains the arguments from CLI.
        """
        return self._parser.parse_args()

if __name__ == "__main__":
    sjpArgs = SlackJPArgs()