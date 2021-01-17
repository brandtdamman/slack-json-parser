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
from collections import namedtuple

FileInformation = namedtuple('FileInformation', ['name', 'type', 'link', 'folder'])
_parser = SlackJPArgs()

def find_files(RootLoc: str, RecurseSwitch) -> list:
    """Compiles a list of files to compile.  If no files are found, the program will
    exit.  Does not begin grabbing links from each file yet for exit behavior reasons.
    
    Arguments:
        RootLoc         --  the directory or file in which to begin scanning
        RecurseSwitch   --  denotes if the directories should be traversed

    Returns:
        fileList        --  list of file paths
    """
    fileList: list = []

    from collections import deque
    from sys import platform
    stack = deque()
    stack.append(RootLoc)

    counter: int = 1
    # See if-statement.
    singleRecurse: bool = False

    # If primary location is a directory, one "recurse" is needed.
    if is_directory(RootLoc):
        singleRecurse = True

    # Traverse the file tree until all files have been found.
    while len(stack) != 0:
        location = stack.pop()

        # Check if the given file path is a directory.
        if is_directory(location):
            if RecurseSwitch or singleRecurse:
                # TODO: Find simple solution to fix assigning False every iteration.
                singleRecurse = False
                for subLocation in os.listdir(location):
                    # Check for platform slashing and append directory information.
                    # TODO: Reduce runtime by moving this out of the while loop.
                    if platform == "win32":
                        stack.append(location + '\\' + subLocation)
                    else:
                        stack.append(location + '/' + subLocation)
        # Location is not a directory so see if it matches .json filetype.
        elif location[-5:] == '.json':
            fileList.append(location)
            print(f"Files found\t-----\t{counter}", end='\r', flush=True)
            counter += 1
        else:
            # Invalid filetype, place INFO or WARNING in log.
            # TODO: Impelement error logging for invalid filetype
            pass 
    
    print('\n', end='')
    return fileList

def is_directory(Location: str) -> bool:
    """Performs a check to see if the given file location is a directory and NOT file.

    Arguments:
        Location        --  file location in string format

    Returns:
        true if location is a directory, otherwise false
    """
    return os.path.isdir(os.path.dirname(Location)) and not os.path.isfile(Location) 

def scan_links(FileList: list, LocationIndex: int, LinkOnlySwitch) -> (list, dict):
    """Scans each file present in given file list for specific JSON variables.

    There are two primary items in Slack Export JSON files:
        - "filetype"
        - "url_private_download"
    Only the second variable is necessary for processing.  While it is more than
    possible to utilize "filetype", the parsing performed makes this ultimately
    unnecessary.

    Arguments:
        FileList            --  list of files to be scanned
        LocationIndex       --  index where folder information becomes important
        LinkOnlySwitch      --  determines if links are the only thing grabbed

    Returns:
        linkList            --  list of file download links
        folderMap           --  dictionary of all folders
    """
    global FileInformation
    linkList: list = []
    folderMap: dict = {} # str: bool

    fileCount: int = len(FileList)
    fileCounter: int = 0

    for name in FileList:
        try:
            file = open(name, mode='r+', encoding='UTF-8')
            reader = file.readlines()
            file.close()
        except Exception:
            # TODO: Change exception type.
            # TODO: Use centralized error logging.
            print(f"File {name} was unable to be opened.")
            continue

        tokenIndex: int = None
        downloadIndex: int = None
        link: str = None
        filetype: str = None
        filename: str = None
        folder: str = None

        # This is used to avoid doing string comparisons every if-statment.
        # PRESUMABLY, this will safe time spent scaning for links.
        operationCounter: int = 0

        #print(f"Files found\t{counter}", end='\r', flush=True)

        # TODO: Remove these god-awful magic numbers.
        # Now read from file.
        for line in reader:
            line = line.strip()
            if operationCounter == 0 and line[:4] == '"id"':
                filename = line[7:-2]
                operationCounter = 1
            elif operationCounter == 1 and line[:6] == '"filet':
                # Found file type, now store.
                filetype = line[13:line.find('"',13)]
                operationCounter = 2
            elif operationCounter == 2 and line[:13] == '"url_private_':
                # Found download link, store and reset.
                tokenIndex = line.find("?t=")
                if downloadIndex is None:
                    # This should only be done once.
                    downloadIndex = line.find("download\\/") + 10

                # Grab the link, then the file name.
                link = line[25:-2]
                filename += '-' + line[downloadIndex:tokenIndex]

                folder = name[LocationIndex:-5]
                if not folderMap.get(folder, False):
                    folderMap[folder] = True

                # FileInformation -> name, type, link, folder
                linkList.append(FileInformation(filename, filetype, link.replace("\\", ""), folder))
                operationCounter = 0
                print(f"Files Processed\t-----\t{fileCounter}/{fileCount}", end='\r', flush=True)

        fileCounter += 1

    # TODO: Replace with SimpleNamespace objects, named tuples, or custom class
    print('\n', end='')
    return linkList, folderMap

def prompt_file(ForcePrompt: bool) -> None:
    """Prompts the user if an output file already exists.

    Arguments:
        ForcePrompt     --  determines if logic is ultimately skipped

    Returns:
        writeFlag       --  determines how the file will be opened 
    """

    # Prompt user if overwriting is desired, where applicable.
    writeFlag = 'w'
    if not ForcePrompt and os.path.isfile(OutputFile):
        print(f"Do you want to override file ({OutputFile})?")
        ans = input("[O]verwrite, [A]ppend, or [Q]uit (Default is overwrite)\t>")
        
        # Needs a better solution.
        if ans == 'a' or ans == 'A':
            writeFlag = 'a'
        elif ans == 'Q' or ans == 'q':
            # TODO: Exit out of program ASAP.
            # ERROR LEVEL
            return

    return writeFlag

def write_links(LinkList: list, FileTypes: list, OutputFile: str, ForcePrompt: bool) -> None:
    """Each link in the given list will be written to the desired
    output file.

    Arguments:
        LinkList        --  list of file download links (link, file name, file type)
        FileTypes       --  dictionary of allowed file types
        OutputFile      --  location of output file, if applicable
        ForcePrompt     --  determines if file can be overwritten, if present
    """
    # Open file and check if it already exists.
    writer = open(OutputFile, mode=prompt_file(ForcePrompt), encoding='UTF-8')

    for fUrl in LinkList:
        # If there are no specified file types, skip check.
        if FileTypes is None or FileTypes.get(fUrl[2], False):
            writer.write(fUrl[0])
            writer.write("\n")

    # Close resource
    writer.close()

def download_files(LinkList: list, FolderMap:dict, FileTypes: list, OutputDirectory: str, ForcePrompt: bool) -> None:
    """Downloads each file from their respective link.

    Arguments:
        LinkList            --  list of file download links (name, type, link, folder)
        FolderMap           --  dictionary of folders
        FileTypes           --  dictionary of allowed file types
        OutputDirectory     --  output directory for downloaded files
        ForcePrompt         --  determines if file can be overwritten, if present
    """
    # Determine filesystem delimination.
    slash = '/'
    from sys import platform
    if platform == "win32":
        slash = '\\'

    # Produce output log file in appropriate location.
    from datetime import datetime

    # Keep time the same for output file and folder.
    currTime: str = datetime.now().strftime("%d-%B-%Y-%H-%M-%S")
    outputFile: str = OutputDirectory + slash + 'slackjp-files-' + currTime + '.txt'
    # writer = open(outputFile, mode=prompt_file(ForcePrompt), encoding='UTF-8')

    # Change output folder to avoid dumping all files into the same folder.
    outputFolder: str = OutputDirectory + slash + 'slackjp-output-' + currTime

    # Never silence errors.
    try:
        os.mkdir(outputFolder)
    except FileNotFoundError as e:
        # Directory is not reachable or does not exist, attempt recursive mkdir.
        print("Directory does not exist.\n")
        ans = input("Do you want to [M]ake the directory or [A]bort? (Default is make)\t>")

        # Handle response
        if ans == 'A' or ans == 'a':
            print("Aborting...\n")
            # writer.close()
            exit()
        else:
            # Make an effort of attempting something else.
            # TODO: If this fails, then I don't know what to do yet.
            os.makedirs(outputFolder)

    # For all necessary folders, _create them_!
    print("Creating export folders...")
    for folder in FolderMap.keys():
        try:
            os.makedirs(outputFolder + folder)
        except FileNotFoundError as e:
            print("Failure when making folders for downloading.  Aborting...")
            exit()

    import wget
    # counter: int = 0
    print("Downloading files...")
    for fileInfo in LinkList:
        # If there are no specified file types, skip check.
        if FileTypes is None or FileTypes.get(fileInfo.type, False):
            # Produce counter information.
            # TODO: Add user prompt to use either non-descriptive file names (type only) or full name.
            slackFileName: str = outputFolder + slash + fileInfo.folder + slash + fileInfo.name

            # Download file via wget library.
            # TODO: Account for file permissions.  Check WELL in-advance.
            wget.download(fileInfo.link, slackFileName)

            # TODO: Remove token information.  This is a user file, not admin.
            # writer.write(f"File {fUrl[1]} ({fUrl[0]}) written to [{slackFileName}].\n")
            # counter += 1

    # Tie up loose ends.
    writer.close()

    # wget doesn't like cleaning up its output, for reasons unknown.
    print('\n')

##
#   Global TODO List
##
# TODO: Add exit codes from man page
# TODO: Clean up file and possibly split
# TODO: Centralized error handling
# TODO: Create sub-folders for downloading files (per channel)
# TODO: Catalog channel information in-advance.
# TODO: Make a configuration file for all the magic numbers presently used.

# Ensure this file is run directly.
if __name__ == "__main__":
    
    args = _parser.get_args()

    # Will test soon.
    rootLocation: str = os.path.realpath(args.directory)
    fileList: list = find_files(rootLocation, args.recurse)

    # TODO: Modify link scan to handle differnt styles of link scanning.
    # TODO: Change style to avoid unnecessary work with Link Scanning.
    linkList, folderMap = scan_links(fileList, len(rootLocation), args.linkOutput is not None)
    if len(linkList) == 0:
        print("No links found.  SlackJP stopping.")
        # TODO: Replace with error logging call.
        exit()

    # Manage possible functions.
    if args.linkOutput:
        print("This feature is currently broken.")
        # write_links(linkList, args,filetype, args.linkOutput, args.force)
    elif args.downOutput:
        download_files(linkList, folderMap, args.filetype, args.downOutput, args.force)
    elif args.textOutput:
        print("This feature is not yet implemented.")
    elif args.htmlOutput:
        print("This feature is not yet implemented.")

    # Replace with error codes if necessary.
    print("All operations completed.")
