# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(930, 713)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.selectedTreeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Name");
        self.selectedTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.selectedTreeWidget.setObjectName(u"selectedTreeWidget")
        self.selectedTreeWidget.setGeometry(QRect(460, 190, 451, 461))
        font = QFont()
        font.setPointSize(12)
        self.selectedTreeWidget.setFont(font)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 120, 891, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.pathLineEdit = QLineEdit(self.layoutWidget)
        self.pathLineEdit.setObjectName(u"pathLineEdit")

        self.horizontalLayout.addWidget(self.pathLineEdit)

        self.goButton = QPushButton(self.layoutWidget)
        self.goButton.setObjectName(u"goButton")

        self.horizontalLayout.addWidget(self.goButton)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(460, 160, 177, 22))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.expandCollapseButton = QPushButton(self.centralwidget)
        self.expandCollapseButton.setObjectName(u"expandCollapseButton")
        self.expandCollapseButton.setGeometry(QRect(760, 160, 151, 32))
        self.browserWidget = QWidget(self.centralwidget)
        self.browserWidget.setObjectName(u"browserWidget")
        self.browserWidget.setGeometry(QRect(20, 160, 431, 501))
        self.label_5 = QLabel(self.browserWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 100, 22))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.browserWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(310, 0, 111, 32))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.backButton = QPushButton(self.widget)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout_2.addWidget(self.backButton)

        self.forwardButton = QPushButton(self.widget)
        self.forwardButton.setObjectName(u"forwardButton")

        self.horizontalLayout_2.addWidget(self.forwardButton)

        self.systemTreeWidget = QTreeWidget(self.browserWidget)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"Name");
        self.systemTreeWidget.setHeaderItem(__qtreewidgetitem1)
        self.systemTreeWidget.setObjectName(u"systemTreeWidget")
        self.systemTreeWidget.setGeometry(QRect(0, 30, 421, 411))
        self.systemTreeWidget.setFont(font)
        self.widget1 = QWidget(self.browserWidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 470, 431, 32))
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.selectAllButton = QPushButton(self.widget1)
        self.selectAllButton.setObjectName(u"selectAllButton")

        self.horizontalLayout_3.addWidget(self.selectAllButton)

        self.deselectButton = QPushButton(self.widget1)
        self.deselectButton.setObjectName(u"deselectButton")

        self.horizontalLayout_3.addWidget(self.deselectButton)

        self.multiCheckBox = QCheckBox(self.browserWidget)
        self.multiCheckBox.setObjectName(u"multiCheckBox")
        self.multiCheckBox.setGeometry(QRect(160, 440, 101, 31))
        self.multiCheckBox.setLayoutDirection(Qt.LeftToRight)
        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 30, 441, 77))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget2)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.widget2)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(True)
        font3.setWeight(50)
        self.label_2.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_7 = QLabel(self.widget2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 930, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtreewidgetitem = self.selectedTreeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Collapsed/Collapsible", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"File Path", None))
        self.goButton.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Selected / Expanded", None))
        self.expandCollapseButton.setText(QCoreApplication.translate("MainWindow", u"Expand Collapsed", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"File System", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.forwardButton.setText(QCoreApplication.translate("MainWindow", u">", None))
        ___qtreewidgetitem1 = self.systemTreeWidget.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Collapsed", None));
        self.selectAllButton.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.deselectButton.setText(QCoreApplication.translate("MainWindow", u"Deselect All", None))
        self.multiCheckBox.setText(QCoreApplication.translate("MainWindow", u"Multi-Select", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ingenuity Programming Challenge", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sequence File Selector", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Monika Hedman - March 2020", None))
    # retranslateUi

