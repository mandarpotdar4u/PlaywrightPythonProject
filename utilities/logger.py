import logging


def logGen():
    logging.basicConfig(filename='Logs/logger.log', format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%m %d %Y : %H %M %S', filemode='w')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger
