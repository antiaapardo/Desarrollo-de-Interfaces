# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GestorDeTareas.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(300, 150, 160, 146))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.BtnNuevoProyecto = QPushButton(self.verticalLayoutWidget)
        self.BtnNuevoProyecto.setObjectName(u"BtnNuevoProyecto")

        self.verticalLayout.addWidget(self.BtnNuevoProyecto)

        self.BtnConfirmar = QPushButton(self.verticalLayoutWidget)
        self.BtnConfirmar.setObjectName(u"BtnConfirmar")

        self.verticalLayout.addWidget(self.BtnConfirmar)

        self.BtnMensajes = QPushButton(self.verticalLayoutWidget)
        self.BtnMensajes.setObjectName(u"BtnMensajes")

        self.verticalLayout.addWidget(self.BtnMensajes)

        self.BtnPreferencias = QPushButton(self.verticalLayoutWidget)
        self.BtnPreferencias.setObjectName(u"BtnPreferencias")

        self.verticalLayout.addWidget(self.BtnPreferencias)

        self.BtnExportar = QPushButton(self.verticalLayoutWidget)
        self.BtnExportar.setObjectName(u"BtnExportar")

        self.verticalLayout.addWidget(self.BtnExportar)

        self.lblPreferencias = QLabel(self.centralwidget)
        self.lblPreferencias.setObjectName(u"lblPreferencias")
        self.lblPreferencias.setGeometry(QRect(70, 30, 131, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuHerramientas = QMenu(self.menubar)
        self.menuHerramientas.setObjectName(u"menuHerramientas")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BtnNuevoProyecto.setText(QCoreApplication.translate("MainWindow", u"Nuevo proyecto...", None))
        self.BtnConfirmar.setText(QCoreApplication.translate("MainWindow", u"Confirmar accion...", None))
        self.BtnMensajes.setText(QCoreApplication.translate("MainWindow", u"Centro de mensajes...", None))
        self.BtnPreferencias.setText(QCoreApplication.translate("MainWindow", u"Preferencias de usuario", None))
        self.BtnExportar.setText(QCoreApplication.translate("MainWindow", u"Exportar informe", None))
        self.lblPreferencias.setText(QCoreApplication.translate("MainWindow", u"Preferencias sin asignar ", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo ", None))
        self.menuHerramientas.setTitle(QCoreApplication.translate("MainWindow", u"Herramientas", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

