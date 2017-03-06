# Testing fetch

# Testing parse
# - download the fetch once - and save it to a file and then test to your hearts desire
# https://github.com/kevin1024/vcrpy
import crossword_scraper
import vcr
from lxml import html, etree

@vcr.use_cassette("fixtures/vcr_cassettes/nytcrossword.yaml")
def test_crawler_read_one_page_nytcrossword():
    # Tests if crossword_scraper's crawl has returned an element tree.
    # TODO: Test for contents of element tree.
    response = crossword_scraper.crawl_website("http://www.nytcrossword.com/")
    assert etree.iselement(response)
    assert len(response) > 0
    # Extracts the text content of a tree into a list.
    assert "Across" in response.xpath("//text ()")
    crossword_scraper.scrape_nytcrossword(response)

test_crawler_read_one_page_nytcrossword()
