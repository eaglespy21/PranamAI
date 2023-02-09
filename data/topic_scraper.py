from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
        self.open_url('https://www.quora.com/topic/India')
        elements = self.driver.find_elements(By.CLASS_NAME, 'js-focus-visible')
        print(str(len(elements)) + "!!!!!!!!!!!!!!!!!!")
        # time.sleep(100)


if __name__ == "__main__":
    scraper = QuoraScraper()
    scraper.start_driver()
    scraper.scrape()