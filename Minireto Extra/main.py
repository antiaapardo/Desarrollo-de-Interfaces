import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QTabWidget, QCheckBox, QHBoxLayout
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt


from t1_switch import Ui_MainWindow as Ui_Switch
from t2_moneylineedit import MoneyLineEdit
from t3_batterywidget import BatteryWidget
from t4_searchinput import SearchInput

import resources_rc 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Panel de Mini-Tareas")
        self.setWindowIcon(QIcon("icono.png"))
        self.resize(900, 600)

    
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

      
        self.add_task_switch()
        self.add_task_moneylineedit()
        self.add_task_battery()
        self.add_task_search()

        
        self.statusBar().showMessage("Listo")



    def add_task_switch(self):
        w = QWidget()
        layout = QVBoxLayout(w)

        chk = QCheckBox("OFF")
        chk.setStyleSheet("""
            QCheckBox::indicator { width: 46px; height: 24px; }
            QCheckBox::indicator:unchecked { border-radius: 12px; background:#ccc; }
            QCheckBox::indicator:checked { border-radius: 12px; background:#2ecc71; }
        """)
        chk.toggled.connect(lambda s: chk.setText("ON" if s else "OFF"))

        layout.addWidget(QLabel("Interruptor ON/OFF:"))
        layout.addWidget(chk)
        layout.addStretch()
        self.tabs.addTab(w, "T1: Switch")

    def add_task_moneylineedit(self):
        w = QWidget()
        layout = QVBoxLayout(w)

        txt = MoneyLineEdit()
        lbl = QLabel("Valor: 0.00 €")
        txt.valueChanged.connect(lambda v: lbl.setText(f"Valor: {v:.2f} €"))

        layout.addWidget(QLabel("Introduce cantidad:"))
        layout.addWidget(txt)
        layout.addWidget(lbl)
        layout.addStretch()
        self.tabs.addTab(w, "T2: MoneyLineEdit")

    def add_task_battery(self):
        w = QWidget()
        layout = QVBoxLayout(w)

        battery = BatteryWidget()
        layout.addWidget(QLabel("Nivel de batería:"))
        layout.addWidget(battery)
        layout.addStretch()
        self.tabs.addTab(w, "T3: Battery")

    def add_task_search(self):
        w = QWidget()
        layout = QVBoxLayout(w)

        search = SearchInput()
        layout.addWidget(QLabel("Campo de búsqueda:"))
        layout.addWidget(search)
        layout.addStretch()
        self.tabs.addTab(w, "T4: SearchInput")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
