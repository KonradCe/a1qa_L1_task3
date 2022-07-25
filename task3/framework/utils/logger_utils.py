import logging


def logger_setup():
    logging.basicConfig(
        filename="my_log.log",
        level=logging.INFO,
        encoding="utf-8",
        force=True,
        format="%(asctime)s\t%(levelname)s\t%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def log_info(message):
    logging.info(message)


def log_warning(message):
    logging.warning(message)
