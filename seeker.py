#import stuff here
import argparse
import time

from wordlist import wordlist_function
from without_argv import without_arg
from text import description,usage
from directory_scanner import directory_scanner
from port_scanner import port_scan_main

#Variables
a = 'wordlist_all.txt'
c = 'wordlist_common.txt'

#arguments
parser = argparse.ArgumentParser(prog=None, usage=usage, description=description, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True) #Remove unneccessary arguments

#parser.print_help()

parser.add_argument("-t", "--target", help="Path to directory to index")
parser.add_argument("-o",'--operation',metavar='', help='Choose an operation')
parser.add_argument("-c",'--command', metavar='',help='Choose a command')
parser.add_argument("-v",'--verbose', metavar='', action='store_true',help='Verbose')


args = parser.parse_args()


#First work on argument based then no argument based

if not any(vars(args).values()):
    without_arg()

if args.operation == 'd' or args.operation == 'D':
    if args.command == 'full' or args.command == 'f':
        wordlist_function = wordlist_function(a)
    elif args.command == 'common' or args.command == 'c':
        wordlist_function = wordlist_function(c)
    else:
        wordlist_function = wordlist_function(args.command)
    directory_scanner(args.target,wordlist_file=wordlist_function)
    
if args.operation == 'p' or args.operation == 'P':
    print('port scanning started')
    if args.verbose :
        port_scan_main(target=f"{args.target}",verbose=True)
    





