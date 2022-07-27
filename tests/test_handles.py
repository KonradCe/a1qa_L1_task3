from task3.framework.utils import wait_utils
from task3.framework.utils.logger_utils import log_info
from task3.pages.links_page import LinksPage
from task3.pages.main_page import MainPage
from task3.pages.sample_page import SamplePage
from task3.pages.support_forms.left_pannel_menu import LeftPanelMenu
from task3.pages.windows_page import BrowserWindowsPage
from task3.framework import driver_utils as driver_utils


def test_case4(driver_setup_teardown):
    log_info("start of TEST CASE 4 - HANDLES")

    # STEP 1: navigate to main page
    # -> main page is open
    log_info("STEP 1: navigate to main page")
    main_page = MainPage()
    main_page.go_to_main_page()
    error_message_step1 = "opening main page should result in main page being open"
    assert main_page.is_open(), error_message_step1

    # STEP 2: Click on Alerts, Frame & Windows button; In the menu click a Browser Windows button
    # -> Page with Browser Windows form is open
    main_page.click_on_alert_frame_window_btn()
    left_menu = LeftPanelMenu()
    left_menu.click_on_button_from_category(
        button_name="Browser Windows", category_name="Frame"
    )
    windows_page = BrowserWindowsPage()
    error_message_step2 = "clicking on 'Browser Windows' button in the menu should open 'Browser Windows' page"
    assert windows_page.is_open(), error_message_step2
    windows_page.set_handle()

    # STEP 3: Click on New Tab button
    # -> New tab with sample page is open
    current_handle_list = driver_utils.get_handles()
    windows_page.click_new_tab_btn()
    wait_utils.wait_for_new_window_to_open(current_handle_list)
    driver_utils.switch_to_new_handle(current_handle_list)
    sample_page = SamplePage()
    error_message_step3 = "clicking on 'new tab' button should result in opening a new tab with a sample page"
    assert sample_page.is_open(), error_message_step3

    # STEP 4: Close current tab
    # -> Page with Browser Windows form is open
    driver_utils.close_current_window()
    driver_utils.switch_to_handle(windows_page.page_handle)
    error_message_step4 = "after closing tab with 'sample page' we should be back in 'Browser Windows' page"
    assert windows_page.is_open(), error_message_step4

    # STEP 5: In the menu on the left click Elements → Links button
    # -> Page with Links form is open
    left_menu.click_on_button_from_category(
        button_name="Links", category_name="Elements"
    )
    links_page = LinksPage()
    error_message_step5 = "clicking on links page in left panel menu should result in links page being open"
    assert links_page.is_open(), error_message_step5
    links_page.set_handle()

    # STEP 6: Click on Home link
    # -> New tab with main page is open
    current_handle_list = driver_utils.get_handles()
    links_page.click_on_home_link()
    wait_utils.wait_for_new_window_to_open(current_handle_list)
    driver_utils.switch_to_new_handle(current_handle_list)
    main_page = MainPage()
    error_message_step6 = (
        "clicking on Home link in 'Links' page should open 'Main Page' in a new tab"
    )
    assert main_page.is_open(), error_message_step6

    # STEP 7: Resume to previous tab
    # -> Page with Links form is open
    driver_utils.switch_to_handle(links_page.page_handle)
    error_message_step7 = (
        "switching back to 'Links' page tab should result in 'Links' page being open"
    )
    assert links_page.is_open(), error_message_step7


if __name__ == "__main__":
    test_case4(None)
