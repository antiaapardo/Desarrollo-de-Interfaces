from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel


class BotonSaludador(QWidget):
    # Señal que emite un string cuando se hace clic
    saludado = Signal(str)

    def __init__(self):
        super().__init__()

        self.lbl = QLabel("Esperando clic…")
        self.btn = QPushButton("Saludar")

        layout = QVBoxLayout(self)
        layout.addWidget(self.lbl)
        layout.addWidget(self.btn)

        # Conectar el botón al slot
        self.btn.clicked.connect(self.on_saludar)

    @Slot()
    def on_saludar(self):
        self.lbl.setText("¡Hola! Señal recibida 🙂")
        # Emitir la señal con un mensaje
        self.saludado.emit("Saludé correctamente")

