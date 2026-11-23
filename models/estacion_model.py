from database.conexion import get_connection


class EstacionHidricaModel:
    """Acceso a datos: solo llama a procedimientos almacenados."""

    def listar(self, busqueda=""):
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.callproc("sp_listar_estaciones", [busqueda])
            filas = []
            for resultado in cur.stored_results():
                filas = resultado.fetchall()
            return filas
        finally:
            conn.close()

    def registrar(self, compuerta, porcentaje, caudal):
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.callproc("sp_registrar_estacion", [compuerta, porcentaje, caudal])
            conn.commit()
        finally:
            conn.close()
