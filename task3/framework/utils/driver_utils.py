from selenium import webdriver

from task3.framework.browser_factory import BrowserFactory
from task3.framework.utils.logger_utils import LoggerUtils


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonWebDriver(metaclass=SingletonMeta):
    __driver = None

    @classmethod
    def get_driver(cls, browser_name="chrome") -> webdriver:
        if cls.__driver is None:
            cls.__driver = BrowserFactory().create_driver(browser_name)
        return cls.__driver

    @classmethod
    def unassign_driver(cls):
        cls.__driver = None

    @classmethod
    def go_to_page(cls, url):
        LoggerUtils.log_info(f"driver - go to page {url}")
        cls.get_driver().get(url)

    @classmethod
    def go_back(cls):
        LoggerUtils.log_info(f"driver - navigate back")
        cls.get_driver().back()

    @classmethod
    def go_forward(cls):
        LoggerUtils.log_info(f"driver - navigate forward")
        cls.get_driver().forward()

    @classmethod
    def refresh_page(cls):
        LoggerUtils.log_info(f"driver - refresh page")
        cls.get_driver().refresh()

    @classmethod
    def driver_quit(cls):
        LoggerUtils.log_info(f"driver - quit")
        cls.get_driver().quit()

    @classmethod
    def get_current_handle(cls):
        return cls.get_driver().current_window_handle

    @classmethod
    def get_handles(cls):
        return cls.get_driver().window_handles

    @classmethod
    def switch_to_handle(cls, handle):
        LoggerUtils.log_info(f"driver - switching windows")
        cls.get_driver().switch_to.window(handle)

    @classmethod
    def switch_to_new_handle(cls, old_handle_list):
        new_handle_list = cls.get_handles()
        for possible_new_handle in new_handle_list:
            if possible_new_handle not in old_handle_list:
                cls.switch_to_handle(possible_new_handle)

    @classmethod
    def close_current_window(cls):
        LoggerUtils.log_info(f"driver - close current window")
        cls.get_driver().close()
