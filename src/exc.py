class EmptyConfigError(Exception):
    def __str__(self):
        return "Configuration File is Empty."
