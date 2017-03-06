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
    Reads a page from a url and then prints it to a file for scraping
    GOAL: Will read a series of pages defined by another variable. For now, let's just read one page.
    """
    Page = requests.get(Url)
    # Turns the webpage into an Element Tree
    DOMTree = html.fromstring(Page.content)
    # Should I do this, or just return the tree?
    # I WORKED SO HARD....
    # Just return the tree.
    return DOMTree

def scrape_nytcrossword(DOMTree):
    """
    Process the data from a website offline
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

