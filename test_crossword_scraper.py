# Testing fetch

# Testing parse
# - download the fetch once - and save it to a file and then test to your hearts desire
# https://github.com/kevin1024/vcrpy
import crossword_scraper
import vcr
from lxml import html, etree
import pytest
import requests
import os

@vcr.use_cassette("fixtures/vcr_cassettes/nytcrossword.yaml")
def test_crawler_on_nytcrossword():
    """
    Tests our web crawler on the nytcrossword front page.
    """
    response = crossword_scraper.crawl_website("http://www.nytcrossword.com/")
    # Does my crawler create an element tree?
    assert etree.iselement(response)
    assert len(response) > 0
    # Does my element tree contain the information I need?
    assert "Across" in response.xpath("//text ()")

def test_crawler_exception_handling():
    """
    Tests that our web crawler exception handles invalid urls.
    """
    crossword_scraper.crawl_website("nytcrossword", error_file = "errors_tmp.txt")
    f = open("errors_tmp.txt", "r")
    errors = f.read()
    assert "nytcrossword" in errors
    f.close()
    os.remove("errors_tmp.txt")


def test_scraper_on_nytcrossword():
    # How would I make this independent? I'd have to read the file and turn it into an element tree. The thing I dreaded doing. Sigh.
    pass
