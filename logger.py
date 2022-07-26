from datetime import datetime
from enum import Enum


class LogLevel(Enum):
    ERROR = 0
    WARN = 1
    INFO = 2
    DEBUG = 3


def error(message):
    log(message, LogLevel.ERROR)


def warn(message):
    log(message, LogLevel.WARN)


def info(message):
    log(message, LogLevel.INFO)


def debug(message):
    log(message, LogLevel.DEBUG)


def log(message, log_lvl):
    if log_lvl.value <= current_log_level.value:
        print(f'{current_time()} [{log_lvl.name}] {message}')


def current_time():
    return datetime.now().strftime("%H:%M:%S")


current_log_level = LogLevel.INFO
