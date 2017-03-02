# Testing fetch

# Testing parse
# - download the fetch once - and save it to a file and then test to your hearts desire
# https://github.com/kevin1024/vcrpy
import crossword_scraper
import vcr

# Let's get this test to work.
@vcr.use_cassette("fixtures/vcr_cassettes/nytcrossword.yaml")
def test_crawler_on_nytcrossword():
    response = crossword_scraper.crawl_website("http://www.nytcrossword.com/")
    assert "<html>" in response
