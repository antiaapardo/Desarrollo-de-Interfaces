from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt


class ProductoConIcono(QWidget):
    def __init__(self, icono_ruta: str, nombre: str, precio: float, parent=None):
        super().__init__(parent)

        # Imagen del producto
        self.label_imagen = QLabel()
        pixmap = QPixmap(icono_ruta)
        self.label_imagen.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.label_imagen.setAlignment(Qt.AlignCenter)

        # Nombre del producto
        self.label_nombre = QLabel(nombre)
        self.label_nombre.setAlignment(Qt.AlignCenter)
        self.label_nombre.setFont(QFont("Arial", 11, QFont.Bold))

        # Precio del producto
        self.label_precio = QLabel(f"{precio:.2f} €")
        self.label_precio.setAlignment(Qt.AlignCenter)
        self.label_precio.setFont(QFont("Arial", 10))
        self.label_precio.setStyleSheet("color: green;")

        # Layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.label_imagen)
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.label_precio)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)
        self.setFixedSize(150, 180)
        self.setStyleSheet("""
            QWidget {
                border: 1px solid #ccc;
                border-radius: 8px;
                background-color: #fafafa;
            }
            QLabel {
                padding: 3px;
            }
        """)
