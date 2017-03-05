"""
Data from: http://www.nytcrossword.com/
Scrapes the site for crossword puzzles.
"""
# Learn about virtualenv
# Switch to lxml
import requests
from bs4 import BeautifulSoup
# lxml - wrapper around beautifulsoup
# You have to instantiate the etree - models the DOM
# That model allows you to traverse the DOM

# CURRENTLY WORKING ON
def crawl_website(url):
    """
    Reads a page from a url and then prints it to a file
    GOAL: Will read a series of pages defined by another variable. For now, let's just read one page.
    """
    Response = requests.get(url)
    PageContent = Response.text
    Soup = BeautifulSoup(PageContent, "html.parser")
    # We can reasonably assume that this will work okay for 1 page.
    # We will get it working for 1 page and then expand to multiple pages with scrapy?
    # You're getting bytes and need to
    return Soup

def scrape_nytcrossword(f):
    """
    Process the data from a website offline
    """
    return 0

