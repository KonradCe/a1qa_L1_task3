import json
import random
import string
from pathlib import Path


test_data_file_path = Path(Path.cwd(), "task3/data/test_data.json")


def get_main_page_url() -> str:
    with open(test_data_file_path) as f:
        j = json.load(f)
    return j["main_page_url"]


def generate_random_string() -> str:
    letters = string.ascii_letters
    length = random.randrange(3, 20)
    random_list = [random.choice(letters) for i in range(length)]
    return "".join(random_list)
