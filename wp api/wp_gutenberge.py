"""
Wordpress Rest Api Simple Wrapper for python
A simple python wrapper for the 6.0 version of wordpress
"""
from .errors import InvalidArgumentException


class WpApi:
    """
    Provides methods to get information about wordpress api credentials

    Args:
        site_url(`str`): Your website url
        username('str'): You website user name
        password('str'): You website authentication key

    Raises: Invalid Argument Exceptions
    """

    def __init__(self, site_url: str, username: str, password: str):
        self.site_url = site_url
        self.username = username
        self.password = password




