import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from BuscadorProducto import Ui_MainWindow  
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    
        self.setWindowTitle("Mini 1 – Buscador de productos")

       
        self.labels = [
            self.ui.label,
            self.ui.label_2,
            self.ui.label_3,
            self.ui.label_4,
            self.ui.label_5,
        ]

        # Conectamos el evento de texto cambiado
        self.ui.lineEdit.textChanged.connect(self.filter_products)

    def filter_products(self, text):
        """Filtra los productos según el texto introducido (sin distinguir mayúsculas/minúsculas)."""
        text = text.strip().lower()

        for label in self.labels:
            label_text = label.text().lower()
            label.setVisible(text in label_text)  # Si coincide, se muestra; si no, se oculta


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
