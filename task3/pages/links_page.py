from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.utils.logger_utils import LoggerUtils


class LinksPage(BaseForm):
    __unique_element = BasicElement(
        (By.XPATH, "//div[@id='linkWrapper']"), "links page unique wrapper"
    )
    __home_link = BasicElement(
        (By.XPATH, "//a[@id='simpleLink']"), "link to main page (from 'Links' page)"
    )

    def __init__(self):
        super().__init__(
            self.__unique_element,
            "'Links' page",
        )

    def click_on_home_link(self):
        LoggerUtils.log_info(f"{self.page_name} - clicking on {self.__home_link.name}")
        self.__home_link.click()
