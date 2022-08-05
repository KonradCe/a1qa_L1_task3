from selenium.webdriver import ActionChains, Keys

from task3.framework.elements.base_element import BaseElement
from task3.framework.utils.driver_utils import SingletonWebDriver as Swd


class Slider(BaseElement):
    def increase_value_by(self, increase_value):
        action = ActionChains(Swd.get_driver())
        for i in range(increase_value):
            action.send_keys(Keys.RIGHT)
        action.perform()

    def decrease_value_by(self, decrease_value):
        action = ActionChains(Swd.get_driver())
        for i in range(-decrease_value):
            action.send_keys(Keys.LEFT)
        action.perform()
