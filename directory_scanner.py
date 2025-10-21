import requests

from time_handler import current_time


#add functions here
def directory_scanner(target,wordlist_file):
    total_directories = 0
    print(f'\nDirectory Scanning started at {current_time()}')

    for words in wordlist_file:
        x = requests.get(f"{target}/{words}") 
        if x.status_code == 200:
            total_directories = total_directories + 1 
            print(f"{target}/{words}")
    print(f"\nTotal {total_directories} directories found")

