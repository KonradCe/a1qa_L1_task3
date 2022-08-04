from task3.framework.utils.logger_utils import LoggerUtils
from task3.pages.alerts_page import AlertsPage
from task3.pages.main_page import MainPage
from task3.pages.support_forms.left_pannel_menu import LeftPanelMenu


def test_alerts(driver_setup_teardown):
    desired_string_step3 = "You clicked a button"
    desired_string_step5 = "Do you confirm action?"
    desired_string_step7 = "Please enter your name"

    LoggerUtils.log_info("start of TEST CASE 1 - ALERTS")
    # STEP 1: navigate to main page
    # -> main page is open
    LoggerUtils.log_info("STEP 1: navigate to main page")
    main_page = MainPage()
    main_page.go_to_main_page()
    error_message_step1 = "opening main page should result in main page being open"
    assert main_page.is_open(), error_message_step1

    # STEP 2: Click on Alerts, Frame & Windows button. In a menu click Alerts button.
    # -> Alerts form has appeared on page
    LoggerUtils.log_info("STEP 2: Click on Alerts, Frame & Windows button...")
    main_page.click_on_alert_frame_window_btn()

    alerts_page = AlertsPage()
    LoggerUtils.log_info("STEP 2: ...In a menu click Alerts button.")
    left_menu = LeftPanelMenu()
    left_menu.click_on_button_from_category(button_name="Alerts", category_name="Frame")
    error_message_step2 = (
        "clicking on alerts button in the menu should show form to test alerts"
    )
    assert alerts_page.is_open(), error_message_step2

    # STEP 3: Click on 'Click Button to see alert' button
    # -> Alert with text "You clicked a button" is open
    LoggerUtils.log_info("STEP 3: Click on 'Click Button to see alert' button")
    alerts_page.click_on_alert_button()
    error_message_step3 = "clicking on alerts button should prompt an alert with 'You clicked a button' text."
    assert alerts_page.alert_with_text_is_open(
        desired_string_step3
    ), error_message_step3

    # STEP 4: Click OK button
    # -> alert has closed
    LoggerUtils.log_info("STEP 4: Click OK button")
    alerts_page.accept_alert()
    error_message_step4 = "Accepting the alert should cause alert to close"
    assert alerts_page.alert_is_closed(), error_message_step4

    # STEP 5: Click on 'On button click, confirm box will appear' button
    # -> 'Alert with text "Do you confirm action?" is open'
    LoggerUtils.log_info(
        "STEP 5: Click on 'On button click, confirm box will appear' button"
    )
    alerts_page.click_on_confirmation_btn()
    error_message_step5 = (
        "clicking on 'On button click, confirm box will appear button' should prompt a "
        "confirmation box, with 'Do you confirm action?' text"
    )
    assert alerts_page.alert_with_text_is_open(
        desired_string_step5
    ), error_message_step5

    # STEP 6: Click on OK button
    # -> Alert has closed
    # -> Text "You selected Ok" has appeared on page
    LoggerUtils.log_info("STEP 6: Click on OK button")
    alerts_page.accept_alert()
    error_message_step6a = (
        "accepting confirmation box should result close the confirmation window"
    )
    error_message_step6b = (
        "accepting confirmation box should display 'you selected OK' text"
    )

    assert alerts_page.alert_is_closed(), error_message_step6a
    assert alerts_page.positive_confirmation_msg_exist(), error_message_step6b

    # STEP 7: Click on "On button click, prompt box will appear" button
    # -> Alert with text "Please enter your name" is open
    LoggerUtils.log_info(
        "STEP 7: Click on 'On button click, prompt box will appear' button"
    )
    alerts_page.click_on_prompt_btn()
    error_message_step7 = (
        "clicking on 'On button click, prompt box will appear' should trigger a "
        "prompt, with 'Please enter your name' text"
    )
    assert alerts_page.alert_with_text_is_open(
        desired_string_step7
    ), error_message_step7

    # STEP 8: Enter randomly generated text, click OK button
    # -> Alert has closed
    # -> Appeared text equals to the one you've entered before
    LoggerUtils.log_info("STEP 8: Enter randomly generated text, click OK button...")
    text_input = alerts_page.send_random_input_to_prompt()
    LoggerUtils.log_info("STEP 8: ...click OK button")
    alerts_page.accept_alert()
    error_message_step8 = (
        "entering random input and accepting the prompt should result in 2 things: "
        "closing of the prompt and a messaged with entered text next to the button"
    )
    assert alerts_page.alert_is_closed(), error_message_step8
    assert alerts_page.prompt_confirmation_msg_with_text_exist(
        text_input
    ), error_message_step8
