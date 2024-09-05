import logging
import os
import time



def logGen():
    logging.basicConfig(filename='logs/logger.log', format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%m %d %Y : %H %M %S', filemode='w')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger


# def logGen():
#     logging.basicConfig(filename=f'logs/log_{time.strftime('%Y %m %d_%H %M %S')}.log',format='%(asctime)s %(levelname)s %(message)s',datefmt='%m %d %Y %H %M %S', filemode='w')
#
#     log_directory = "logs"
#     if not os.path.exists(log_directory):
#         os.makedirs(log_directory)
#
#     # Configure the logging
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.INFO)
#
#     file_handler = logging.FileHandler(f"logs\\log_{time.strftime('%Y%m%d_%H%M%S')}.log", mode="w")
#     file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
#     logger.addHandler(file_handler)
#
#     return logger
