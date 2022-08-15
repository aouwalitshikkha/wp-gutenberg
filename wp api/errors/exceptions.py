"""Custom exceptions module"""

class WordpressException(Exception):
    """Common base class for all Wordpress API exceptions."""
    def __init__(self, reason: str):
        super().__init__()
        self.reason = reason

    def __str__(self) -> str:
        return '%s' % self.

class InvalidArgumentException(WordpressException):
    """Raised when arguments are not correct."""
    pass
