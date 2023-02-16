import typing
from selenium.webdriver.remote.webelement import WebElement

WebElementsList = list[WebElement]
StrList = list[str]


class Prompt(typing.NamedTuple):
    prompt: str
    url: str


class QA(typing.NamedTuple):
    prompt: Prompt
    completion: str

    def __repr__(self) -> str:
        return f'<QuestionAns {self.prompt}, {self.completion}>'


QAList = list[QA]
QuestionList = list[Prompt]