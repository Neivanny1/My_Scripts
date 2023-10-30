#!/usr/bin/bash python3
import requests
from bs4 import BeautifulSoup
import os
import urllib.request

# The URL of the website to scrape
url = "https://example.com"  # Replace with the actual URL of the test website

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links (a tags) on the page
    links = soup.find_all('a')

    # Create a directory to save the downloaded files
    if not os.path.exists('downloaded_folders'):
        os.mkdir('downloaded_folders')

    # Loop through the links and download folders
    for link in links:
        href = link.get('href')
        if href.endswith('/'):
            folder_name = href.rstrip('/').split('/')[-1]
            folder_url = url + href
            folder_path = os.path.join('downloaded_folders', folder_name)

            # Check if the folder doesn't exist, then download it
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
                print(f"Downloading folder: {folder_name}")
                urllib.request.urlretrieve(folder_url, os.path.join(folder_path, "index.html"))
                print(f"Folder '{folder_name}' downloaded.")
            else:
                print(f"Folder '{folder_name}' already exists. Skipping.")

else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
