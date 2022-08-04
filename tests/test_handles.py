from task3.framework.driver_utils import SingletonWebDriver as Swd
from task3.framework.utils.wait_utils import WaitUtils
from task3.framework.utils.logger_utils import LoggerUtils
from task3.pages.links_page import LinksPage
from task3.pages.main_page import MainPage
from task3.pages.sample_page import SamplePage
from task3.pages.support_forms.left_pannel_menu import LeftPanelMenu
from task3.pages.windows_page import BrowserWindowsPage


def test_switching_windows(driver_setup_teardown):
    LoggerUtils.log_info("start of TEST CASE 4 - HANDLES")

    # STEP 1: navigate to main page
    # -> main page is open
    LoggerUtils.log_info("STEP 1: navigate to main page")
    main_page = MainPage()
    main_page.go_to_main_page()
    error_message_step1 = "opening main page should result in main page being open"
    assert main_page.is_open(), error_message_step1

    # STEP 2: Click on Alerts, Frame & Windows button; In the menu click a Browser Windows button
    # -> Page with Browser Windows form is open
    LoggerUtils.log_info("STEP 2: Click on Alerts, Frame & Windows button...")
    main_page.click_on_alert_frame_window_btn()
    LoggerUtils.log_info("STEP 2: ... In the menu click a Browser Windows button")
    left_menu = LeftPanelMenu()
    left_menu.click_on_button_from_category(
        button_name="Browser Windows", category_name="Frame"
    )
    windows_page = BrowserWindowsPage()
    error_message_step2 = "clicking on 'Browser Windows' button in the menu should open 'Browser Windows' page"
    assert windows_page.is_open(), error_message_step2
    windows_page_handle = Swd.get_current_handle()

    # STEP 3: Click on New Tab button
    # -> New tab with sample page is open
    LoggerUtils.log_info("STEP 3: Click on New Tab button")
    current_handle_list = Swd.get_handles()
    windows_page.click_new_tab_btn()
    WaitUtils.wait_for_new_window_to_open(current_handle_list)
    Swd.switch_to_new_handle(current_handle_list)
    sample_page = SamplePage()
    error_message_step3 = "clicking on 'new tab' button should result in opening a new tab with a sample page"
    assert sample_page.is_open(), error_message_step3

    # STEP 4: Close current tab
    # -> Page with Browser Windows form is open
    LoggerUtils.log_info("STEP 4: Close current tab")
    Swd.close_current_window()
    Swd.switch_to_handle(windows_page_handle)
    error_message_step4 = "after closing tab with 'sample page' we should be back in 'Browser Windows' page"
    assert windows_page.is_open(), error_message_step4

    # STEP 5: In the menu on the left click Elements → Links button
    # -> Page with Links form is open
    LoggerUtils.log_info(
        "STEP 5: In the menu on the left click Elements → Links button"
    )
    left_menu.click_on_button_from_category(
        button_name="Links", category_name="Elements"
    )
    links_page = LinksPage()
    error_message_step5 = "clicking on links page in left panel menu should result in links page being open"
    assert links_page.is_open(), error_message_step5
    links_page_handle = Swd.get_current_handle()

    # STEP 6: Click on Home link
    # -> New tab with main page is open
    LoggerUtils.log_info("STEP 6: Click on Home link")
    current_handle_list = Swd.get_handles()
    links_page.click_on_home_link()
    WaitUtils.wait_for_new_window_to_open(current_handle_list)
    Swd.switch_to_new_handle(current_handle_list)
    main_page = MainPage()
    error_message_step6 = (
        "clicking on Home link in 'Links' page should open 'Main Page' in a new tab"
    )
    assert main_page.is_open(), error_message_step6

    # STEP 7: Resume to previous tab
    # -> Page with Links form is open
    LoggerUtils.log_info("STEP 7: Resume to previous tab")
    Swd.switch_to_handle(links_page_handle)
    error_message_step7 = (
        "switching back to 'Links' page tab should result in 'Links' page being open"
    )
    assert links_page.is_open(), error_message_step7


if __name__ == "__main__":
    test_case4(None)
