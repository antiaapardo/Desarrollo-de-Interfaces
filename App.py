import sys


from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from MiniApp import Ui_MainWindow

class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        print("La aplicación se ha iniciado correctamente.")
        self.btn1.clicked.connect(self.on_cambiar)

    def on_cambiar(self):
            self.lblTexto.setText("Muy bien.")
            print("Se ha presionado el boton")

if __name__ == "__main__":

            app = QApplication(sys.argv)
            window = Ventana()
            window.show()
            sys.exit(app.exec())