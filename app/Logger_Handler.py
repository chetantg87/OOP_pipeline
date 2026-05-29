from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
import threading

class Formatter:

    @staticmethod
    def format(level, message):
        return f'{datetime.now().strftime(Logger.date_format)} [{level.name}]: {message} \n'

class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4

class Handler(ABC):

    def __init__(self):
        self.lock = threading.Lock()

    @abstractmethod
    def emit(self, message):
        pass

class FileHandler(Handler):

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def emit(self, message):
        with self.lock:
            with open(self.filename, 'a') as f:
                f.write(message)

class ConsoleHandler(Handler):

    def __init__(self):
        super().__init__()

    def emit(self, message):
        with self.lock:
            print(message)

class Logger:

    date_format = '%Y-%m-%d %H:%M:%S'

    def __init__(self, level=LogLevel.INFO):
        self.handlers = []
        self.level = level

    def add_handler(self, handler):
        self.handlers.append(handler)

    def set_level(self, level):
        self.level = LogLevel[level]

    def log(self, level, message):
        if level.value >= self.level.value:
            formatted_message = Formatter.format(level, message)
            for handler in self.handlers:
                handler.emit(message=formatted_message)

    def debug(self, message):
        self.log(LogLevel.DEBUG, message)

    def info(self, message):
        self.log(LogLevel.INFO, message)

    def warning(self, message):
        self.log(LogLevel.WARNING, message)

    def error(self, message):
        self.log(LogLevel.ERROR, message)

if __name__ == "__main__":

    logger = Logger()
    logger.set_level('ERROR')
    logger.add_handler(ConsoleHandler())

    logger.add_handler(FileHandler('log.txt'))

    logger.error("HELLO")

