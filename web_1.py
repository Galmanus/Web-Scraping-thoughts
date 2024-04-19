# Import the necessary modules
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# Define a function to get the title of a webpage
def getTitle(url):
    try:
        # Send an HTTP request to the specified URL and read the response content
        html = urlopen(url)

        # Parse the HTML content of the webpage using the html.parser
        bs = BeautifulSoup(html.read(), 'html.parser')

        # Search for the first <h1> tag in the HTML document and store it in a variable called title
        title = bs.body.h1

    # If the <h1> tag is not found, return None
    except AttributeError as e:
        return None

    return title

# Call the function with the URL of the webpage
title = getTitle('http://www.pythonscraping.com/pages/page1.html')

# Check if the title was found





