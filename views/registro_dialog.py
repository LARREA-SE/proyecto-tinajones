from PyQt5.QtCore import QRegularExpression, Qt
from PyQt5.QtGui import QRegularExpressionValidator
from PyQt5.QtWidgets import (
    QDialog, QFormLayout, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
)


class RegistroDialog(QDialog):
    """Ventana modal de registro."""

    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.setWindowTitle("Registrar Estacion Hidrica")
        self.setModal(True)
        self.setMinimumWidth(340)

        self.txt_compuerta = QLineEdit()
        self.txt_compuerta.setPlaceholderText("Ej: Compuerta 1")
        self.txt_compuerta.setValidator(
            QRegularExpressionValidator(QRegularExpression(r"^[A-Za-z0-9ÁÉÍÓÚáéíóúÑñ \-]{0,50}$"))
        )

        self.txt_porcentaje = QLineEdit()
        self.txt_porcentaje.setPlaceholderText("0 - 100")
        self.txt_porcentaje.setValidator(
            QRegularExpressionValidator(QRegularExpression(r"^\d{0,3}([.,]\d{0,2})?$"))
        )

        self.txt_caudal = QLineEdit()
        self.txt_caudal.setPlaceholderText("m³/s")
        self.txt_caudal.setValidator(
            QRegularExpressionValidator(QRegularExpression(r"^\d{0,8}([.,]\d{0,2})?$"))
        )

        form = QFormLayout()
        form.addRow("Compuerta:", self.txt_compuerta)
        form.addRow("Porcentaje llenado (%):", self.txt_porcentaje)
        form.addRow("Caudal (m³/s):", self.txt_caudal)

        btn_guardar = QPushButton("Guardar")
        btn_cancelar = QPushButton("Cancelar")
        btn_guardar.clicked.connect(self.guardar)
        btn_cancelar.clicked.connect(self.reject)

        botones = QHBoxLayout()
        botones.addStretch()
        botones.addWidget(btn_guardar)
        botones.addWidget(btn_cancelar)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(botones)

    def guardar(self):
        try:
            ok, mensaje = self.controller.registrar(
                self.txt_compuerta.text(),
                self.txt_porcentaje.text(),
                self.txt_caudal.text(),
            )
        except Exception as e:
            QMessageBox.critical(self, "Error de base de datos", str(e))
            return

        if not ok:
            QMessageBox.warning(self, "Datos invalidos", mensaje)
            return  # no se cierra el programa ni el dialogo

        if "ALERTA" in mensaje:
            QMessageBox.warning(self, "Alerta", mensaje)
        else:
            QMessageBox.information(self, "Registro exitoso", mensaje)
        self.accept()
