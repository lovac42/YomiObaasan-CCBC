#!/usr/bin/env python2
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




from PyQt4 import QtGui
from . import japanese
from .anki_connect import AnkiConnect
from .preference_data import Preferences
from .reader import MainWindowReader
import sys


class Yomichan:
    def __init__(self):
        self.language = japanese.initLanguage()

        self.preferences = Preferences()


class YomichanPlugin(Yomichan):
    def __init__(self):
        Yomichan.__init__(self)

        self.toolIconVisible = False
        self.window          = None
        self.anki            = anki_bridge.Anki()
        self.parent          = self.anki.window()
        self.ankiConnect     = AnkiConnect(self.anki, self.preferences)

        separator = QtGui.QAction(self.parent)
        separator.setSeparator(True)
        self.anki.addUiAction(separator)

        action = QtGui.QAction(QtGui.QIcon(':/img/img/icon_logo_32.png'), '&YomiObaasan...', self.parent)
        action.setIconVisibleInMenu(True)
        action.setShortcut('Ctrl+Y')
        action.triggered.connect(self.onShowRequest)
        self.anki.addUiAction(action)


    def onShowRequest(self):
        if self.window:
            self.window.setVisible(True)
            self.window.activateWindow()
        else:
            self.window = MainWindowReader(
                self.parent,
                self.preferences,
                self.language,
                None,
                self.anki,
                self.onWindowClose
            )
            self.window.show()


    def onWindowClose(self):
        self.window = None

