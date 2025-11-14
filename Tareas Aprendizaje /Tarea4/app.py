#Tarea4
from PySide6.QtWidgets import QApplication, QMainWindow
from componentes.boton_saludador import BotonSaludador  

app = QApplication([])
win = QMainWindow()
win.setWindowTitle("Componente Botón Saludador")
win.setCentralWidget(BotonSaludador())
win.show()
app.exec()
