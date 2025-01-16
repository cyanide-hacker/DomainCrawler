# DomainCrawler
Finds all domains of an organization and outputs it to the console and to a txt file.

# Setup:
````
python -m venv .
source ./bin/activate
pip install -r requirments.txt
````
# Usage
You need to grab an API token from https://reverse-whois.whoisxmlapi.com.
You get 500 queries with a free account.

Syntax is as follows:
````
python ./DomainCrawler.py -a [your_api_key] -o '[Organization Name]'

