from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement


class SamplePage(BaseForm):
    __unique_element = BasicElement(
        (By.XPATH, "//h1[@id='sampleHeading']"), "sample page unique header"
    )

    def __init__(self):
        super().__init__(
            self.__unique_element,
            "sample page",
        )
