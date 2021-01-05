#   ######  ##          ###     ######  ##    ##          ##  ######   #######  ##    ##    ########     ###    ########   ######  ######## ########  
#  ##    ## ##         ## ##   ##    ## ##   ##           ## ##    ## ##     ## ###   ##    ##     ##   ## ##   ##     ## ##    ## ##       ##     ## 
#  ##       ##        ##   ##  ##       ##  ##            ## ##       ##     ## ####  ##    ##     ##  ##   ##  ##     ## ##       ##       ##     ## 
#   ######  ##       ##     ## ##       #####             ##  ######  ##     ## ## ## ##    ########  ##     ## ########   ######  ######   ########  
#        ## ##       ######### ##       ##  ##      ##    ##       ## ##     ## ##  ####    ##        ######### ##   ##         ## ##       ##   ##   
#  ##    ## ##       ##     ## ##    ## ##   ##     ##    ## ##    ## ##     ## ##   ###    ##        ##     ## ##    ##  ##    ## ##       ##    ##  
#   ######  ######## ##     ##  ######  ##    ##     ######   ######   #######  ##    ##    ##        ##     ## ##     ##  ######  ######## ##     ## 

# Written by Brandt Damman
_verNumber = '0.1.0'

import argparse
import os

# Argument Parser Setup
_parser = argparse.ArgumentParser(description='Slack JSON Parser', epilog='Further \
    information can be found via "man slackjp".')
_parser.add_argument('-d', action='store_true', help='Download attached files.')
#_parser.add_argument('-D', action='store_true', nargs='+', help='')

_parser.add_argument('--version', action='version', version='%(prog)s ' + _verNumber)

def find_files(RootLoc, RecurseSwitch):
    """Compiles a list of files to compile.  If no files are found, the program will
    exit.  Does not begin grabbing links from each file yet for exit behavior reasons.
    
    Arguments:
        RootLoc         --  the directory or file in which to begin scanning
        RecurseSwitch   --  denotes if the directories should be traversed

    Returns:
        list            --  list of file paths
    """
    list = []

    from collections import deque
    from sys import platform
    stack = deque()
    stack.append(RootLoc)

    # Traverse the file tree until all files have been found.
    while len(stack) is not 0:
        location = stack.pop()

        # Check if the given file path is a directory.
        if os.path.isdir(os.path.dirname(location)) and not os.path.isfile(location) :
            if RecurseSwitch:
                for subLocation in os.listdir(location):
                    # Check for platform slashing and append directory information.
                    if platform == "win32":
                        stack.append(location + '\\' + subLocation)
                    else:
                        stack.append(location + '/' + subLocation)
        # Location is not a directory so see if it matches .json filetype.
        elif location[-5:] == '.json':
            list.append(location)
        # Invalid filetype, place INFO or WARNING in log.
        else:
            pass # TODO: Impelement error logging.
    
    return list

def scan_links(FileList):
    """Scans each file present in given file list for specific JSON variables.

    Arguments:
        FileList    --  list of files to be scanned

    Returns:
        list        --  list of file download links
    """
    pass

def download_files(LinkList):
    """Downloads each file from the respective link.  Changes behavior based
    on OS as no single OS family is alike.

    Arguments:
        LinkList    --  list of file download links
    """
    pass

# Ensure this file is run directly.
if __name__ == "__main__":
    fileList = find_files(os.getcwd(), True)
    for file in fileList:
        print(file)