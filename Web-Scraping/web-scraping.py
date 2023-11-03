import requests
from bs4 import BeautifulSoup

# Example of how to use BeautifulSoup to scrape data from a webpage
# This is for educational purposes and should not be used without permission

url = 'https://www.yorku.ca/'

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all elements in the HTML document
    for element in soup.find_all(True):  # The True argument here is to match every element
        print(f"Element: {element.name}")
        for attr, value in element.attrs.items():
            print(f"  Attribute: {attr}, Value: {value}")
        print(f"  Text: {element.get_text(strip=True)}\n")
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
