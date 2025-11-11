import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from producto import Producto 
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
