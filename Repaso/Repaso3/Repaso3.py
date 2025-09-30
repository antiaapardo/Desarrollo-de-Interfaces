# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Repaso3.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(280, 260, 241, 23))
        self.progressBar.setValue(0)
        self.BtnIniciar = QPushButton(self.centralwidget)
        self.BtnIniciar.setObjectName(u"BtnIniciar")
        self.BtnIniciar.setGeometry(QRect(340, 290, 79, 24))
        self.listTareas = QListWidget(self.centralwidget)
        QListWidgetItem(self.listTareas)
        QListWidgetItem(self.listTareas)
        QListWidgetItem(self.listTareas)
        self.listTareas.setObjectName(u"listTareas")
        self.listTareas.setGeometry(QRect(270, 60, 256, 192))
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
        self.BtnIniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))

        __sortingEnabled = self.listTareas.isSortingEnabled()
        self.listTareas.setSortingEnabled(False)
        ___qlistwidgetitem = self.listTareas.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"TAREA1", None));
        ___qlistwidgetitem1 = self.listTareas.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"TAREA2", None));
        ___qlistwidgetitem2 = self.listTareas.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"TAREA3", None));
        self.listTareas.setSortingEnabled(__sortingEnabled)

    # retranslateUi

