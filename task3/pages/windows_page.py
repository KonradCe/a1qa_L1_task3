from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.button_element import ButtonElement
from task3.framework.utils.logger_utils import LoggerUtils


class BrowserWindowsPage(BaseForm):
    __unique_element = BasicElement(
        (
            By.XPATH,
            "//div[@class='main-header' and text()[contains(., 'Browser Windows')]]",
        ),
        "alerts page unique header",
    )
    __new_tab_btn = ButtonElement(
        (By.XPATH, "//button[@id='tabButton']"), "new tab button"
    )

    def __init__(self):
        super().__init__(
            self.__unique_element,
            "'Browser Windows' page",
        )

    def click_new_tab_btn(self):
        LoggerUtils.log_info(
            f"{self.page_name} - clicking on {self.__new_tab_btn.name}"
        )
        self.__new_tab_btn.click()
