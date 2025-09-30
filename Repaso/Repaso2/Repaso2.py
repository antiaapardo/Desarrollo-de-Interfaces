# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Repaso2.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineNombre = QLineEdit(self.centralwidget)
        self.lineNombre.setObjectName(u"lineNombre")
        self.lineNombre.setGeometry(QRect(310, 90, 113, 21))
        self.lineNombre.setStyleSheet(u"")
        self.comboBoxRol = QComboBox(self.centralwidget)
        self.comboBoxRol.addItem("")
        self.comboBoxRol.addItem("")
        self.comboBoxRol.addItem("")
        self.comboBoxRol.setObjectName(u"comboBoxRol")
        self.comboBoxRol.setGeometry(QRect(320, 130, 80, 24))
        self.checkBoxNormas = QCheckBox(self.centralwidget)
        self.checkBoxNormas.setObjectName(u"checkBoxNormas")
        self.checkBoxNormas.setGeometry(QRect(310, 170, 131, 20))
        self.BtnEnviar = QPushButton(self.centralwidget)
        self.BtnEnviar.setObjectName(u"BtnEnviar")
        self.BtnEnviar.setGeometry(QRect(330, 210, 79, 24))
        self.lblNombre = QLabel(self.centralwidget)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(240, 90, 49, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 130, 49, 16))
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
        self.lineNombre.setText("")
        self.comboBoxRol.setItemText(0, QCoreApplication.translate("MainWindow", u"Alumno", None))
        self.comboBoxRol.setItemText(1, QCoreApplication.translate("MainWindow", u"Profesor", None))
        self.comboBoxRol.setItemText(2, QCoreApplication.translate("MainWindow", u"Invitado", None))

        self.checkBoxNormas.setText(QCoreApplication.translate("MainWindow", u"Acepto las normas", None))
        self.BtnEnviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.lblNombre.setText(QCoreApplication.translate("MainWindow", u"Nombre :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rol : ", None))
    # retranslateUi

