import json
from logging import Logger, getLogger
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from data.data_types import WebElementsList, WebElement, StrList, QAList, QA, QuestionList, Question

FLUTHER_TOPICS_URL = 'https://www.fluther.com/topics/'
GENERATED_DIR = 'C:\\Projects\\PranamAI\\data\\generated'
JSON_EXT = '.json'

class QuoraScraper:
    def __init__(self):
        self.driver = ''
        self.questions = []
        self.answers = []
        self.logger = getLogger()

    def scrape(self, topic: str) -> None:
        # TODO: Replace with a builder pattern for different kinds of completions?
        self._open_url(FLUTHER_TOPICS_URL + topic)
        questions = self._scrape_questions()
        qa_list = self._scrape_answers(questions)
        qa_dicts = [qa._asdict() for qa in qa_list]
        self.logger.debug(json.dumps(qa_dicts))
        with open(Path(GENERATED_DIR, topic + JSON_EXT), 'w', encoding='utf-8') as f:
            json.dump(qa_dicts, f, ensure_ascii=False, indent=4)

    def start_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def close_driver(self):
        self.driver.close()

    def _open_url(self, url):
        self.driver.get(url)

    def _scrape_answers(self, questions: QuestionList) -> QAList:
        qa_list = []
        for question in questions:
            q_text, url = question
            self._open_url(url)
            first_answer_div = self.driver.find_element(By.CLASS_NAME, 'message')
            first_answer = first_answer_div.find_element(By.TAG_NAME, 'p').text
            qa_list.append(QA(q_text, first_answer))
        return qa_list

    def generate_json(questions, answers) -> None:
        # TODO: Replace questions and answers as separate lists into a list of a dedicated dataclass?
        pass

    def _scrape_questions(self) -> QuestionList:
        questions = []
        # TODO: find a better way to find all the questions in one shot
        elements = self.driver.find_elements(By.CLASS_NAME, 'row2')
        elements.extend(self.driver.find_elements(By.CLASS_NAME, 'row1'))
        self.logger.info('!!!!number of questions found!!! %d', len(elements))
        for element in elements:
            q = element.find_element(By.TAG_NAME, 'a')
            href = q.get_attribute('href')
            questions.append(Question(q.text, href))
        self.logger.info('type of href is %s', type(questions[0]))
        return questions