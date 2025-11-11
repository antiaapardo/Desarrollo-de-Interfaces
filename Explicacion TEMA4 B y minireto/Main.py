import sys
from PySide6.QtWidgets import QApplication
from cronometro_ui import CronometroWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = CronometroWidget()
    ventana.setWindowTitle("Cronómetro Qt")
    ventana.resize(200, 150)
    ventana.show()

    sys.exit(app.exec())
