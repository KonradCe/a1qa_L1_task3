from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.button_element import ButtonElement
from task3.framework.utils.logger_utils import log_info


class BrowserWindowsPage(BaseForm):
    UNIQUE_ELEMENT_LOC = (
        By.XPATH,
        "//div[@class='main-header' and text()[contains(., 'Browser Windows')]]",
    )
    NEW_TAB_BTN_LOC = (By.XPATH, "//button[@id='tabButton']")

    def __init__(self):
        super().__init__(
            BasicElement(self.UNIQUE_ELEMENT_LOC, "alerts page unique header"),
            "'Browser Windows' page",
        )

    def click_new_tab_btn(self):
        new_tab_btn = ButtonElement(self.NEW_TAB_BTN_LOC, "new tab button")
        log_info(f"{self.page_name} - clicking on {new_tab_btn.name}")
        new_tab_btn.click()
