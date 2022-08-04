from selenium.webdriver.common.by import By

from task3.framework.utils.test_data_utils import TestDataUtils
from task3.framework.base_form import BaseForm
from task3.framework.driver_utils import SingletonWebDriver as Swd
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.button_element import ButtonElement
from task3.framework.utils.logger_utils import LoggerUtils


class MainPage(BaseForm):
    URL = TestDataUtils.get_main_page_url()
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
        LoggerUtils.log_info(f"{self.page_name} - going to {self.page_name}")
        Swd.go_to_page(self.URL)

    def click_on_alert_frame_window_btn(self):
        alerts_frame_window_btn = ButtonElement(
            self.ALERT_FRAME_WINDOW_BTN_LOC, "'Alerts, Frame & Windows' card button"
        )
        LoggerUtils.log_info(
            f"{self.page_name} - clicking on {alerts_frame_window_btn.name}"
        )
        alerts_frame_window_btn.click()

    def click_on_elements_btn(self):
        elements_btn = ButtonElement(self.ELEMENTS_BTN_LOC, "'elements' card button")
        LoggerUtils.log_info(f"{self.page_name} - clicking on {elements_btn.name}")
        elements_btn.click()
