from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QLabel, QMessageBox
)

from views.registro_dialog import RegistroDialog


class MainWindow(QMainWindow):
    """Ventana principal: listado + busqueda en tiempo real + boton Nuevo."""

    COLUMNAS = ["ID", "Compuerta", "% Llenado", "Caudal (m³/s)"]

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Monitoreo Hidrico - Reservorio Tinajones")
        self.resize(700, 450)

        self.txt_buscar = QLineEdit()
        self.txt_buscar.setPlaceholderText("Buscar por compuerta, porcentaje o caudal...")
        self.txt_buscar.textChanged.connect(self.cargar_tabla)  # tiempo real

        self.btn_nuevo = QPushButton("Nuevo")
        self.btn_nuevo.clicked.connect(self.abrir_registro)

        self.tabla = QTableWidget(0, len(self.COLUMNAS))
        self.tabla.setHorizontalHeaderLabels(self.COLUMNAS)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        superior = QHBoxLayout()
        superior.addWidget(self.txt_buscar)
        superior.addWidget(self.btn_nuevo)

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.addWidget(QLabel("Estaciones registradas"))
        layout.addLayout(superior)
        layout.addWidget(self.tabla)
        self.setCentralWidget(central)

        self.cargar_tabla()

    def cargar_tabla(self):
        try:
            filas = self.controller.listar(self.txt_buscar.text())
        except Exception as e:
            QMessageBox.critical(self, "Error de base de datos", str(e))
            return
        self.tabla.setRowCount(len(filas))
        for r, fila in enumerate(filas):
            for c, valor in enumerate(fila):
                self.tabla.setItem(r, c, QTableWidgetItem(str(valor)))

    def abrir_registro(self):
        dialogo = RegistroDialog(self.controller, self)
        if dialogo.exec_():
            self.cargar_tabla()  # se actualiza despues de mostrar el mensaje
