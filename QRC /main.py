import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# IMPORTANTE: importa el módulo generado por pyside6-rcc
import recursos_rc  # <-- esto registra :/icons/... automáticamente

app = QApplication(sys.argv)

loader = QUiLoader()
f = QFile("interfaz.ui")
f.open(QFile.ReadOnly)
w = loader.load(f)
f.close()

w.show()
app.exec()
