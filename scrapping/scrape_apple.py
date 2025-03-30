import requests
from bs4 import BeautifulSoup
import json

# Apple Homepage URL
url = "https://www.apple.com/"

# Send request and get HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract headings
headings = [h.text.strip() for h in soup.find_all("h2")]

# Save to JSON file
with open("scrapping/apple_data.json", "w", encoding="utf-8") as file:
    json.dump(headings, file, indent=4)

print("✅ Data saved to scrapping/apple_data.json")

