import requests
import sys
from default_wordlist import wordlist_fun

help = False
def usage_guide():
    print("Usage : Python seeker.py <domain> <operation> <wordlist>")

def without_arg():
    print('''
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
''')
    print("Choose one operation \n 1.Indexing \n 2.Port Scanning")

if len(sys.argv) == 1:
    without_arg()
else:
    domain = sys.argv[1]

if sys.argv[1] == 'help':
    help = True
    usage_guide()

indexs = []
if help == False:
    for words in wordlist:
        x = requests.get(f"{domain}/{words}") 
        if x.status_code == 200:
            indexs.append(f"{domain}/{words}")
        
print(f"Total {len(indexs)} found")
for index in indexs:
    print(index)


