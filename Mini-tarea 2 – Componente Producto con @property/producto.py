import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class Producto(QWidget):
    def __init__(self, nombre: str, precio: str, parent=None):
        super().__init__(parent)

       
        self._label_nombre = QLabel(nombre)
        self._label_precio = QLabel(precio)

    
        layout = QHBoxLayout()
        layout.addWidget(self._label_nombre)
        layout.addStretch()  # separador
        layout.addWidget(self._label_precio)
        self.setLayout(layout)

 
    @property
    def nombre(self):
        return self._label_nombre.text()

    @nombre.setter
    def nombre(self, valor):
        self._label_nombre.setText(valor)


    @property
    def precio(self):
        return self._label_precio.text()

    @precio.setter
    def precio(self, valor):
        self._label_precio.setText(valor)
    
class DemoProducto(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini 2 – Componente Producto")

      
        self.producto = Producto("Ratón Óptico Pro", "19,99 €")

        self.btn_actualizar = QPushButton("Actualizar precio")
        self.btn_actualizar.clicked.connect(self.actualizar_precio)

      
        layout = QVBoxLayout()
        layout.addWidget(self.producto)
        layout.addWidget(self.btn_actualizar)
        self.setLayout(layout)

    def actualizar_precio(self):
        # Cambiamos el precio usando el setter
        self.producto.precio = "14,99 €"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = DemoProducto()
    ventana.resize(300, 100)
    ventana.show()
    sys.exit(app.exec())
