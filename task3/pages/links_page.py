from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.utils.logger_utils import LoggerUtils


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
        LoggerUtils.log_info(f"{self.page_name} - clicking on {home_link.name}")
        home_link.click()
