import logging, colorlog

# Define a logger
main_logger = logging.getLogger()
main_logger.setLevel(logging.DEBUG)

# Set up a stream handler to log to the console
stream_handler = colorlog.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# Format log message
formatter = colorlog.ColoredFormatter(
    "%(blue)s%(asctime)s %(white)s[%(log_color)s%(levelname)-8s%(white)s] %(white)s%(message)s"
)
stream_handler.setFormatter(formatter)

# Add handler to logger
main_logger.addHandler(stream_handler)
