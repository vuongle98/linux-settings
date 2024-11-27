import logging


class Logger:
    def __init__(self, level):
        self.level = level
        self.logger = logging.getLogger(__name__)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def warning(self, msg):
        self.logger.warning(msg)