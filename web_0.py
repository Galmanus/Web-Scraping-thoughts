# Import the necessary modules
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

# Set the URL of the webpage to scrape
url = "https://www.example.com"

# Create a Request object with a custom User-Agent header
req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

# Send an HTTP request to the specified URL and read the response content
webpage = urlopen(req).read()

# Parse the HTML content of the webpage using the html.parser
page_soup = soup(webpage, "html.parser")

# Search for the first <title> tag in the HTML document and store it in a variable called title
title = page_soup.find("title")