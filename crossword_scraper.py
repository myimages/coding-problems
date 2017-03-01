"""
Data from: http://www.nytcrossword.com/
Scrapes the site for crossword puzzles.
"""
from lxml import html
import requests

def crawl_website(url):
    """
    Reads a page from a url and then prints it to a file
    GOAL: Will read a series of pages defined by another variable. For now, let's just read one page.
    """
    CrosswordPage = requests.get(url)
    tree = html.fromstring(CrosswordPage.content)
    return 0
def scrape_website(f):
    """
    Process the data from a website offline
    """
    return 0

read_page("http://www.nytcrossword.com/")
