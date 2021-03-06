import logging
import sys


def configure_logging():
    # create a stdout handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logging.basicConfig(
        handlers=[handler],
        level=logging.DEBUG,
    )
