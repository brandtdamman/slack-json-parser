#   ######  ##          ###     ######  ##    ##           ##  ########  
#  ##    ## ##         ## ##   ##    ## ##   ##            ##  ##     ## 
#  ##       ##        ##   ##  ##       ##  ##             ##  ##     ## 
#   ######  ##       ##     ## ##       #####              ##  ########  
#        ## ##       ######### ##       ##  ##       ##    ##  ##        
#  ##    ## ##       ##     ## ##    ## ##   ##      ##    ##  ##        
#   ######  ######## ##     ##  ######  ##    ##      ######   ##        

# Written by Brandt Damman
_verNumber = '0.1.1'

import argparse
import os

# Argument Parser Setup
_parser = argparse.ArgumentParser(description='Slack JSON Parser', epilog='Further \
    information can be found via "man slackjp".')
_parser.add_argument('-R', '--recurse', action='store_true', help='Tells SlackJP to \
    recursively traverse from the root directory.')
_parser.add_argument('-D', '--filetype', type=str, nargs='+', help='Download only \
    specified filetypes.')
_parser.add_argument('-o', '--output', type=str, nargs=1, help='Specify where the \
    the link list will be written.')
_parser.add_argument('directory', type=str, help='Root directory of JSON files')

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
    while len(stack) != 0:
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

    There are two primary items in Slack Export JSON files:
        - "filetype"
        - "url_private_download"
    Only the second variable is necessary for processing.  While it is more than
    possible to utilize "filetype", the parsing performed makes this ultimately
    unnecessary.

    Arguments:
        FileList    --  list of files to be scanned

    Returns:
        list        --  list of file download links
    """
    pass

def download_files(LinkList, FileTypes):
    """Downloads each file from the respective link.  Changes behavior based
    on OS as no single OS family is alike.

    Arguments:
        LinkList    --  list of file download links (link, file name, file type)
        FileTypes   --  dictionary of allowed file types
    """
    #   The following method cannot be finished due to a lack of understanding
    # Slack App API.  There will be a way to resolve this in the future; however
    # now is not the appropriate time.

    #import pip._vendor.requests
    for fUrl in LinkList:
        if FileTypes.get(fUrl[2], False):
            f
            pass

# Ensure this file is run directly.
if __name__ == "__main__":
    args = _parser.parse_args()
    # Prepare switch statements?
    fileList = find_files(os.getcwd(), args.recurse)
    linkList = scan_links(fileList)
    download_files(linkList, args.filetype, args.output)
