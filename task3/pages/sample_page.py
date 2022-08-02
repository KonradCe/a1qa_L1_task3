from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement


class SamplePage(BaseForm):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//h1[@id='sampleHeading']")

    def __init__(self):
        super().__init__(
            BasicElement(self.UNIQUE_ELEMENT_LOC, "sample page unique header"),
            "sample page",
        )
