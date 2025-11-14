#Tarea7
from PySide6.QtWidgets import QApplication, QMainWindow
from componentes.basicos.etiqueta_saludo import EtiquetaSaludo
from componentes.basicos.boton_saludador import BotonSaludador
from componentes.empresa.panel_empleados import PanelEmpleados

app = QApplication([])

win = QMainWindow()
win.setWindowTitle("Componentes con subpaquetes")

# Cambia el widget central según lo que quieras probar:
# win.setCentralWidget(EtiquetaSaludo("Hola desde EtiquetaSaludo"))
# win.setCentralWidget(BotonSaludador())
win.setCentralWidget(PanelEmpleados())

win.show()
app.exec()
