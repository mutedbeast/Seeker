#import stuff here
import requests
import sys
import argparse

from wordlist import wordlist
from without_argv import without_arg
from text import description,usage

#Variables
a = 'wordlist_all.txt'
c = 'wordlist_common.txt'
help = False
total_directories = 0

#arguments
parser = argparse.ArgumentParser(prog=None, usage=usage, description=description, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True) #Remove unneccessary arguments

#parser.print_help()

parser.add_argument("-t", "--target", required=True, help="Path to directory to index")
parser.add_argument("-o",'--operation',required=True, help='add operation here')
parser.add_argument("-c",'--command',required=True, help='add command here')


args = parser.parse_args()

'''
First work on argument based then no argument based

if len(sys.argv) == 1:
    without_arg()
else:

if operation == '-a':
    wordlist = wordlist(a)
elif operation == '-c':
    wordlist = wordlist(c)
elif operation == '-custom':
    wordlist = wordlist(wordlist_file_directory)
'''

if args.operation == 'd' or args.operation == 'D':
    if args.command == 'full' or args.command == 'f':
        wordlist = wordlist(a)
    elif args.command == 'common' or args.command == 'c':
        wordlist = wordlist(c)
    else:
        wordlist = wordlist(args.command)
    
if args.operation == 'p' or args.operation == 'P':
    pass


#print(f"\nTotal {total_directories} found")

print(f"Target : {args.target}")
print(f"Operation : {args.operation}")
print(f"Command: {args.command}")
