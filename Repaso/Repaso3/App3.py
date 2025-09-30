import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication
from Repaso3 import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BtnIniciar.clicked.connect(self.empezar)
        # Crear QTimer
        self.timer = QTimer()
        self.timer.setInterval(50)  # 50 ms por tick
        self.timer.timeout.connect(self.actualizar_barra)

        self.listTareas.itemDoubleClicked.connect(self.mostrar_tarea)

    def empezar(self):
        self.valor = 0
        self.progressBar.setValue(self.valor)
        self.timer.start()
    def actualizar_barra(self):
        if self.valor >= 100:
            self.timer.stop()
        else:
            self.valor += 1
            self.progressBar.setValue(self.valor)
    def mostrar_tarea(self, item):
        texto = item.text()
        print(f"Has hecho doble click en {texto}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
