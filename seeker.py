import requests
import sys
from wordlist import wordlist
from without_argv import without_arg

a = 'wordlist_all.txt'
c = 'wordlist_common.txt'
help = False
total_directories = 0

def usage_guide():
    print("Usage : Python seeker.py <domain> <operation> <wordlist> \n Use all for full search, com for common search" )

if len(sys.argv) == 1:
    without_arg()
else:
    domain = sys.argv[1]
    operation = sys.argv[2]
    wordlist_file_directory = sys.argv[3]

if sys.argv[1] == '-help' or sys.argv[1] == '-h'or sys.argv[1] == 'help':
    help = True
    usage_guide()

if operation == '-a':
    wordlist = wordlist(a)
elif operation == '-c':
    wordlist = wordlist(c)
elif operation == '-custom':
    wordlist = wordlist(wordlist_file_directory)

if help == False:
    for words in wordlist:
        x = requests.get(f"{domain}/{words}") 
        if x.status_code == 200:
            total_directories = total_directories + 1 
            print(f"{domain}/{words}")
        
print(f"\nTotal {total_directories} found")



