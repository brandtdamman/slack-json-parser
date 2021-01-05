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
import sys

# Argument Parser Setup
_parser = argparse.ArgumentParser(description='Slack JSON Parser', epilog='Further \
    information can be found via "man slackjp".')
_parser.add_argument('-d', action='store_true', help='Download attached files.')
_parser.add_argument('-D', action='store_true', nargs='+', help='')

_parser.add_argument('--version', action='version', version='%(prog)s ' + _verNumber)

