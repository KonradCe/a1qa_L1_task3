import json
import logging
from pathlib import Path


class LoggerUtils:
    logger_data_filepath = (
        Path(__file__).resolve().parents[2] / "data" / "logger_data.json"
    )

    @staticmethod
    def logger_setup():
        logging.basicConfig(
            filename=LoggerUtils.get_filename(),
            level=LoggerUtils.get_logging_level(),
            force=LoggerUtils.get_force_boolean(),
            format=LoggerUtils.get_format(),
            datefmt=LoggerUtils.get_date_format(),
        )

    @staticmethod
    def log_debug(message):
        logging.debug(message)

    @staticmethod
    def log_info(message):
        logging.info(message)

    @staticmethod
    def log_warning(message):
        logging.warning(message)

    @classmethod
    def get_filename(cls):
        with open(cls.logger_data_filepath) as f:
            j = json.load(f)
        return j["filename"]

    @classmethod
    def get_format(cls):
        with open(cls.logger_data_filepath) as f:
            j = json.load(f)
        return j["format"]

    @classmethod
    def get_date_format(cls):
        with open(cls.logger_data_filepath) as f:
            j = json.load(f)
        return j["datefmt"]

    @classmethod
    def get_logging_level(cls):
        with open(cls.logger_data_filepath) as f:
            j = json.load(f)
            level = j["level"].lower()

        if level == "critical;" or level == "fatal":
            return logging.CRITICAL
        elif level == "error":
            return logging.ERROR
        elif level == "warning" or level == "warn":
            return logging.WARNING
        elif level == "info":
            return logging.INFO
        elif level == "debug":
            return logging.DEBUG
        else:
            return logging.NOTSET

    @classmethod
    def get_force_boolean(cls):
        with open(cls.logger_data_filepath) as f:
            j = json.load(f)
        return j["force"]
