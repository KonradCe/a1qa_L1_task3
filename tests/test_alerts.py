from framework.driver_utils import SingletonWebDriver as Swd

driver = Swd.get_driver()
driver.get("https://store.steampowered.com/")
