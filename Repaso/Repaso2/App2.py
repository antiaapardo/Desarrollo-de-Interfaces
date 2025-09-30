import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from Repaso2 import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar botón
        self.BtnEnviar.clicked.connect(self.enviar)

    def enviar(self):
        nombre = self.lineNombre.text()
        rol = self.comboBoxRol.currentText() # Si es QComboBox
        normas = self.checkBoxNormas.isChecked()  # Suponiendo que se llama checkBox

        if not nombre or not normas:
            print("Faltan datos.")
        else:
            print(f"Nombre: {nombre} | Rol: {rol} | Acepta: Sí")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
