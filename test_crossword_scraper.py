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

def test_crawler_error_handling():
    """
    Tests that our web crawler exception handles invalid urls.
    """

    crossword_scraper.crawl_website("nytcrossword", error_file_loc = "errors_tmp.txt")
    error_f = open("errors_tmp.txt", "r")
    errors = error_f.read()
    assert "nytcrossword" in errors
    error_f.close()
    os.remove("errors_tmp.txt")

@vcr.use_cassette("fixtures/vcr_cassettes/nytcrossword_invalid.yaml")
def test_scraper_on_invalid_page():
    response = crossword_scraper.crawl_website("http://www.nytcrossword.com/page/1")
    scrape = crossword_scraper.scrape_nytcrossword(response)
    assert scrape == None

def test_scraper_on_nytcrossword():
    # How would I make this independent? I'd have to read the file and turn it into an element tree. The thing I dreaded doing. Sigh.
    pass
