from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QMessageBox
)
from componentes.basicos.boton_saludador import BotonSaludador
from componentes.empresa.panel_empleados import PanelEmpleados

app = QApplication([])

win = QMainWindow()

# Contenedor principal
cont = QWidget()
lay = QVBoxLayout(cont)

# Componentes
a = BotonSaludador()
b = PanelEmpleados()

lay.addWidget(a)
lay.addWidget(b)

# Slot para mostrar mensaje cuando se emite la señal
@Slot(str)
def avisar(mensaje):
    QMessageBox.information(win, "Evento", mensaje)

# Conectar señal
a.saludado.connect(avisar)

win.setCentralWidget(cont)
win.show()
app.exec()
