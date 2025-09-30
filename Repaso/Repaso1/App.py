import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from Repaso1 import Ui_MainWindow #Archivo que generaste en el que generó pyside6-uic

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #Cargar lo que hiciste en la paleta

        self.lblText.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout(self.centralwidget)
        layout.addWidget(self.lblText, alignment=Qt.AlignCenter)

        print("Arrancado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
