import logging


class LoggerUtils:
    @staticmethod
    def logger_setup():
        # TODO: logger params should be put into logger_data.json
        logging.basicConfig(
            filename="my_log.log",
            level=logging.INFO,
            # encoding="utf-8",
            force=True,
            format="%(asctime)s\t%(levelname)s\t%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
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
