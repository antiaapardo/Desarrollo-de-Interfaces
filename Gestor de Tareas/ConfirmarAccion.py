# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfirmarAccion.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
    QLabel, QSizePolicy, QWidget)

class Ui_ConfirmarAccion(object):
    def setupUi(self, ConfirmarAccion):
        if not ConfirmarAccion.objectName():
            ConfirmarAccion.setObjectName(u"ConfirmarAccion")
        ConfirmarAccion.resize(400, 300)
        self.buttonBox = QDialogButtonBox(ConfirmarAccion)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(120, 130, 164, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.lblTexto = QLabel(ConfirmarAccion)
        self.lblTexto.setObjectName(u"lblTexto")
        self.lblTexto.setGeometry(QRect(60, 90, 271, 20))

        self.retranslateUi(ConfirmarAccion)

        QMetaObject.connectSlotsByName(ConfirmarAccion)
    # setupUi

    def retranslateUi(self, ConfirmarAccion):
        ConfirmarAccion.setWindowTitle(QCoreApplication.translate("ConfirmarAccion", u"Dialog", None))
        self.lblTexto.setText(QCoreApplication.translate("ConfirmarAccion", u"\u00bfSeguro que desea eliminar los datos temporales ?", None))
    # retranslateUi

