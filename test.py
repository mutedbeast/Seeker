import requests

target = 'https://www.chobani.com'
words = 'about'

x = requests.get(f"{target}/{words}") 
        
if x.status_code == 200:
    print("Success")
else:
    print('Failure')