from data.topic_scraper import QuoraScraper

def test_scraper():
    scraper = QuoraScraper()
    scraper.start_driver()
    scraper.scrape('gifts')
    scraper.close_driver()