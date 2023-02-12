from pathlib import Path
from data.topic_scraper import QuoraScraper, GENERATED_DIR



def test_scraper():
    topic = 'gifts'
    scraper = QuoraScraper()
    scraper.start_driver()
    scraper.scrape(topic=topic)
    scraper.close_driver()
    path_to_jsonl_file = Path(GENERATED_DIR, topic + '.json')
    assert Path.exists(path_to_jsonl_file) is True
