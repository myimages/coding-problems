"""
Data from: http://www.nytcrossword.com/
Scrapes the site for crossword puzzles.
"""
# We're going to learn about these
import requests
from lxml import html, etree


def crawl_website(url):
    """
    Reads one page from a url and then returns the DOMTree
    PARAMETERS
    url: String, a url representing a website that we wish to crawl
    RETURNS
    DOMTree: An Element Tree created using the html module from the lxml library
    """
    # Need to add some error handling here. I don't want it to crash if the url is not valid
    page = requests.get(url)
    DOM_tree = html.fromstring(page.content)
    return DOM_tree

def etree_to_file(DOM_tree):
    return

def scrape_nytcrossword(DOM_tree):
    """
    Process the data from the nyt website for clue:answer pairs
    """

    # We can use this to read the crossword solutions
    DOM_list = DOM_tree.xpath("//text ()")
    i_across = [i for i, j in enumerate(DOM_list) if j == "Across"]
    i_down = [i for i, j in enumerate(DOM_list) if j == "Down"]
    clues = []
    for element in DOM_list[i_across[1]+1:i_down[1]]:
        element = element.strip()
        if element:
            clues.append(element)
    for element in DOM_list[i_down[1]:]:
        element = element.strip()
        if element:
            clues.append(element)
        else:
            break

