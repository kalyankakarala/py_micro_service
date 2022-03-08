import logging


class AppService:
    logger = logging.getLogger('root')

    def __init__(self):
        self.logger.info("init app...")

    def start(self):
        self.logger.info("starting the app...")