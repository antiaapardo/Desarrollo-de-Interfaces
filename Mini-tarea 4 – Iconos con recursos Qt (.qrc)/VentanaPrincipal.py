import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
from ProductoConIcono import ProductoConIcono  # asegúrate de que el archivo se llama exactamente "ProductoConIcono.py"
import resources_rc  # importa el archivo generado con pyside6-rcc


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mini tarea 4 – Productos con icono")

        # Layout horizontal
        layout = QHBoxLayout()
        layout.setSpacing(20)

        # Crear los tres productos (usa las rutas de recurso con ":/icons/")
        producto1 = ProductoConIcono("icons/laptop.png", "Portátil ZenAir", 799)
        producto2 = ProductoConIcono("icons/mouse.png", "Ratón Ergonomic", 25)
        producto3 = ProductoConIcono("icons/keyboard.png", "Teclado Gamer RGB", 99)

        # Añadirlos al layout
        layout.addWidget(producto1)
        layout.addWidget(producto2)
        layout.addWidget(producto3)

        self.setLayout(layout)
        self.setFixedSize(550, 220)


# -----------------------------
# Bloque principal (main)
# -----------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
