import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class Producto(QWidget):
    def __init__(self, nombre: str, precio: str, parent=None):
        super().__init__(parent)

        # Etiquetas privadas
        self._label_nombre = QLabel(nombre)
        self._label_precio = QLabel(precio)

        # Layout horizontal: nombre a la izquierda, precio a la derecha
        layout = QHBoxLayout()
        layout.addWidget(self._label_nombre)
        layout.addStretch()  # separador
        layout.addWidget(self._label_precio)
        self.setLayout(layout)

    # Propiedad nombre
    @property
    def nombre(self):
        return self._label_nombre.text()

    @nombre.setter
    def nombre(self, valor):
        self._label_nombre.setText(valor)

    # Propiedad precio
    @property
    def precio(self):
        return self._label_precio.text()

    @precio.setter
    def precio(self, valor):
        self._label_precio.setText(valor)
    
