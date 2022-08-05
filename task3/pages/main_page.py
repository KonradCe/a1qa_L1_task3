from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.button_element import ButtonElement
from task3.framework.utils.driver_utils import SingletonWebDriver as Swd
from task3.framework.utils.logger_utils import LoggerUtils
from task3.framework.utils.test_data_utils import TestDataUtils


class MainPage(BaseForm):
    URL = TestDataUtils.get_main_page_url()
    __unique_element = BasicElement(
        (By.XPATH, "//div[@class='home-banner']"), "unique element on main page"
    )
    __alerts_frame_window_btn = ButtonElement(
        (
            By.XPATH,
            "//div[contains(@class, 'top-card')]//h5[contains(text(),'Alerts')]",
        ),
        "'Alerts, Frame & Windows' card button",
    )
    __elements_btn = ButtonElement(
        (
            By.XPATH,
            "//div[contains(@class, 'top-card')]//h5[contains(text(),'Elements')]",
        ),
        "'elements' card button",
    )
    __widgets_btn = ButtonElement(
        (
            By.XPATH,
            "//div[contains(@class, 'top-card')]//h5[contains(text(),'Widgets')]",
        ),
        "'widgets' card button",
    )

    def __init__(self):
        super().__init__(
            self.__unique_element,
            "main page",
        )

    def go_to_main_page(self):
        LoggerUtils.log_info(f"{self.page_name} - going to {self.page_name}")
        Swd.go_to_page(self.URL)

    def click_on_alert_frame_window_btn(self):
        LoggerUtils.log_info(
            f"{self.page_name} - clicking on {self.__alerts_frame_window_btn.name}"
        )
        self.__alerts_frame_window_btn.click()

    def click_on_elements_btn(self):
        LoggerUtils.log_info(
            f"{self.page_name} - clicking on {self.__elements_btn.name}"
        )
        self.__elements_btn.click()

    def click_on_widgets_btn(self):
        LoggerUtils.log_info(
            f"{self.page_name} - clicking on {self.__widgets_btn.name}"
        )
        self.__widgets_btn.click()
