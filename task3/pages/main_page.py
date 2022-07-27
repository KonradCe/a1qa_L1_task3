from selenium.webdriver.common.by import By

import task3.framework.driver_utils
import task3.framework.utils.test_data_utils
from task3.framework.base_form import BaseForm
from task3.framework.elements import BasicElement, ButtonElement
from task3.framework.utils.logger_utils import log_info


class MainPage(BaseForm):
    URL = task3.framework.utils.test_data_utils.get_main_page_url()
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div[@class='home-banner']")
    ALERT_FRAME_WINDOW_BTN_LOC = (
        By.XPATH,
        "//div[contains(@class, 'top-card')]//h5[contains(text(),'Alerts')]",
    )
    ELEMENTS_BTN_LOC = (
        By.XPATH,
        "//div[contains(@class, 'top-card')]//h5[contains(text(),'Elements')]",
    )

    def __init__(self):
        super().__init__(
            BasicElement(self.UNIQUE_ELEMENT_LOC, "unique element on main page"),
            "main page",
        )

    def go_to_main_page(self):
        log_info(f"{self.page_name} - going to {self.page_name}")
        task3.framework.driver_utils.go_to_page(self.URL)

    def click_on_alert_frame_window_btn(self):
        alerts_frame_window_btn = ButtonElement(
            self.ALERT_FRAME_WINDOW_BTN_LOC, "'Alerts, Frame & Windows' card button"
        )
        log_info(f"{self.page_name} - clicking on {alerts_frame_window_btn.name}")
        alerts_frame_window_btn.click()

    def click_on_elements_btn(self):
        elements_btn = ButtonElement(self.ELEMENTS_BTN_LOC, "'elements' card button")
        log_info(f"{self.page_name} - clicking on {elements_btn.name}")
        elements_btn.click()
