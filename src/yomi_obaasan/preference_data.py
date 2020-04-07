# -*- coding: utf-8 -*-

# Copyright (C) 2013  Alex Yatskov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



# The files in this addon may have been modified for CCBC, and may not be the same as the original.
# The files in this addon may have been modified for CCBC, and may not be the same as the original.
# The files in this addon may have been modified for CCBC, and may not be the same as the original.
# The files in this addon may have been modified for CCBC, and may not be the same as the original.


import codecs
import json
import operator
import os

from .config import Config


class Preferences(object):
    conf = Config("YomiObaasan")

    # def __init__(self):

    def __getitem__(self, name):
        return self.conf.get(name)

    def __setitem__(self, name, value):
        self.conf.set(name, value)

    def save(self):
        self.conf.save()


    def filePosition(self, filename):
        rfs = self.conf.get("recentFiles", [])
        matches = list(filter(lambda f: f['path'] == filename, rfs))
        return 0 if len(matches) == 0 else matches[0]['position']


    def recentFiles(self):
        rfs = self.conf.get("recentFiles", [])
        return [x['path'] for x in rfs]


    def updateFactTags(self, tags):
        tag_list = self.conf.get("tags", [])
        if tags in tag_list:
            tag_list.remove(tags)
        tag_list.insert(0, tags)


    def updateRecentFile(self, filename, position):
        rfs = self.conf.get("recentFiles", [])
        rfs = list(filter(lambda f: f['path'] != filename, rfs))
        rfs.insert(0, {'path': filename, 'position': position})
        self.conf.set("recentFiles", rfs)


    def clearRecentFiles(self):
        self.conf.set("recentFiles", [])
