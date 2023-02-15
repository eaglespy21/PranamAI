import json
from pathlib import Path
from data.topic_scraper import QuoraScraper, GENERATED_DIR
from data.data_types import QA

topic = 'gifts'
path_to_jsonl_file = Path(GENERATED_DIR, topic + '.jsonl')


def test_scraper():

    scraper = QuoraScraper()
    scraper.start_driver()
    scraper.scrape(topic=topic)
    scraper.close_driver()


def test_content_of_generated_file():
    # TODO: Either create a test fixture for test_scraper or call that function here

    assert Path.exists(path_to_jsonl_file) is True
    qa_list = []
    with open(path_to_jsonl_file, 'r', encoding='utf-8') as f:
        for line in f:
            qa_list.append(json.loads(line))
    assert len(qa_list) >= 1
    for qa in qa_list:
        assert qa.keys() == QA('t', 't')._asdict().keys()
        qa = QA(**qa)
        print(qa)
        assert not ('https' in qa.question)
