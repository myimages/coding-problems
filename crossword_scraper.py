"""
Data from: http://www.nytcrossword.com/
Scrapes the site for crossword puzzles.
"""
from lxml import html
import requests

# CURRENTLY WORKING ON
def crawl_website(url):
    """
    Reads a page from a url and then prints it to a file
    GOAL: Will read a series of pages defined by another variable. For now, let's just read one page.
    """
    Page = requests.get(url)
    tree = html.fromstring(Page.content)
    # We can reasonably assume that this will work okay for 1 page.
    # We will get it working for 1 page and then expand to multiple pages with scrapy?
    return tree

def scrape_nytcrossword(f):
    """
    Process the data from a website offline
    """
    return 0
