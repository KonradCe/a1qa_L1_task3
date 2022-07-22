import framework.browser_factory


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
    def get_driver(cls, browser_name="Chrome"):
        if cls.__driver is None:
            cls.__driver = framework.browser_factory.create_driver(browser_name)
        return cls.__driver

    def unassign_driver(self):
        self.__driver = None


def go_to_page(url):
    SingletonWebDriver.get_driver().get(url)


def go_back():
    SingletonWebDriver.get_driver().back()


def go_forward():
    SingletonWebDriver.get_driver().forward()


def refresh_page():
    SingletonWebDriver.get_driver().refresh()
