# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ejercicio12.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 607)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.actionAbrir.setIcon(icon)
        self.actionAbrir.setMenuRole(QAction.MenuRole.NoRole)
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.actionGuardar.setIcon(icon1)
        self.actionGuardar.setMenuRole(QAction.MenuRole.NoRole)
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.actionSalir.setIcon(icon2)
        self.actionSalir.setMenuRole(QAction.MenuRole.NoRole)
        self.actionMostrar_playlist = QAction(MainWindow)
        self.actionMostrar_playlist.setObjectName(u"actionMostrar_playlist")
        self.actionMostrar_playlist.setMenuRole(QAction.MenuRole.NoRole)
        self.actionOcultar_playlist = QAction(MainWindow)
        self.actionOcultar_playlist.setObjectName(u"actionOcultar_playlist")
        self.actionOcultar_playlist.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 796, 33))
        self.menuARCHIVO = QMenu(self.menubar)
        self.menuARCHIVO.setObjectName(u"menuARCHIVO")
        self.menuVER = QMenu(self.menubar)
        self.menuVER.setObjectName(u"menuVER")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.dockPlaylist = QDockWidget(MainWindow)
        self.dockPlaylist.setObjectName(u"dockPlaylist")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.listWidget = QListWidget(self.dockWidgetContents)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(310, 0, 256, 61))
        self.dockPlaylist.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.dockPlaylist)

        self.menubar.addAction(self.menuARCHIVO.menuAction())
        self.menubar.addAction(self.menuVER.menuAction())
        self.menuARCHIVO.addAction(self.actionAbrir)
        self.menuARCHIVO.addAction(self.actionGuardar)
        self.menuARCHIVO.addAction(self.actionSalir)
        self.menuVER.addAction(self.actionMostrar_playlist)
        self.menuVER.addAction(self.actionOcultar_playlist)
        self.toolBar.addAction(self.actionAbrir)
        self.toolBar.addAction(self.actionGuardar)
        self.toolBar.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir...", None))
#if QT_CONFIG(statustip)
        self.actionAbrir.setStatusTip(QCoreApplication.translate("MainWindow", u"Abrir un archivo ", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(statustip)
        self.actionGuardar.setStatusTip(QCoreApplication.translate("MainWindow", u"Guardar el archivo", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(statustip)
        self.actionSalir.setStatusTip(QCoreApplication.translate("MainWindow", u"Cerrar la aplicacion", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionMostrar_playlist.setText(QCoreApplication.translate("MainWindow", u"Mostrar playlist", None))
        self.actionOcultar_playlist.setText(QCoreApplication.translate("MainWindow", u"Ocultar playlist", None))
        self.menuARCHIVO.setTitle(QCoreApplication.translate("MainWindow", u"ARCHIVO", None))
        self.menuVER.setTitle(QCoreApplication.translate("MainWindow", u"VER", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.dockPlaylist.setWindowTitle(QCoreApplication.translate("MainWindow", u"Playlist", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"cancion_1.wav", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"cancion_2.wav", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"cancion_3.wav", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

