import json
import re
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
    start_end_re = re.compile(r'^ .* END$', re.DOTALL)
    end_re = re.compile(r'.*\n\n###\n\n$')
    for qa in qa_list:
        assert qa.keys() == QA('t', 't')._asdict().keys()
        assert list(qa.keys()) == ['prompt', 'completion']
        qa = QA(**qa)
        # print(qa)
        assert not ('https' in qa.prompt)
        assert end_re.search(qa.prompt)
        assert 'END' in qa.completion
        assert start_end_re.search(qa.completion)
    # Assert for u/2019 or single quotes
