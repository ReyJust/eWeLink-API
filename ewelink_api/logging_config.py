import coloredlogs, logging

logger = logging.getLogger("eWeLinkAPI")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(name)s - %(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

# Apply coloredlogs with the custom format
coloredlogs.install(level='DEBUG', logger=logger, fmt="%(asctime)s | %(name)s | [%(levelname)s] - %(message)s")

# Examples log messages
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.critical("This is a critical message")


# file_handler = logging.FileHandler('sdk.log')
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
