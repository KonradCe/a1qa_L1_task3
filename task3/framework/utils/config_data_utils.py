import json
from pathlib import Path

config_data_file_path = Path(Path.cwd(), "task3/data/config_data.json")


def get_browser_of_choice():
    with open(config_data_file_path) as f:
        j = json.load(f)
        browser = j["browser"]
    return browser


def get_chrome_params() -> list:
    with open(config_data_file_path) as f:
        j = json.load(f)
        chrome_parameters = [*j["chrome_params"]]
    return chrome_parameters


def get_firefox_options_params() -> list:
    with open(config_data_file_path) as f:
        j = json.load(f)
        options_params = [*j["firefox_options_params"]]
    return options_params


def get_firefox_profile_prefs() -> dict:
    with open(config_data_file_path) as f:
        j = json.load(f)
        profile_prefs = j["firefox_profile_prefs"]
    return profile_prefs
