"""
Data from: http://www.nytcrossword.com/
Scrapes the site for crossword puzzles.
"""
# We're going to learn about these
import requests
from lxml import html, etree


# CURRENTLY WORKING ON
def crawl_website(Url):
    """
    Reads a page from a url and then prints it to a file
    GOAL: Will read a series of pages defined by another variable. For now, let's just read one page.
    """
    Page = requests.get(Url)
    Tree = html.fromstring(Page.content)

    return Tree

def scrape_nytcrossword(f):
    """
    Process the data from a website offline
    """
    return 0

