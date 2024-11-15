import logging
from rich.logging import RichHandler

class Logger:
    def __init__(self):
        FORMAT = "%(message)s"
        logging.basicConfig(
            level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
        )
        self.log = logging.getLogger("rich")
