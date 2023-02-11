from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class QuoraScraper:
    def __init__(self):
        self.driver = ''
        self.dataframe = ''
        self.questions = []
        self.answers = []


    def start_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def close_driver(self):
        self.driver.close()

    def open_url(self, url):
        self.driver.get(url)

    def scrape(self):
        self.open_url('https://www.fluther.com/topics/gifts/')
        elements = self.driver.find_elements(By.CLASS_NAME, 'row2')
        print(str(len(elements)) + "!!!!!!!!!!!!!!!!!!")
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

if __name__ == "__main__":
    scraper = QuoraScraper()
    scraper.start_driver()
    scraper.scrape()