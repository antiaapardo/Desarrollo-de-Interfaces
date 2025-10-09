import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Ejercicio9 import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar acciones
        self.actionAbrir.triggered.connect(self.abrir)
        self.actionGuardar.triggered.connect(self.guardar)
        self.actionSalir.triggered.connect(self.salir)

    # Funciones de las acciones
    def abrir(self):
        self.statusbar.showMessage("Abrir archivo")
        print("Abrir archivo")

    def guardar(self):
        self.statusbar.showMessage("Guardar archivo")
        print("Guardar archivo")

    def salir(self):
        self.statusbar.showMessage("Salir de la aplicación")
        print("Salir de la aplicación")
        QApplication.quit()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
