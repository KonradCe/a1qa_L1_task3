from selenium import webdriver

import task3.framework.browser_factory
from task3.framework.utils.logger_utils import log_info, log_debug


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class SingletonWebDriver(metaclass=Singleton):
    __driver = None

    @classmethod
    def get_driver(cls, browser_name="chrome") -> webdriver:
        if cls.__driver is None:
            cls.__driver = task3.framework.browser_factory.create_driver(browser_name)
        return cls.__driver

    @classmethod
    def unassign_driver(cls):
        cls.__driver = None


def go_to_page(url):
    log_info(f"driver - go to page {url}")
    SingletonWebDriver.get_driver().get(url)


def go_back():
    log_info(f"driver - navigate back")
    SingletonWebDriver.get_driver().back()


def go_forward():
    log_info(f"driver - navigate forward")
    SingletonWebDriver.get_driver().forward()


def refresh_page():
    log_info(f"driver - refresh page")
    SingletonWebDriver.get_driver().refresh()


def driver_quit():
    log_info(f"driver - quit")
    SingletonWebDriver.get_driver().quit()


def unassing_driver():
    log_debug(f"driver - set driver variable to null")
    SingletonWebDriver.unassign_driver()


def get_current_handle():
    return SingletonWebDriver.get_driver().current_window_handle


def get_handles():
    return SingletonWebDriver.get_driver().window_handles


def switch_to_handle(handle):
    log_info(f"driver - switching windows")
    SingletonWebDriver.get_driver().switch_to.window(handle)


def switch_to_new_handle(old_handle_list):
    new_handle_list = get_handles()
    for possible_new_handle in new_handle_list:
        if possible_new_handle not in old_handle_list:
            switch_to_handle(possible_new_handle)


def close_current_window():
    log_info(f"driver - close current window")
    SingletonWebDriver.get_driver().close()
