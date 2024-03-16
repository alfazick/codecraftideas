# Project Overview: Concurrent Web Scraper with Defensive Programming
# Objective: To build a Python application that scrapes data from multiple URLs concurrently, 
# demonstrates error handling, implements timeouts for network requests, 
# and manages resources effectively.

# Key Features:

# Concurrent fetching of web pages to improve efficiency.
# Timeouts for network requests to avoid hanging.
# Exception handling to manage errors gracefully.
# Limitation on the number of concurrent operations to prevent resource exhaustion.


import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import time 

# List of URLs to scrape
urls = [
    "http://example.com",
    # Add more URLs as needed
]

# Function to fetch and parse a single URL

def fetch_and_parse(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').get_text()
        print(f"Title found: {title}")
        return title
    except requests.Timeout:
        print(f"Request timed out for {url}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

# Function to save titles to a file

def save_titles(titles):
    with open("titles.txt","w") as file:
        for title in titles:
            if title:
                file.write(f"{title}\n")

def main():
    start_time = time.time()
    titles = []
    with ThreadPoolExecutor(max_workers = 5) as executor:
        future_to_url = {
            executor.submit(fetch_and_parse,url): url for url in urls
        }
        for future in as_completed(future_to_url):
            titles.append(future.result())
        
    save_titles(titles)
    print(f"Scrapping completed in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()