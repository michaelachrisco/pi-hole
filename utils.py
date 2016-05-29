# Pi-hole: A black hole for Internet advertisements
# (c) 2015, 2016 by Jacob Salmela
# Network-wide ad blocking via your Raspberry Pi
# http://pi-hole.net
# Pi-hole gravity function to download, aggregate, and parse source lists
#
# Pi-hole is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

import requests


def get_last_modified(url):
    """Request headers from url and return Last-Modified date.
       Return None if Last-Modified header is not available"""
    r = requests.head(url)
    try:
        date = r.headers['Last-Modified']
    except KeyError:
        date = None
    return date

