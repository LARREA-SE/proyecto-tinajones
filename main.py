import sys
from PyQt5.QtWidgets import QApplication

from controllers.estacion_controller import EstacionController
from views.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    ventana = MainWindow(EstacionController())
    ventana.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
