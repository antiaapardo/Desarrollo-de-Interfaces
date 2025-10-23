import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog,QMessageBox, QFileDialog, QFontDialog, QInputDialog,QColorDialog, QLabel, QSizePolicy,QProgressDialog)
from PySide6.QtGui import QColor, QFont
from PySide6.QtCore import Qt, QTimer
from GestorDeTareas import Ui_MainWindow
import NuevoProyecto
import ConfirmarAccion


class Confirmar(QDialog, ConfirmarAccion.Ui_ConfirmarAccion):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent_window = parent 
        
       
        self.lblPreferencias.setWordWrap(True)  # Permite que el texto salte de línea
        self.lblPreferencias.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.lblPreferencias.setGeometry(10, 10, 600, 200)  # Más alto
        self.lblPreferencias.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) # pyright: ignore[reportUndefinedVariable]
            
        self.lblPreferencias.setWordWrap(True)
        self.lblPreferencias.setStyleSheet("font-size: 16px; color: black;")
        self.lblPreferencias.setGeometry(10, 10, 600, 80)  # x, y, ancho, alto
        self.lblPreferencias.show()

        self.buttonBox.accepted.connect(self.confirmar_accion)
        self.buttonBox.rejected.connect(self.cancelar_accion)

    def confirmar_accion(self): 

        self.parent_window.statusBar().showMessage("Acción confirmada")
        print("Datos eliminados")
        self.reject()

    def cancelar_accion(self):
        if self.parent_window:
            self.parent_window.statusBar().showMessage("Operación abortada por el usuario")
        self.reject()

class MiDialogo(QDialog, NuevoProyecto.Ui_NuevoProyecto):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent_window = parent  # guardar referencia a la ventana principal

        self.buttonBox.accepted.connect(self.confirmar_proyecto)
        self.buttonBox.rejected.connect(self.cancelar_proyecto)

    def confirmar_proyecto(self):
        nombre = self.lineNombre.text().strip()
        if nombre:
            QMessageBox.information(
                self,
                "Proyecto creado",
                f"Proyecto {nombre} creado correctamente."
            )
            self.accept()
        else:
            QMessageBox.warning(
                self,
                "Error",
                "Debe ingresar un nombre de proyecto."
            )

    def cancelar_proyecto(self):
        if self.parent_window:
            self.parent_window.statusBar().showMessage("Operación cancelada")
        self.reject()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BtnNuevoProyecto.clicked.connect(self.NuevoProyecto)
        self.BtnConfirmar.clicked.connect(self.ConfirmarAccion)
        self.BtnMensajes.clicked.connect(self.Mensajes)
        self.BtnPreferencias.clicked.connect(self.preferencias)
        self.BtnExportar.clicked.connect(self.exportar)
        
    def exportar(self):
        # Crear QProgressDialog
        progress = QProgressDialog("Exportando informe...", "Cancelar", 0, 100, self)
        progress.setWindowTitle("Exportar Informe")
        progress.setWindowModality(Qt.WindowModal)
        progress.setMinimumDuration(0)  # Mostrar inmediatamente
        progress.setAutoClose(False)
        progress.setValue(0)

        # Variable para progreso
        self.progreso_actual = 0

        # Función para actualizar progreso
        def actualizar_progreso():
            if progress.wasCanceled():
                timer.stop()
                QMessageBox.warning(self, "Exportación", "Exportación cancelada por el usuario")
                return
            self.progreso_actual += 1
            progress.setValue(self.progreso_actual)
            if self.progreso_actual >= 100:
                timer.stop()
                progress.setValue(100)
                QMessageBox.information(self, "Exportación", "Exportación finalizada correctamente")

        # Crear timer para simular progreso
        timer = QTimer(self)
        timer.timeout.connect(actualizar_progreso)
        timer.start(50)  # Avanza cada 50 ms (~5 segundos para completar)
        

    def preferencias(self):
    # 1. Seleccionar carpeta de guardado
        ruta = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta de guardado", "/home")
      

        color_actual = self.lblPreferencias.palette().color(self.lblPreferencias.foregroundRole())
        color = QColorDialog.getColor(color_actual, self, "Seleccionar color del texto")
        if color.isValid():
            self.lblPreferencias.setStyleSheet(f"color: {color.name()};")
            print(f"Color seleccionado: {color.name()}")
        else:
            print("No se seleccionó ningún color.")
            
        dialogo_fuente = QFontDialog(self)
        dialogo_fuente.setCurrentFont(self.lblPreferencias.font())
        if dialogo_fuente.exec():
            fuente = dialogo_fuente.currentFont()
            self.lblPreferencias.setFont(fuente)
            print(f"Fuente seleccionada: {fuente.family()}, Tamaño: {fuente.pointSize()}pt")
            
        # 3. Ingresar nombre de usuario
        nombre, ok = QInputDialog.getText(self, "Nombre de usuario", "Ingrese su nombre:")
        if ok and nombre:
            self.usuario = nombre
        else:
            self.usuario = "Usuario sin nombre"


        # 5. Aplicar preferencias al QLabel
        self.lblPreferencias.setText(
            f"Usuario: {self.usuario}, Color: {color.name()}, Fuente: {fuente.family()} {fuente.pointSize()}pt, Ruta: {ruta}"
        )
       

        
    def Mensajes(self):
         QMessageBox.information(self, "Information", "Operacion completada con exito")
         QMessageBox.warning(self, "Warning", "Estás a punto de sobrescribir un archivo existente.")
         QMessageBox.critical(self, "Critical", "Error grave en el proceso de guardado.")
         respuesta = QMessageBox.question(self,"Question","¿Deseas continuar con la operación?")

         if respuesta == QMessageBox.StandardButton.Yes: 
             print("El usuario eligio Si")
         else: 
             print("El usuario eligio que No")
 

    def NuevoProyecto(self):
        dialogo = MiDialogo(self)  # pasar self como padre
        dialogo.exec()

    def ConfirmarAccion(self):
        ConfirmarAccion = Confirmar(self)  
        ConfirmarAccion.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
