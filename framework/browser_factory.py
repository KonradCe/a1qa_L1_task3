from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import framework.utils.config_data


def create_driver(browser_name="chrome"):

    browser_name = browser_name.lower()

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        chrome_params = framework.utils.config_data.get_chrome_parameters_()
        for p in chrome_params:
            options.add_argument(p)
        chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        return chrome_driver

    elif browser_name == "firefox":
        # TODO: implement creating firefox driver
        pass

    elif browser_name == "edge":
        raise NotImplementedError("this functionality will be implemented in future releases")

    else:
        raise ValueError(f"{browser_name} is not supported")
