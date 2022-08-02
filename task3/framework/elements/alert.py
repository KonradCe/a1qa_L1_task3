from selenium.common import NoAlertPresentException

from task3.framework.driver_utils import SingletonWebDriver as Swd
from task3.framework.utils import wait_utils


class Alert:
    def __get_alert(self):
        return wait_utils.wait_for_alert()

    def accept(self):
        self.__get_alert().accept()

    def dismiss(self):
        self.__get_alert().dismiss()

    def send_input(self, message):
        self.__get_alert().send_keys(message)

    def get_text(self):
        return self.__get_alert().text

    def is_alert_present(self):
        try:
            Swd.get_driver().switch_to.alert
            return True
        except NoAlertPresentException:
            return False
