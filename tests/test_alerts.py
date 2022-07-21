from framework.singleton_driver import SingletonWebDriver as Swd

driver = Swd.get_driver()
driver.get('www.google.com')