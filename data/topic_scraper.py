import json
from logging import Logger, getLogger
from selenium import webdriver
from selenium.webdriver.common.by import By

FLUTHER_TOPICS_URL = 'https://www.fluther.com/topics/'

class QuoraScraper:
    def __init__(self):
        self.driver = ''
        self.questions = []
        self.answers = []
        self.logger = getLogger()


    def start_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def close_driver(self):
        self.driver.close()

    def open_url(self, url):
        self.driver.get(url)

    def scrape(self, topic: str) -> None:
        self.open_url(FLUTHER_TOPICS_URL + topic)
        # TODO: find a better way to find all the questions in one shot
        elements = self.driver.find_elements(By.CLASS_NAME, 'row2')
        elements.extend(self.driver.find_elements(By.CLASS_NAME, 'row1'))
        self.logger.info('!!!!number of questions found!!! %d', len(elements))

        question_urls = []
        for element in elements:
            q = element.find_element(By.TAG_NAME, 'a')
            # print(q.text)
            href = q.get_attribute('href')
            question_urls.append(href)
        print(question_urls[0])
        self.get_answer(question_urls[0])


    def get_answer(self, link_to_question: str)-> str:
        self.open_url(link_to_question)
        first_answer_div = self.driver.find_element(By.CLASS_NAME, 'message')
        first_answer = first_answer_div.find_element(By.TAG_NAME, 'p').text
        print(first_answer)
        return first_answer