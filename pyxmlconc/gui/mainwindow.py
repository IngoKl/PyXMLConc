# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1137, 756)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.load_button = QPushButton(self.centralWidget)
        self.load_button.setObjectName(u"load_button")

        self.horizontalLayout_3.addWidget(self.load_button)

        self.save_button = QPushButton(self.centralWidget)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_3.addWidget(self.save_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.concordance_list = QListWidget(self.centralWidget)
        self.concordance_list.setObjectName(u"concordance_list")
        font = QFont()
        font.setFamily(u"Courier Std")
        font.setPointSize(12)
        self.concordance_list.setFont(font)
        self.concordance_list.setAlternatingRowColors(True)
        self.concordance_list.setTextElideMode(Qt.ElideMiddle)
        self.concordance_list.setSortingEnabled(True)

        self.verticalLayout_4.addWidget(self.concordance_list)

        self.results_label = QLabel(self.centralWidget)
        self.results_label.setObjectName(u"results_label")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.results_label.setFont(font1)

        self.verticalLayout_4.addWidget(self.results_label)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.tags_label = QLabel(self.centralWidget)
        self.tags_label.setObjectName(u"tags_label")

        self.verticalLayout_3.addWidget(self.tags_label)

        self.tag_list = QListWidget(self.centralWidget)
        self.tag_list.setObjectName(u"tag_list")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tag_list.sizePolicy().hasHeightForWidth())
        self.tag_list.setSizePolicy(sizePolicy)
        self.tag_list.setMaximumSize(QSize(200, 16777215))
        self.tag_list.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_3.addWidget(self.tag_list)

        self.tag_deselect_button = QPushButton(self.centralWidget)
        self.tag_deselect_button.setObjectName(u"tag_deselect_button")

        self.verticalLayout_3.addWidget(self.tag_deselect_button)

        self.attribute_label = QLabel(self.centralWidget)
        self.attribute_label.setObjectName(u"attribute_label")

        self.verticalLayout_3.addWidget(self.attribute_label)

        self.attribute_search = QLineEdit(self.centralWidget)
        self.attribute_search.setObjectName(u"attribute_search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.attribute_search.sizePolicy().hasHeightForWidth())
        self.attribute_search.setSizePolicy(sizePolicy1)
        self.attribute_search.setMinimumSize(QSize(200, 0))

        self.verticalLayout_3.addWidget(self.attribute_search)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.frequency_list = QListWidget(self.centralWidget)
        self.frequency_list.setObjectName(u"frequency_list")
        self.frequency_list.setMaximumSize(QSize(200, 16777215))
        self.frequency_list.setSortingEnabled(True)

        self.horizontalLayout_2.addWidget(self.frequency_list)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ignore_tags_box = QCheckBox(self.centralWidget)
        self.ignore_tags_box.setObjectName(u"ignore_tags_box")
        self.ignore_tags_box.setEnabled(True)
        self.ignore_tags_box.setChecked(False)

        self.horizontalLayout_4.addWidget(self.ignore_tags_box)

        self.strip_tags_box = QCheckBox(self.centralWidget)
        self.strip_tags_box.setObjectName(u"strip_tags_box")
        self.strip_tags_box.setChecked(True)

        self.horizontalLayout_4.addWidget(self.strip_tags_box)

        self.ignore_case_box = QCheckBox(self.centralWidget)
        self.ignore_case_box.setObjectName(u"ignore_case_box")

        self.horizontalLayout_4.addWidget(self.ignore_case_box)

        self.allow_overlap_box = QCheckBox(self.centralWidget)
        self.allow_overlap_box.setObjectName(u"allow_overlap_box")

        self.horizontalLayout_4.addWidget(self.allow_overlap_box)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_button = QPushButton(self.centralWidget)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout.addWidget(self.search_button)

        self.search_bar = QLineEdit(self.centralWidget)
        self.search_bar.setObjectName(u"search_bar")

        self.horizontalLayout.addWidget(self.search_bar)

        self.working_mode_box = QComboBox(self.centralWidget)
        self.working_mode_box.addItem("")
        self.working_mode_box.addItem("")
        self.working_mode_box.setObjectName(u"working_mode_box")
        self.working_mode_box.setCurrentText(u"Tokenizer")
        self.working_mode_box.setFrame(True)

        self.horizontalLayout.addWidget(self.working_mode_box)

        self.lrbound = QSpinBox(self.centralWidget)
        self.lrbound.setObjectName(u"lrbound")
        self.lrbound.setValue(4)

        self.horizontalLayout.addWidget(self.lrbound)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyXMLConc", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.results_label.setText(QCoreApplication.translate("MainWindow", u"0 Results", None))
        self.tags_label.setText(QCoreApplication.translate("MainWindow", u"Available Tags", None))
        self.tag_deselect_button.setText(QCoreApplication.translate("MainWindow", u"Deselect", None))
        self.attribute_label.setText(QCoreApplication.translate("MainWindow", u"Attribute Search (e.g. a1=\"1\";a2=\"2\")", None))
        self.ignore_tags_box.setText(QCoreApplication.translate("MainWindow", u"Ignore Tags Completely", None))
        self.strip_tags_box.setText(QCoreApplication.translate("MainWindow", u"Strip Tags", None))
        self.ignore_case_box.setText(QCoreApplication.translate("MainWindow", u"Ignore Case", None))
        self.allow_overlap_box.setText(QCoreApplication.translate("MainWindow", u"Allow Overlap", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.working_mode_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Tokenizer", None))
        self.working_mode_box.setItemText(1, QCoreApplication.translate("MainWindow", u"re.findall", None))

    # retranslateUi

