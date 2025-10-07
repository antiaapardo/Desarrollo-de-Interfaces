# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_ejercicio4.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(280, 80, 160, 116))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Btn1 = QPushButton(self.verticalLayoutWidget)
        self.Btn1.setObjectName(u"Btn1")

        self.verticalLayout.addWidget(self.Btn1)

        self.Btn2 = QPushButton(self.verticalLayoutWidget)
        self.Btn2.setObjectName(u"Btn2")

        self.verticalLayout.addWidget(self.Btn2)

        self.Btn3 = QPushButton(self.verticalLayoutWidget)
        self.Btn3.setObjectName(u"Btn3")

        self.verticalLayout.addWidget(self.Btn3)

        self.Btn4 = QPushButton(self.verticalLayoutWidget)
        self.Btn4.setObjectName(u"Btn4")

        self.verticalLayout.addWidget(self.Btn4)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Btn2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Btn3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Btn4.setText(QCoreApplication.translate("MainWindow", u"4", None))
    # retranslateUi

