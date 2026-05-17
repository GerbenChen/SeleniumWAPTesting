import logging

from utils.artifact_manager import (
    artifact_manager
)


LOG_FILE = (
    artifact_manager.log_path(
        "test_execution"
    )
)


def get_logger() -> logging.Logger:

    logger = logging.getLogger(
        "wap_test"
    )

    if logger.handlers:

        return logger

    logger.setLevel(
        logging.INFO
    )

    formatter = logging.Formatter(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(filename)s:%(lineno)d | "
        "%(message)s"
    )

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    file_handler.setFormatter(
        formatter
    )

    stream_handler = logging.StreamHandler()

    stream_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        file_handler
    )

    logger.addHandler(
        stream_handler
    )

    logger.propagate = False

    return logger