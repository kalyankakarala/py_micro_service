import sys
import logging


class AppLogger:

    def init_handlers(self):
        formatter = logging.Formatter(
            '[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s [%(threadName)s] - %(message)s')
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logger = logging.getLogger('root')
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
