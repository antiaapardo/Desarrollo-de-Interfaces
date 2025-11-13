import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt  
from TechMarketDashboard import Ui_MainWindow  
from ProductoConIcono import ProductoConIcono
import resources_rc  


class TechMarketDashboardMain(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar la UI generada
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Crear layout vertical dentro del scroll area
        self.products_layout = QVBoxLayout()
        self.products_layout.setAlignment(Qt.AlignTop)
        self.ui.scrollAreaWidgetContents.setLayout(self.products_layout)

        # Lista de productos
        self.productos = []

        # Agregar productos de ejemplo
        self.agregar_productos_ejemplo()

        # Conectar buscador
        self.ui.lineEdit.textChanged.connect(self.filtrar_productos)

        # Conectar botones de la barra de herramientas
        self.ui.actionmostrar_Estadisticas.triggered.connect(self.mostrar_estadisticas)
        self.ui.actionA_adir_Producto.triggered.connect(self.agregar_producto)
        self.ui.actionEliminar_Producto.triggered.connect(self.eliminar_producto)

        # Barra de estado
        self.ui.statusbar.showMessage("Listo")

    def agregar_productos_ejemplo(self):
        ejemplos = [
            (":/icons/laptop.png", "Portátil ZenAir", 799),
            (":/icons/mouse.png", "Ratón Ergonomic", 25),
            (":/icons/keyboard.png", "Teclado Gamer RGB", 99)
        ]
        for icono, nombre, precio in ejemplos:
            self.agregar_producto(icono, nombre, precio)

    def agregar_producto(self, icono=":/icons/laptop.png", nombre="Nuevo producto", precio=0):
        producto = ProductoConIcono(icono, nombre, precio)
        self.productos.append(producto)
        self.products_layout.addWidget(producto)

    def eliminar_producto(self):
        if self.productos:
            producto = self.productos.pop()
            self.products_layout.removeWidget(producto)
            producto.deleteLater()

    def filtrar_productos(self, texto):
        texto = texto.lower()
        for producto in self.productos:
            nombre = producto.label_nombre.text().lower()
            producto.setVisible(texto in nombre)

    def mostrar_estadisticas(self):
        total = len(self.productos)
        visibles = sum(1 for p in self.productos if p.isVisible())
        QMessageBox.information(
            self,
            "Estadísticas",
            f"Total de productos: {total}\nProductos visibles: {visibles}"
        )



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TechMarketDashboardMain()
    ventana.show()
    sys.exit(app.exec())
