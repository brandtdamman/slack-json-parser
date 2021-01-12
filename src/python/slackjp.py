#   ######  ##          ###     ######  ##    ##           ##  ########  
#  ##    ## ##         ## ##   ##    ## ##   ##            ##  ##     ## 
#  ##       ##        ##   ##  ##       ##  ##             ##  ##     ## 
#   ######  ##       ##     ## ##       #####              ##  ########  
#        ## ##       ######### ##       ##  ##       ##    ##  ##        
#  ##    ## ##       ##     ## ##    ## ##   ##      ##    ##  ##        
#   ######  ######## ##     ##  ######  ##    ##      ######   ##        

# Written by Brandt Damman
from slackargparser import SlackJPArgs
import os

_parser = SlackJPArgs()

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

    # See if-statement.
    singleRecurse = False

    # If primary location is a directory, one "recurse" is needed.
    if os.path.isdir(os.path.dirname(RootLoc)) and not os.path.isfile(RootLoc):
        singleRecurse = True

    # Traverse the file tree until all files have been found.
    while len(stack) != 0:
        location = stack.pop()

        # Check if the given file path is a directory.
        if os.path.isdir(os.path.dirname(location)) and not os.path.isfile(location):
            if RecurseSwitch or singleRecurse:
                # TODO: Find simple solution to fix assigning False every iteration.
                singleRecurse = False
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

def scan_links(FileList, LinkOnlySwitch):
    """Scans each file present in given file list for specific JSON variables.

    There are two primary items in Slack Export JSON files:
        - "filetype"
        - "url_private_download"
    Only the second variable is necessary for processing.  While it is more than
    possible to utilize "filetype", the parsing performed makes this ultimately
    unnecessary.

    Arguments:
        FileList        --  list of files to be scanned
        LinkOnlySwitch  --  determines if links are the only thing grabbed

    Returns:
        list        --  list of file download links
    """
    list = []

    for filename in FileList:
        try:
            file = open(filename, mode='r+', encoding='UTF-8')
            reader = file.readlines()
            file.close()
        except Exception:
            # TODO: Change exception type.
            # TODO: Use centralized error logging.
            print(f"File {filename} was unable to be opened.")

        # File Object -> Link, File Name, & File Type
        tokenIndex = None
        downloadIndex = None
        link = None
        filetype = None
        filename = None

        # TODO: Remove these god-awful magic numbers.
        # Now read from file.
        for line in reader:
            line = line.strip()
            if line[:6] == '"filet' and not LinkOnlySwitch:
                # Found file type, now store.
                filetype = line[13:line.find('"',13)]
            elif line[:13] == '"url_private_':
                # Found download link, store and reset.
                tokenIndex = line.find("?t=")
                if downloadIndex is None:
                    # This should only be done once.
                    downloadIndex = line.find("download\\/") + 10

                # Grab the link, then the file name.
                link = line[25:-2]
                if not LinkOnlySwitch:
                    filename = line[downloadIndex:tokenIndex]
                
                list.append((link, filename, filetype))

    return list

def prompt_file():
    """Prompts the user if an output file already exists.
    """
    return None

def download_files(LinkList, FileTypes, OutputFile, LinkOnlySwitch):
    """Downloads each file from the respective link.  Changes behavior based
    on OS as no single OS family is alike.

    Arguments:
        LinkList        --  list of file download links (link, file name, file type)
        FileTypes       --  dictionary of allowed file types
        OutputFile      --  location of output file, if applicable
    """
    #   The following method cannot be finished due to a lack of understanding
    # Slack App API.  There will be a way to resolve this in the future; however
    # now is not the appropriate time.

    # Select output.  If not given, use default.
    if not OutputFile:
        from datetime import datetime
        OutputFile = os.getcwd() + '/slackjp-output-' + datetime.now().strftime("%d-%B-%Y-%H-%M-%S") + '.txt'

    # Prompt user if overwriting is desired.
    writeFlag = 'w'
    if os.path.isfile(OutputFile):
        print(f"Do you want to override file ({OutputFile})?")
        ans = input("[O]verwrite, [A]ppend, or [Q]uit (Default is overwrite)")
        
        # Needs a better solution.
        if ans == 'a' or ans == 'A':
            writeFlag = 'a'
        elif ans == 'Q' or ans == 'q':
            # TODO: Exit out of program ASAP.
            return

    writer = open(OutputFile, mode=writeFlag, encoding='UTF-8')

    for fUrl in LinkList:
        # If there are no specified file types, skip check.
        if FileTypes is None or FileTypes.get(fUrl[2], False):
            writer.write(fUrl[0].replace("\\", ""))
            writer.write("\n")

    writer.close()

##
#   Primary TODO List
##
# TODO: Add exit codes from man page
# TODO: Clean up file and possibly split
# TODO: Centralized error handling

# Ensure this file is run directly.
if __name__ == "__main__":
    
    args = _parser.get_args()

    if args.directory == ".":
        fileList = find_files(os.getcwd(), args.recurse)
    else:
        fileList = find_files(args.directory, args.recurse)

    linkList = scan_links(fileList, args.linkOutput is not None)

    # Manage possible functions.
    if args.linkOutput:
        write_links(linkList, args.linkOutput)
    elif args.downOutput:
        download_files(linkList, args.filetype, args.downOutput, False)
    elif args.textOutput:
        pass
    elif args.htmlOutput:
        pass

    download_files(linkList, args.filetype, args.output, True)

    # Replace with error codes if necessary.
    print("All operations completed.")
