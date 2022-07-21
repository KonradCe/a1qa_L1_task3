import json

config_data_file_path = "../../data/config_data.json"


def get_chrome_parameters_() -> list:
    with open(config_data_file_path) as f:
        j = json.load(f)
        chrome_parameters = [*j["chrome_options"]]
    return chrome_parameters
