import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from t1_switch import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    # Accedemos al checkbox (debe existir en Ui_MainWindow)
    ui.chkSwitch.setStyleSheet("""
        QCheckBox::indicator { width: 46px; height: 24px; }
        QCheckBox::indicator:unchecked { border-radius: 12px; background:#ccc; }
        QCheckBox::indicator:checked { border-radius: 12px; background:#2ecc71; }
    """)

    # Cambiar texto dinámicamente según el estado
    ui.chkSwitch.toggled.connect(lambda s: ui.chkSwitch.setText("ON" if s else "OFF"))

    window.show()
    sys.exit(app.exec())
