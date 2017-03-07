import requests
from lxml import html, etree


def crawl_website(url):
    """
    Converts a web page into an Element Tree.

    Args:
        url: A string which represents a website that we wish to crawl.

    Returns:
        DOM_tree: An Element Tree created using the html module from the lxml
                  library. Contains None if url was not valid.

    Raises:
        RequestException: An error occurred trying to request the web page.
    """
    # Need to add some error handling here. I don't want it to crash if the url is not valid
    try:
        page = requests.get(url)
    except requests.exceptions.RequestException as e:
        f = open("errors.txt", w)
        f.write(str(e))
        f.close()
        print("%s was not a valid url." % url)
        return None
    DOM_tree = html.fromstring(page.content)
    return DOM_tree

def etree_to_file(DOM_tree):
    """
    Writes an element tree to a file.

    """
    return None

def scrape_nytcrossword(DOM_tree):
    """
    Process the data from the nyt website for clue:answer pairs.

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

