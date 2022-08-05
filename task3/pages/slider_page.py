from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.slider import Slider
from task3.framework.utils.logger_utils import LoggerUtils


class SliderPage(BaseForm):
    __unique_element = BasicElement(
        (By.XPATH, "//div[@id='sliderContainer']"), "unique element on slider page"
    )
    __slider_input = BasicElement(
        (By.XPATH, "//input[@id='sliderValue']"), "input box with slider value"
    )
    __slider = Slider((By.XPATH, "//input[@type='range']"), "slider")

    def __init__(self):
        super().__init__(
            self.__unique_element,
            "page with a slider",
        )

    def set_slider_value_to(self, desired_value):
        self.__slider.click()
        current_value = self.get_slider_value()
        LoggerUtils.log_info(
            f"{self.page_name} - changing slider value from {current_value} to {desired_value}"
        )
        difference = desired_value - current_value
        if difference > 0:
            self.__slider.increase_value_by(difference)
        else:
            self.__slider.decrease_value_by(difference)

    def get_slider_value(self):
        slider_text = self.__slider_input.get_attribute("value")
        return int(slider_text)
