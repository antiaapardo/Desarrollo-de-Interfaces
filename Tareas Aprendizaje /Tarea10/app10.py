from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QTabWidget, QMessageBox
)
from componentes.basicos.boton_saludador import BotonSaludador
from componentes.empresa.panel_empleados import PanelEmpleados
from PySide6.QtGui import QIcon


import recursos_rc


class AppPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini-tareas en Pestañas")

        # (Opcional) Icono propio
        self.setWindowIcon(QIcon(":/icono.png"))

        # Widget principal con layout
        contenedor = QWidget()
        layout = QVBoxLayout(contenedor)

        # Pestañas
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # Componente BotonSaludador
        self.boton_tab = BotonSaludador()
        self.tabs.addTab(self.boton_tab, "Botón Saludador")

        # Componente PanelEmpleados
        self.empleados_tab = PanelEmpleados()
        self.tabs.addTab(self.empleados_tab, "Panel Empleados")

        # Conectar la señal del botón a un QMessageBox
        self.boton_tab.saludado.connect(self.mostrar_mensaje)

        self.setCentralWidget(contenedor)

    @Slot(str)
    def mostrar_mensaje(self, mensaje):
        QMessageBox.information(self, "Evento", mensaje)


if __name__ == "__main__":
    app = QApplication([])

    ventana = AppPrincipal()
    ventana.show()

    app.exec()
