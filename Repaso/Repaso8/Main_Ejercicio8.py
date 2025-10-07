import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Ejercicio8 import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar botones
        self.btn1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))  
        self.Btn2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))  
        self.Btn3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0)) 

        # Ajustar tamaño del stackedWidget para que se vea
        self.stackedWidget.setGeometry(50, 50, 300, 200)

        # Ajustar tamaño de etiquetas
        self.label.setGeometry(10, 10, 100, 30)
        self.label_2.setGeometry(10, 10, 100, 30)
        self.label_3.setGeometry(10, 10, 100, 30)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
