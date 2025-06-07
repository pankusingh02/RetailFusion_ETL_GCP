import logging
import sys

def get_logger(name: str) -> logging.Logger:
    logger=logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler=logging.StreamHandler(sys.stdout)

    formatter= logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')

    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    logger.propagate= False

    return logger