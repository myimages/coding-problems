"""
Data from: http://www.nytcrossword.com/
Scrapes the site for crossword puzzles.
"""
# We're going to learn about these
import requests
from lxml import html, etree


def crawl_website(Url):
    """
    Reads one page from a url and then returns the DOMTree
    PARAMETERS
    Url: String, a url representing a website that we wish to crawl
    RETURNS
    DOMTree: An Element Tree created using the html module from the lxml library
    """
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

