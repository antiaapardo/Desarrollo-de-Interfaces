# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ejercicio7.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QSizePolicy,
    QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(290, 90, 160, 81))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit)

        self.spinBox = QSpinBox(self.formLayoutWidget)
        self.spinBox.setObjectName(u"spinBox")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox)

        self.doubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox)

        self.label_Texto = QLabel(self.formLayoutWidget)
        self.label_Texto.setObjectName(u"label_Texto")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_Texto)

        self.label_Entero = QLabel(self.formLayoutWidget)
        self.label_Entero.setObjectName(u"label_Entero")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_Entero)

        self.label_Decimal = QLabel(self.formLayoutWidget)
        self.label_Decimal.setObjectName(u"label_Decimal")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_Decimal)

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
        self.label_Texto.setText(QCoreApplication.translate("MainWindow", u"TEXTO", None))
        self.label_Entero.setText(QCoreApplication.translate("MainWindow", u"ENTERO", None))
        self.label_Decimal.setText(QCoreApplication.translate("MainWindow", u"DECIMAL", None))
    # retranslateUi

