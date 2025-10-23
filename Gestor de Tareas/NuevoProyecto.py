# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NuevoProyecto.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_NuevoProyecto(object):
    def setupUi(self, NuevoProyecto):
        if not NuevoProyecto.objectName():
            NuevoProyecto.setObjectName(u"NuevoProyecto")
        NuevoProyecto.resize(801, 300)
        self.lblNombre = QLabel(NuevoProyecto)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(30, 40, 241, 16))
        self.lineNombre = QLineEdit(NuevoProyecto)
        self.lineNombre.setObjectName(u"lineNombre")
        self.lineNombre.setGeometry(QRect(300, 40, 113, 21))
        self.buttonBox = QDialogButtonBox(NuevoProyecto)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(160, 80, 164, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.retranslateUi(NuevoProyecto)

        QMetaObject.connectSlotsByName(NuevoProyecto)
    # setupUi

    def retranslateUi(self, NuevoProyecto):
        NuevoProyecto.setWindowTitle(QCoreApplication.translate("NuevoProyecto", u"Dialog", None))
        self.lblNombre.setText(QCoreApplication.translate("NuevoProyecto", u"\u201cIntroduce el nombre del nuevo proyecto", None))
    # retranslateUi

