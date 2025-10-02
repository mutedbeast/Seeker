import requests
import sys
domain = sys.argv[1]

def usage_guide():
    print("Usage : Python seeker.py <domain> <operation> <wordlist>")

def without_arg():
    print("Welcome") #add ascii art

if domain == 'help':
    help = True
    usage_guide()

if help == False:
    x = requests.get(domain) 
    print(x.status_code)

