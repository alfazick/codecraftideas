# Logging and Monitoring: Implement detailed logging and monitoring 
# to detect and respond to unusual activities or errors in real-time.

# 1. Easy: Basic Logging Setup

import logging

# Basic confguration for logging

logging.basicConfig(level = logging.INFO,
                    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename ='custom_log.log',
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logging.info("This is an info message")
logging.warning("This is a warning message")

# 2. Medium: Logging with Different Levels and Modules

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler which logs debug messages
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)

# Create a console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug("This message should go the debug log file")
logger.error("This should appear in the console")

# 3. Hard: Implementing a Custom Logging Handler

# this could be for sending logs to a third service, a database

import logging 
class CustomHandler(logging.Handler):
    def emit(self,record):
        log_entry = self.format(record)
        # do with the log anything you want
        print(f"Custom log handler: {log_entry}")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = CustomHandler()
logger.addHandler(ch)

logger.info("This is a test message for the custom handler")


