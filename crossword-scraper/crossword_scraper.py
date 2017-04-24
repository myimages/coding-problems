import requests
from lxml import html, etree

def crawl_website(url, error_file_loc = "errors.txt"):
    """
    Converts a web page into an Element Tree.

    Args:
        url: A string which represents a website that we wish to crawl.
        error_file_loc: The name of the file where error reports will be
                        recorded.

    Returns:
        DOM_tree: An Element Tree created using the html module from the lxml
                  library. Contains None if url was not valid.

    Raises:
        RequestException: An error occurred trying to request the web page.
    """

    # Check for invalid requests
    try:
        page = requests.get(url)
    except requests.exceptions.RequestException as e:
        error_file = open(error_file_loc, "a")
        error_file.write("%s was not a valid url. " % url)
        error_file.write(str(e) + "\n")
        error_file.close()
        print("%s was not a valid url. \n" % url)
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
    # TODO
    # DOCUMENTATION
    """

    # We can use this to read the crossword solutions
    DOM_list = DOM_tree.xpath("//text ()")
    if "\nSorry, the page you were looking for in this blog does not exist.\n" in DOM_list:
        print("Page did not exist.")
        return None

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

