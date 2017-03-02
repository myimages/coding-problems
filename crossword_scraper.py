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
    CrosswordPage = requests.get(url)
    tree = html.fromstring(CrosswordPage.content)
    # We can reasonably assume that this will work okay for 1 page.
    # We will get it working for 1 page and then expand to multiple pages with scrapy?
    # This will return a 1 if crawling was successful and a 0 if crawling was not successful eventually
    print(tree)
    return 0

def scrape_website(f):
    """
    Process the data from a website offline
    """
    return 0
