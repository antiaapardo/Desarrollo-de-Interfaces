# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TechMarketDashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QScrollArea, QSizePolicy, QStatusBar, QToolBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionA_adir_Producto = QAction(MainWindow)
        self.actionA_adir_Producto.setObjectName(u"actionA_adir_Producto")
        self.actionEliminar_Producto = QAction(MainWindow)
        self.actionEliminar_Producto.setObjectName(u"actionEliminar_Producto")
        self.actionmostrar_Estadisticas = QAction(MainWindow)
        self.actionmostrar_Estadisticas.setObjectName(u"actionmostrar_Estadisticas")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 20, 300, 25))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 60, 760, 500))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 760, 500))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionA_adir_Producto)
        self.toolBar.addAction(self.actionEliminar_Producto)
        self.toolBar.addAction(self.actionmostrar_Estadisticas)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TechMarket Dashboard", None))
        self.actionA_adir_Producto.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Producto", None))
        self.actionEliminar_Producto.setText(QCoreApplication.translate("MainWindow", u"Eliminar Producto", None))
        self.actionmostrar_Estadisticas.setText(QCoreApplication.translate("MainWindow", u"Mostrar Estad\u00edsticas", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar productos...", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"Barra de herramientas", None))
    # retranslateUi

