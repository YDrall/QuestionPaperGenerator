"""
This module contains all the application level exceptions.
"""

CODE_BAD_DATA = 400


class InvalidAttributeError(ValueError):
    def __init__(self, message, *args, **kwargs):
        self.code = CODE_BAD_DATA
        self.message = message
        super().__init__(message, args, kwargs)


class InvalidArgumentError(Exception):
    def __init__(self, message, *args, **kwargs):
        self.code = CODE_BAD_DATA
        self.message = message
        super().__init__(message, args, kwargs)
