from enum import Enum
from abc import ABC, abstractmethod
from app import logger

class Task(ABC):

    def __init__(self):
        self.logger = logger

    @abstractmethod
    def run(self, ro: dict):
        pass


class TaskStatus(Enum):
    PENDING = 0
    RUNNING = 1
    SUCCESS = 2
    FAILED = 3