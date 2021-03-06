# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtGui as QtWidgets



class Ui_MainWindowReader(object):
    def setupUi(self, MainWindowReader):
        MainWindowReader.setObjectName("MainWindowReader")
        MainWindowReader.resize(900, 650)
        MainWindowReader.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/icon_logo_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowReader.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindowReader)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textContent = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textContent.setMouseTracking(True)
        self.textContent.setReadOnly(True)
        self.textContent.setObjectName("textContent")
        self.verticalLayout_4.addWidget(self.textContent)
        MainWindowReader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowReader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpenRecent = QtWidgets.QMenu(self.menuFile)
        self.menuOpenRecent.setObjectName("menuOpenRecent")
        self.menuImport = QtWidgets.QMenu(self.menuFile)
        self.menuImport.setObjectName("menuImport")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTextSize = QtWidgets.QMenu(self.menuView)
        self.menuTextSize.setObjectName("menuTextSize")
        MainWindowReader.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindowReader)
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        self.toolBar.setObjectName("toolBar")
        MainWindowReader.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockVocab = QtWidgets.QDockWidget(MainWindowReader)
        self.dockVocab.setObjectName("dockVocab")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textVocabDefs = QtWidgets.QTextBrowser(self.dockWidgetContents)
        self.textVocabDefs.setAcceptDrops(False)
        self.textVocabDefs.setOpenLinks(False)
        self.textVocabDefs.setObjectName("textVocabDefs")
        self.verticalLayout.addWidget(self.textVocabDefs)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.textVocabSearch = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.textVocabSearch.setObjectName("textVocabSearch")
        self.horizontalLayout_3.addWidget(self.textVocabSearch)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.dockVocab.setWidget(self.dockWidgetContents)
        MainWindowReader.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockVocab)
        self.statusBar = QtWidgets.QStatusBar(MainWindowReader)
        self.statusBar.setObjectName("statusBar")
        MainWindowReader.setStatusBar(self.statusBar)
        self.dockAnki = QtWidgets.QDockWidget(MainWindowReader)
        self.dockAnki.setObjectName("dockAnki")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listDefinitions = QtWidgets.QListWidget(self.dockWidgetContents_2)
        self.listDefinitions.setObjectName("listDefinitions")
        self.verticalLayout_2.addWidget(self.listDefinitions)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboTags = QtWidgets.QComboBox(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboTags.sizePolicy().hasHeightForWidth())
        self.comboTags.setSizePolicy(sizePolicy)
        self.comboTags.setEditable(True)
        self.comboTags.setObjectName("comboTags")
        self.horizontalLayout_2.addWidget(self.comboTags)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.dockAnki.setWidget(self.dockWidgetContents_2)
        MainWindowReader.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockAnki)
        self.dockKanji = QtWidgets.QDockWidget(MainWindowReader)
        self.dockKanji.setObjectName("dockKanji")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textKanjiDefs = QtWidgets.QTextBrowser(self.dockWidgetContents_3)
        self.textKanjiDefs.setAcceptDrops(False)
        self.textKanjiDefs.setOpenLinks(False)
        self.textKanjiDefs.setObjectName("textKanjiDefs")
        self.verticalLayout_3.addWidget(self.textKanjiDefs)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.textKanjiSearch = QtWidgets.QLineEdit(self.dockWidgetContents_3)
        self.textKanjiSearch.setObjectName("textKanjiSearch")
        self.horizontalLayout_4.addWidget(self.textKanjiSearch)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.dockKanji.setWidget(self.dockWidgetContents_3)
        MainWindowReader.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockKanji)
        self.actionOpen = QtWidgets.QAction(MainWindowReader)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/icon_action_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(MainWindowReader)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/icon_action_quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setIconVisibleInMenu(True)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPreferences = QtWidgets.QAction(MainWindowReader)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img/icon_action_preferences.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon3)
        self.actionPreferences.setIconVisibleInMenu(True)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAbout = QtWidgets.QAction(MainWindowReader)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/img/icon_action_about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon4)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName("actionAbout")
        self.actionZoomIn = QtWidgets.QAction(MainWindowReader)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/img/icon_action_zoom_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomIn.setIcon(icon5)
        self.actionZoomIn.setIconVisibleInMenu(True)
        self.actionZoomIn.setObjectName("actionZoomIn")
        self.actionZoomOut = QtWidgets.QAction(MainWindowReader)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/img/icon_action_zoom_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomOut.setIcon(icon6)
        self.actionZoomOut.setIconVisibleInMenu(True)
        self.actionZoomOut.setObjectName("actionZoomOut")
        self.actionZoomReset = QtWidgets.QAction(MainWindowReader)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/img/icon_action_zoom_reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomReset.setIcon(icon7)
        self.actionZoomReset.setIconVisibleInMenu(True)
        self.actionZoomReset.setObjectName("actionZoomReset")
        self.actionFind = QtWidgets.QAction(MainWindowReader)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/img/icon_action_find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon8)
        self.actionFind.setIconVisibleInMenu(True)
        self.actionFind.setObjectName("actionFind")
        self.actionFindNext = QtWidgets.QAction(MainWindowReader)
        self.actionFindNext.setObjectName("actionFindNext")
        self.actionToggleWrap = QtWidgets.QAction(MainWindowReader)
        self.actionToggleWrap.setCheckable(True)
        self.actionToggleWrap.setChecked(True)
        self.actionToggleWrap.setObjectName("actionToggleWrap")
        self.actionToggleVocab = QtWidgets.QAction(MainWindowReader)
        self.actionToggleVocab.setCheckable(True)
        self.actionToggleVocab.setObjectName("actionToggleVocab")
        self.actionHomepage = QtWidgets.QAction(MainWindowReader)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/img/img/icon_action_homepage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHomepage.setIcon(icon9)
        self.actionHomepage.setIconVisibleInMenu(True)
        self.actionHomepage.setObjectName("actionHomepage")
        self.actionToggleAnki = QtWidgets.QAction(MainWindowReader)
        self.actionToggleAnki.setCheckable(True)
        self.actionToggleAnki.setObjectName("actionToggleAnki")
        self.actionFeedback = QtWidgets.QAction(MainWindowReader)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/img/img/icon_action_feedback.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFeedback.setIcon(icon10)
        self.actionFeedback.setObjectName("actionFeedback")
        self.actionToggleKanji = QtWidgets.QAction(MainWindowReader)
        self.actionToggleKanji.setCheckable(True)
        self.actionToggleKanji.setObjectName("actionToggleKanji")
        self.actionKindleDeck = QtWidgets.QAction(MainWindowReader)
        self.actionKindleDeck.setObjectName("actionKindleDeck")
        self.actionWordList = QtWidgets.QAction(MainWindowReader)
        self.actionWordList.setObjectName("actionWordList")
        self.menuImport.addAction(self.actionKindleDeck)
        self.menuImport.addAction(self.actionWordList)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuOpenRecent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFindNext)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menuTextSize.addAction(self.actionZoomIn)
        self.menuTextSize.addAction(self.actionZoomOut)
        self.menuTextSize.addSeparator()
        self.menuTextSize.addAction(self.actionZoomReset)
        self.menuView.addAction(self.menuTextSize.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionToggleAnki)
        self.menuView.addAction(self.actionToggleVocab)
        self.menuView.addAction(self.actionToggleKanji)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionToggleWrap)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoomIn)
        self.toolBar.addAction(self.actionZoomOut)
        self.toolBar.addAction(self.actionZoomReset)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFind)

        self.retranslateUi(MainWindowReader)
        self.actionToggleVocab.toggled['bool'].connect(self.dockVocab.setVisible)
        self.actionQuit.triggered.connect(MainWindowReader.close)
        self.actionToggleAnki.toggled['bool'].connect(self.dockAnki.setVisible)
        self.actionToggleKanji.toggled['bool'].connect(self.dockKanji.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindowReader)

    def retranslateUi(self, MainWindowReader):
        _translate = QtCore.QCoreApplication.translate
        MainWindowReader.setWindowTitle(_translate("MainWindowReader", "YomiObaasan"))
        self.textContent.setPlainText(_translate("MainWindowReader", "Paste text here or open a .txt file you want to read!"))
        self.menuFile.setTitle(_translate("MainWindowReader", "&File"))
        self.menuOpenRecent.setTitle(_translate("MainWindowReader", "Open &recent"))
        self.menuImport.setTitle(_translate("MainWindowReader", "&Import"))
        self.menuEdit.setTitle(_translate("MainWindowReader", "&Edit"))
        self.menuHelp.setTitle(_translate("MainWindowReader", "&Help"))
        self.menuView.setTitle(_translate("MainWindowReader", "&View"))
        self.menuTextSize.setTitle(_translate("MainWindowReader", "&Zoom"))
        self.toolBar.setWindowTitle(_translate("MainWindowReader", "toolBar"))
        self.dockVocab.setWindowTitle(_translate("MainWindowReader", "Vocabulary"))
        self.label.setText(_translate("MainWindowReader", "Expression"))
        self.dockAnki.setWindowTitle(_translate("MainWindowReader", "Extracts"))
        self.label_3.setText(_translate("MainWindowReader", "Active tag(s)"))
        self.dockKanji.setWindowTitle(_translate("MainWindowReader", "Kanji"))
        self.label_2.setText(_translate("MainWindowReader", "Character"))
        self.actionOpen.setText(_translate("MainWindowReader", "&Open..."))
        self.actionOpen.setToolTip(_translate("MainWindowReader", "Open file"))
        self.actionOpen.setShortcut(_translate("MainWindowReader", "Ctrl+O"))
        self.actionQuit.setText(_translate("MainWindowReader", "&Quit"))
        self.actionQuit.setToolTip(_translate("MainWindowReader", "Quit Yomichan"))
        self.actionQuit.setShortcut(_translate("MainWindowReader", "Esc"))
        self.actionPreferences.setText(_translate("MainWindowReader", "&Preferences..."))
        self.actionPreferences.setToolTip(_translate("MainWindowReader", "Edit preferences"))
        self.actionAbout.setText(_translate("MainWindowReader", "&About..."))
        self.actionAbout.setToolTip(_translate("MainWindowReader", "About Yomichan"))
        self.actionAbout.setShortcut(_translate("MainWindowReader", "F1"))
        self.actionZoomIn.setText(_translate("MainWindowReader", "Zoom &in"))
        self.actionZoomIn.setShortcut(_translate("MainWindowReader", "Ctrl++"))
        self.actionZoomOut.setText(_translate("MainWindowReader", "Zoom &out"))
        self.actionZoomOut.setShortcut(_translate("MainWindowReader", "Ctrl+-"))
        self.actionZoomReset.setText(_translate("MainWindowReader", "&Reset"))
        self.actionZoomReset.setToolTip(_translate("MainWindowReader", "Reset zoom"))
        self.actionZoomReset.setShortcut(_translate("MainWindowReader", "Ctrl+0"))
        self.actionFind.setText(_translate("MainWindowReader", "&Find..."))
        self.actionFind.setToolTip(_translate("MainWindowReader", "Find text"))
        self.actionFind.setShortcut(_translate("MainWindowReader", "Ctrl+F"))
        self.actionFindNext.setText(_translate("MainWindowReader", "Find &next"))
        self.actionFindNext.setToolTip(_translate("MainWindowReader", "Find text again"))
        self.actionFindNext.setShortcut(_translate("MainWindowReader", "F3"))
        self.actionToggleWrap.setText(_translate("MainWindowReader", "&Word wrap"))
        self.actionToggleWrap.setToolTip(_translate("MainWindowReader", "Toggle word wrap"))
        self.actionToggleVocab.setText(_translate("MainWindowReader", "&Vocabulary"))
        self.actionToggleVocab.setToolTip(_translate("MainWindowReader", "Toggle definitions"))
        self.actionHomepage.setText(_translate("MainWindowReader", "&Homepage..."))
        self.actionHomepage.setToolTip(_translate("MainWindowReader", "Yomichan homepage"))
        self.actionToggleAnki.setText(_translate("MainWindowReader", "&Extracts"))
        self.actionFeedback.setText(_translate("MainWindowReader", "&Feedback..."))
        self.actionToggleKanji.setText(_translate("MainWindowReader", "&Kanji"))
        self.actionKindleDeck.setText(_translate("MainWindowReader", "&Kindle deck..."))
        self.actionWordList.setText(_translate("MainWindowReader", "&Word list..."))


from . import resources_rc
