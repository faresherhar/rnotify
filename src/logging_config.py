import logging

# Define a logger
main_logger = logging.getLogger()
main_logger.setLevel(logging.DEBUG)

# Set up a stream handler to log to the console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# Format log message
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
stream_handler.setFormatter(formatter)

# Add handler to logger
main_logger.addHandler(stream_handler)
