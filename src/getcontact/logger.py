from datetime import datetime
from getcontact.config import config


class Log:
    @staticmethod
    def d(*args):
        if config.VERBOSE:
            print(
                datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"),
                " ".join([str(arg) for arg in args]),
            )

    @staticmethod
    def error(*args):
        if config.VERBOSE:
            print(
                datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"),
                "error",
                " ".join([str(arg) for arg in args]),
            )
