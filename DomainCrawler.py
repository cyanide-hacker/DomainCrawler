import requests
import json
import argparse
import dns.resolver
import colorama
from colorama import Fore, Style
import random
import csv

colorama.init(autoreset=True)

def add_drips(text, probability=0.3):
    new_text = ""
    for char in text:
        if char == " ":
            new_text += char
        else:
            if random.random() < probability:
                new_text += Fore.GREEN + char
            else:
                new_text += Fore.BLUE + char
    return new_text

ascii_banner = """
 /$$$$$$$                                    /$$            /$$$$$$                                   /$$                    
| $$__  $$                                  |__/           /$$__  $$                                 | $$                    
| $$  \ $$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$ /$$$$$$$ | $$  \__/  /$$$$$$  /$$$$$$  /$$  /$$  /$$| $$  /$$$$$$   /$$$$$$ 
| $$  | $$ /$$__  $$| $$_  $$_  $$ |____  $$| $$| $$__  $$| $$       /$$__  $$|____  $$| $$ | $$ | $$| $$ /$$__  $$ /$$__  $$
| $$  | $$| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$| $$  \ $$| $$      | $$  \__/ /$$$$$$$| $$ | $$ | $$| $$| $$$$$$$$| $$  \__/
| $$  | $$| $$  | $$| $$ | $$ | $$ /$$__  $$| $$| $$  | $$| $$    $$| $$      /$$__  $$| $$ | $$ | $$| $$| $$_____/| $$      
| $$$$$$$/|  $$$$$$/| $$ | $$ | $$|  $$$$$$$| $$| $$  | $$|  $$$$$$/| $$     |  $$$$$$$|  $$$$$/$$$$/| $$|  $$$$$$$| $$      
|_______/  \______/ |__/ |__/ |__/ \_______/|__/|__/  |__/ \______/ |__/      \_______/ \_____/\___/ |__/ \_______/|__/      
                                                                                                                            
"""

bleeding_banner = "\n".join(add_drips(line) for line in ascii_banner.splitlines())
print(bleeding_banner)

def perform_post_request(api_key, organization):
    url = "https://reverse-whois.whoisxmlapi.com/api/v2"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "apiKey": api_key,
        "searchType": "current",
        "mode": "purchase",
        "punycode": True,
        "advancedSearchTerms": [{
            "field": "RegistrantContact.Organization",
            "term": organization,
            "exactMatch": False
        }]
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        print("Request Successful!")
        data = response.json()
        domains_list = data.get("domainsList", [])
        
        with open("domains_list.txt", "w") as file:
            for domain in domains_list:
                file.write(domain + "\n")
                print(domain)  # Output each domain to the terminal
        
        print(f"Domains have been written to 'domains_list.txt'. Total domains: {len(domains_list)}")
    else:
        print("Failed to make request!")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

def main():
    parser = argparse.ArgumentParser(description='Fetch domains associated with a specified organization using an API key.')
    parser.add_argument('-a', '--api_key', required=True, help='API Key for authentication')
    parser.add_argument('-o', '--organization', required=True, help='The organization name to search for.')
    args = parser.parse_args()
    
    perform_post_request(args.api_key, args.organization)

if __name__ == "__main__":
    main()
