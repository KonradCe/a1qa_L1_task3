from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements import BasicElement, ButtonElement


class LinksPage(BaseForm):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div[@id='linkWrapper']")
    HOME_LINK_LOC = (By.XPATH, "//a[@id='simpleLink']")

    def __init__(self):
        super().__init__(
            BasicElement(self.UNIQUE_ELEMENT_LOC, "links page unique wrapper"),
            "'Links' page",
        )

    def click_on_home_link(self):
        home_link = BasicElement(
            self.HOME_LINK_LOC, "link to main page (from 'Links' page)"
        )
        home_link.click()
