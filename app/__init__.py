from .Logger_Handler import Logger, FileHandler, LogLevel

logger = Logger()
logger.set_level('DEBUG')
logger.add_handler(FileHandler("logs.txt"))