import os

from port_scanner import port_scan_main
from directory_scanner import directory_scanner
from wordlist import wordlist_function

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
    operation = input("Choose one operation \n 1.Directory Scanning \n 2.Port Scanning \nEnter your operation : ")
    if operation == '2':
        timeout = float(input("Enter timeout value : "))
        port_scan_main(target,verbose=False,timeout=timeout)
    if operation == '1':
        wordlist_input = input("Choose a wordlist_function file \nType C For common wordlist_function\n A for all \n Path of custom")
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


without_arg()