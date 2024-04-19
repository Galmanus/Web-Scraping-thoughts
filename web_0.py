# Import the necessary modules
from urllib.request import Request, urlopen  # Importing modules for making HTTP requests and handling responses
from bs4 import BeautifulSoup as soup  # Importing BeautifulSoup module for parsing HTML and XML documents

# Set the URL of the webpage to scrape
url = "https://www.google.com"  # Defining the URL of the webpage to be scraped

# Create a Request object with a custom User-Agent header
req = Request(url, headers={"User-Agent": "Mozilla/5.0"})  # Creating a Request object with a custom User-Agent header to mimic a web browser

# Send an HTTP request to the specified URL and read the response content
webpage = urlopen(req).read()  # Sending an HTTP request to the specified URL and reading the response content

# Parse the HTML content of the webpage using the html.parser
page_soup = soup(webpage, "html.parser")  # Parsing the HTML content of the webpage using the html.parser

# Search for the first <title> tag in the HTML document and store it in a variable called title
title = page_soup.find("title")  # Searching for the first <title> tag in the HTML document and storing it in a variable called title