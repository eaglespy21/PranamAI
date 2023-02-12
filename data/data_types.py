import typing
from selenium.webdriver.remote.webelement import WebElement

WebElementsList = list[WebElement]
StrList = list[str]


class QA(typing.NamedTuple):
    question: str
    answer: str

    def __repr__(self) -> str:
        return f'<QuestionAns {self.question}, {self.answer}>'


QAList = list[QA]