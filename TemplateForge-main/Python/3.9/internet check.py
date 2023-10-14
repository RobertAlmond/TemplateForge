# Required modules: re, urllib

import re
import urllib.request
import urllib.error


def is_connected(attempts: int = 5, *sites: str or list[str]):
    """Checks if there is an internet connection.

    Args:
        attempts: The number of attempts to connect to each website.
        sites: A list of websites to check. If sites = None, sites = ['https://www.google.com',
                 'https://www.yahoo.com',
                 'https://www.bing.com',
                 'https://www.facebook.com',
                 'https://www.twitter.com',
                 'https://www.wikipedia.org', ]

    Returns:
        True if there is an internet connection, False otherwise.
    """
    if sites:
        for url in sites:
            if not re.match(r'^https?://.+$', url):
                raise ValueError(f'{url} is not a valid website address.')

    if not sites:
        sites = ['https://www.google.com',
                 'https://www.yahoo.com',
                 'https://www.bing.com',
                 'https://www.facebook.com',
                 'https://www.twitter.com',
                 'https://www.wikipedia.org', ]

    for url in sites:
        for _ in range(attempts):
            try:
                urllib.request.urlopen(url)
                return True
            except urllib.error.URLError:
                pass
                return False
