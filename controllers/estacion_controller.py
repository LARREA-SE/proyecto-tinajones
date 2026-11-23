from models.estacion_model import EstacionHidricaModel


class EstacionController:
    def __init__(self):
        self.model = EstacionHidricaModel()

    def listar(self, busqueda=""):
        return self.model.listar(busqueda.strip())

    @staticmethod
    def evaluar_alerta(porcentaje):
        """Reglas del escenario (el mensaje NO se guarda en BD)."""
        if porcentaje < 30:
            return "ALERTA: SEQUIA / RESTRICCION"
        elif porcentaje <= 85:
            return "NIVEL OPERATIVO NORMAL"
        else:
            return "ALERTA: RIESGO DE DESBORDE"

    def registrar(self, compuerta, porcentaje, caudal):
        """Valida, guarda y devuelve (exito, mensaje)."""
        compuerta = compuerta.strip()
        if not compuerta or not str(porcentaje).strip() or not str(caudal).strip():
            return False, "Complete todos los campos."
        try:
            porcentaje = float(str(porcentaje).replace(",", "."))
            caudal = float(str(caudal).replace(",", "."))
        except ValueError:
            return False, "Porcentaje y caudal deben ser numericos."
        if not (0 <= porcentaje <= 100):
            return False, "El porcentaje de llenado debe estar entre 0 y 100."
        if caudal < 0:
            return False, "El caudal no puede ser negativo."

        mensaje = self.evaluar_alerta(porcentaje)
        self.model.registrar(compuerta, porcentaje, caudal)
        return True, mensaje
