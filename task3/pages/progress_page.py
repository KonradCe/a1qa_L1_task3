from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.button_element import ButtonElement
from task3.framework.elements.progress_bar_element import ProgressBarElement
from task3.framework.utils.logger_utils import LoggerUtils


class ProgressBarPage(BaseForm):
    __unique_element = BasicElement(
        (By.XPATH, "//div[@id='progressBarContainer']"),
        "unique element on progress page",
    )
    __progress_start_stop_btn = ButtonElement(
        (By.XPATH, "//button[@id='startStopButton']"),
        "button to start and stop bar progress",
    )
    __progress_bar = ProgressBarElement(
        (By.XPATH, "//div[@role='progressbar']"), "progress bar"
    )

    def __init__(self):
        super().__init__(
            self.__unique_element,
            "page with a progress bar",
        )

    def start_stop_progress_bar(self):
        LoggerUtils.log_info(
            f"{self.page_name} - click on button to start or stop progress bar"
        )
        self.__progress_start_stop_btn.click()

    def stop_progress_at_value(self, value):
        LoggerUtils.log_info(
            f"{self.page_name} - waiting for progress bar to reach {value}, to click on start/stop button"
        )
        self.__progress_bar.wait_for_value(str(value))
        self.start_stop_progress_bar()

    def get_value_from_progress_bar(self):
        return self.__progress_bar.get_value()
