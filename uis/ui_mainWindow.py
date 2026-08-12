# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowEkxtOS.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

from PySide6_AceEditor.code_frame import AceCodeWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_open = QPushButton(self.centralwidget)
        self.pushButton_open.setObjectName(u"pushButton_open")

        self.horizontalLayout.addWidget(self.pushButton_open)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout.addWidget(self.pushButton_save)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_from = AceCodeWidget(self.centralwidget)
        self.widget_from.setObjectName(u"widget_from")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_from.sizePolicy().hasHeightForWidth())
        self.widget_from.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.widget_from)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_trans = QPushButton(self.centralwidget)
        self.pushButton_trans.setObjectName(u"pushButton_trans")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_trans.sizePolicy().hasHeightForWidth())
        self.pushButton_trans.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.pushButton_trans)

        self.pushButton_copy = QPushButton(self.centralwidget)
        self.pushButton_copy.setObjectName(u"pushButton_copy")

        self.verticalLayout_2.addWidget(self.pushButton_copy)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.widget_to = AceCodeWidget(self.centralwidget)
        self.widget_to.setObjectName(u"widget_to")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_to.sizePolicy().hasHeightForWidth())
        self.widget_to.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.widget_to)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Qt2PECMD", None))
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00UI\u6587\u4ef6", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58PECMD\u6587\u4ef6", None))
        self.pushButton_trans.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362", None))
        self.pushButton_copy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u7ed3\u679c", None))
    # retranslateUi

