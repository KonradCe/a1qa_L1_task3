from task3.pages.main_page import MainPage


def test_case1(driver_setup_teardown):
    # STEP 1: navigate to main page -> main page is open
    main_page = MainPage()
    main_page.go_to_main_page()
    error_message_step1 = "opening main page should result in main page being open"
    assert main_page.is_open(), error_message_step1

    # STEP 2: Click on Alerts, Frame & Windows button. In a menu click Alerts button. ->
    # Alerts form has appeared on page
    main_page.click_on_alert_frame_window_btn()
    main_page.click_on_alert_btn_in_menu()
    error_message_step2 = (
        "clicking on alerts button in the menu should show form to test alerts"
    )
    assert main_page.is_alerts_form_open(), error_message_step2

    # STEP 3: Click on Click Button to see alert button	-> Alert with text "You clicked a button" is open


if __name__ == "__main__":
    test_case1(None)
