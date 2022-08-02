from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from task3.framework.utils import config_data_utils


class BrowserFactory:
    def create_driver(self, browser_name):

        browser_name = browser_name.lower()

        if browser_name == "chrome":
            return self.create_chrome_driver()

        elif browser_name == "firefox":
            return self.create_firefox_driver()

        elif browser_name == "edge":
            raise NotImplementedError(
                "this functionality will be implemented in future releases"
            )

        else:
            raise ValueError(f"{browser_name} is not supported")

    def create_chrome_driver(self):
        options = webdriver.ChromeOptions()
        chrome_params = config_data_utils.get_chrome_params()
        for p in chrome_params:
            options.add_argument(p)
        chrome_driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )
        return chrome_driver

    def create_firefox_driver(self):
        # specifying log_path as None stops the driver from creating log file every run,
        # and displays log output in the console
        service = FirefoxService(GeckoDriverManager().install(), log_path=None)

        options = webdriver.FirefoxOptions()

        firefox_options_params = config_data_utils.get_firefox_options_params()
        for param in firefox_options_params:
            options.add_argument(param)

        firefox_option_prefs: dict = config_data_utils.get_firefox_options_prefs()
        for pref, value in firefox_option_prefs.items():
            options.set_preference(pref, value)

        firefox_driver = webdriver.Firefox(service=service, options=options)
        return firefox_driver
