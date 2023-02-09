from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Start a new instance of ChromeDriver
driver = webdriver.Chrome(options=options)

# Navigate to the Quora homepage
driver.get("https://www.quora.com/topic/Spirituality")

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find all the questions on the page
questions = soup.find_all("div", class_="q-text qu-truncateLines--5 puppeteer_test_question_title")

# Loop through each question and print the text
for question in questions:
    print(question.text)

# Find all the answers on the page
answers = soup.find_all("div", class_="AnswerBase")

# Loop through each answer and print the text
for answer in answers:
    print(answer.text)

# Quit the ChromeDriver instance
driver.quit()