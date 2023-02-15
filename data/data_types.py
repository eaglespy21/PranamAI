import typing
from selenium.webdriver.remote.webelement import WebElement

WebElementsList = list[WebElement]
StrList = list[str]


class Question(typing.NamedTuple):
    question: str
    url: str


class QA(typing.NamedTuple):
    question: Question
    answer: str

    def __repr__(self) -> str:
        return f'<QuestionAns {self.question}, {self.answer}>'


QAList = list[QA]
QuestionList = list[Question]