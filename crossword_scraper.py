"""
Data from: http://www.nytcrossword.com/
Scrapes the site for crossword puzzles.
"""
# We're going to learn about these
import requests
from lxml import html, etree
import re

# BEGIN Code copied from the Django project
def is_valid_url(Url):
    """
    Checks that a url is a valid url
    PARAMETERS
    Url: String
    RETURNS
    Boolean: True if Url is a valid url, False otherwise.
    """
    Regex = re.compile(
    # http:// or https://
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return Url is not None and Regex.search(Url)
# END code copied from the Django project


def crawl_website(Url):
    """
    Reads one page from a url and then returns the DOMTree
    PARAMETERS
    Url: String, a url representing a website that we wish to crawl
    RETURNS
    DOMTree: An Element Tree created using the html module from the lxml library
    """
    assert is_valid_url(Url)
    Page = requests.get(Url)
    DOMTree = html.fromstring(Page.content)
    return DOMTree

def etree_to_file(DOMTree):
    return

def scrape_nytcrossword(DOMTree):
    """
    Process the data from the nyt website for clue:answer pairs
    """

    # We can use this to read the crossword solutions
    DOMList = DOMTree.xpath("//text ()")
    iAcross = [i for i, j in enumerate(DOMList) if j == "Across"]
    iDown = [i for i, j in enumerate(DOMList) if j == "Down"]
    Clues = []
    for element in DOMList[iAcross[1]+1:iDown[1]]:
        element = element.strip()
        if element:
            Clues.append(element)
    for element in DOMList[iDown[1]:]:
        element = element.strip()
        if element:
            Clues.append(element)
        else:
            break
    print(Clues)

