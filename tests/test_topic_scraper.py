import unittest
from data.topic_scraper import QuoraScraper

class TestScraper(unittest.TestCase):

    def test_scraper(self):
        scraper = QuoraScraper()
        scraper.start_driver()
        scraper.scrape('gifts')
        scraper.close_driver()