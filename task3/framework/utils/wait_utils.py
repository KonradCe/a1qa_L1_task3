import selenium.webdriver.common.alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from task3.framework.driver_utils import SingletonWebDriver as Swd
from task3.framework.utils.config_data_utils import get_explicit_wait_time


def wait_for_alert() -> selenium.webdriver.common.alert.Alert:
    wait = WebDriverWait(Swd.get_driver(), get_explicit_wait_time())
    alert = wait.until(EC.alert_is_present())
    return alert
