import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

import framework.utils.config_data as config_utils


def create_driver(browser_name):

    browser_name = browser_name.lower()

    if browser_name == "chrome":
        return create_chrome_driver()

    elif browser_name == "firefox":
        return create_firefox_driver()

    elif browser_name == "edge":
        raise NotImplementedError(
            "this functionality will be implemented in future releases"
        )

    else:
        raise ValueError(f"{browser_name} is not supported")


def create_chrome_driver():
    options = webdriver.ChromeOptions()
    chrome_params = config_utils.get_chrome_params()
    for p in chrome_params:
        options.add_argument(p)
    chrome_driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    return chrome_driver


def create_firefox_driver():
    # specifying log_path as None stops the driver from creating log file every run, and sends display log output in console
    service = FirefoxService(GeckoDriverManager().install(), log_path=None)

    options = webdriver.FirefoxOptions()

    firefox_options_params = config_utils.get_firefox_options_params()
    for param in firefox_options_params:
        options.add_argument(param)

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile_prefs: dict = config_utils.get_firefox_profile_prefs()
    for pref, value in firefox_profile_prefs.items():
        firefox_profile.set_preference(pref, value)

    firefox_driver = webdriver.Firefox(
        service=service, options=options, firefox_profile=firefox_profile
    )
    return firefox_driver
