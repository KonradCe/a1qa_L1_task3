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
    def get_driver(cls, browser_name=''):
        if cls.__driver is None:
            cls.__driver = framework.browser_factory.create_driver(browser_name)
        return cls.__driver

    def unassign_driver(self):
        self.__driver = None
