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

import utils
import datetime

sources = ["https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
           "http://adblock.gjtech.net/?format=unix-hosts",
           "http://mirror1.malwaredomains.com/files/justdomains",
           "http://sysctl.org/cameleon/hosts",
           "https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist",
           "https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt",
           "https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt",
           "http://hosts-file.net/ad_servers.txt"]


class AdList:
    """Base AdList class"""
    def __init__(self, uri):
        self.uri = uri
        self.modified_date = utils.get_last_modified(uri)
        self.creation_date = datetime.datetime.now()

    def __str__(self):
        return '{} created on {}. Last Modified on {}'.format(self.uri, self.creation_date, self.modified_date)

    def get_modified_date(self):
        return self.modified_date

    def get_creation_date(self):
        return self.creation_date

    def get_uri(self):
        return self.uri


class BlockLists:
    """Collection of AdLists"""
    def __init__(self):
        self.block_lists = []

    def new_block_list(self, uri):
        self.block_lists.append(AdList(uri))

b = BlockLists()
for source in sources:
    b.new_block_list(source)

for l in b.block_lists:
    print(l)


