import requests
#add functions here
def directory_scanner():
    for words in wordlist:
        x = requests.get(f"{target}/{words}") 
        if x.status_code == 200:
            total_directories = total_directories + 1 
            print(f"{target}/{words}")
