import requests
from bs4 import BeautifulSoup

def scrape_real_estate_data(base_url, pages):
    property_data = []
    for page in range(1, pages + 1):
        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract data logic here
        # Append to property_data
    return property_data
