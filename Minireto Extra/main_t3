import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PySide6.QtCore import Qt
from t3_batterywidget import BatteryWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Battery Widget Demo")

        # Instancia del widget personalizado
        self.battery = BatteryWidget()

        # Etiqueta para mostrar el valor numérico
        self.label = QLabel("Nivel: 50%")
        self.label.setAlignment(Qt.AlignCenter)

        # Slider para ajustar el nivel
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.update_level)

        # Layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.battery)
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        self.setLayout(layout)

    def update_level(self, value):
        """Actualiza el nivel de la batería y el texto"""
        self.battery.setLevel(value)
        self.label.setText(f"Nivel: {value}%")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(250, 200)
    window.show()
    sys.exit(app.exec())
