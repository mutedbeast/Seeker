import os

from port_scanner import port_scan_main
from directory_scanner import directory_scanner
from wordlist import wordlist_function
from urllib.parse import urlparse

a = 'wordlist_all.txt'
c = 'wordlist_common.txt'

def without_arg():
    print(r'''

  _________              __                 
 /   _____/ ____   ____ |  | __ ___________ 
 \_____  \_/ __ \_/ __ \|  |/ // __ \_  __ \
 /        \  ___/\  ___/|    <\  ___/|  | \/
/_______  /\___  >\___  >__|_ \\___  >__|   
        \/     \/     \/     \/    \/       
                                                              
''')
    target = input("Enter the target : ")
    operation = input("\nChoose an operation\n1.Directory Scanning\n2.Port Scanning \n\n➤ Your operation : ")
    if operation == '2':
        if target.startswith(('http://', 'https://')):
            target = urlparse(target).netloc
        timeout = float(input("Enter timeout value : "))
        port_scan_main(target,verbose=False,timeout=timeout)
    if operation == '1':
        if not target.startswith(('http://', 'https://')):
            target = 'https://' + target
        #wordlist_input = input("Choose a wordlist_function file \nType C For common wordlist_function\n A for all \n Path of custom")
        print("\n┌─ WORDLIST SELECTION ─────────────────────────────────────┐")
        print("│ [C] Common    - Quick scan with popular paths              │")
        print("│ [A] All       - Comprehensive scan (slower)                │")
        print("│ [Path]        - Custom wordlist file                       │")
        print("└─────────────────────────────────────────────────────────── ┘")
        wordlist_input = input("\n➤ Your choice: ").strip()

        if wordlist_input == "C" or wordlist_input== "c":
            wordlist_file = wordlist_function(c)
        elif wordlist_input == "A" or wordlist_input == "a":
            wordlist_file = wordlist_function(a)
        else:
            wordlist_file = wordlist_function(normalize_user_path(wordlist_input))
        directory_scanner(target,wordlist_file)

def normalize_user_path(p: str) -> str:
    p = p.strip()
    if (p.startswith(("'", '"')) and p.endswith(("'", '"'))) or p.startswith(("'", '"')) or p.endswith(("'", '"')):
        p = p.strip("'\"")
    if len(p) > 3 and (p[0] == '/' and p[2] == '/'):
        drive_letter = p[1].upper()
        if drive_letter.isalpha():
            p = f"{drive_letter}:{p[2:]}"
    p = os.path.expandvars(os.path.expanduser(p))
    p = os.path.normpath(p)
    return p

