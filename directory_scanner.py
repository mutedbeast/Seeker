import requests
import string
import random

from time_handler import current_time

#add functions here
def directory_scanner(target, wordlist_file):
    total_directories = 0
    false_positives = 0
    
    print(f'\nDirectory Scanning started at {current_time()}')
    print(f'Target: {target}')
    print('='*60)
    
    # Get baseline response from a random non-existent page
    baseline_response = requests.get(f"{target}/{''.join(random.choices(string.ascii_lowercase, k=32))}")
    baseline_length = len(baseline_response.content)
    baseline_redirect = baseline_response.url
    
    print(f'Baseline check complete (length: {baseline_length} bytes)\n')
    
    for words in wordlist_file:
        words = words.strip()  # Remove whitespace/newlines
        try:
            response = requests.get(f"{target}/{words}", allow_redirects=True, timeout=5)
            
            # Check multiple conditions
            if response.status_code == 200:
                content_length = len(response.content)
                final_url = response.url
                
                # Filter out false positives
                if (final_url == f"{target}/{words}" or  # Not redirected
                    final_url == f"{target}/{words}/" or  # Trailing slash OK
                    abs(content_length - baseline_length) > 100):  # Content differs significantly
                    
                    total_directories += 1
                    print(f"[200] {target}/{words} ({content_length} bytes)")
                    
                    # Show if redirected but content is different
                    if final_url != f"{target}/{words}" and final_url != f"{target}/{words}/":
                        print(f"      ↳ Redirects to: {final_url}")
                else:
                    false_positives += 1
                    
            elif response.status_code in [301, 302, 303, 307, 308]:
                total_directories += 1
                print(f"[{response.status_code}] {target}/{words} → {response.headers.get('Location', 'Unknown')}")
                
            elif response.status_code == 403:
                total_directories += 1
                print(f"[403] {target}/{words} (Forbidden - exists but restricted)")
                
        except requests.exceptions.RequestException as e:
            print(f"[ERR] {target}/{words} - {str(e)[:50]}")
            continue
    
    print('\n' + '='*60)
    print(f"Scan completed at {current_time()}")
    print(f"Valid directories found: {total_directories}")
    print(f"False positives filtered: {false_positives}")
    print('='*60)