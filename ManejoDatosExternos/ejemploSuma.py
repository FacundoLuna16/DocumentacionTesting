import sqlite3

class BaseDatosSQLite:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.conexion = sqlite3.connect(nombre_archivo)
        self.cursor = self.conexion.cursor()

    def ejecutar_consulta(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.conexion.close()

    def obtener_datos_tabla(self):
        consulta_sql = "SELECT a, b, resultado FROM suma"
        return self.ejecutar_consulta(consulta_sql)

def ejemplo_uso_sqlite():
    base_datos = BaseDatosSQLite('datosSuma.db')

    try:
        datos_tabla = base_datos.obtener_datos_tabla()
        print(datos_tabla)
    finally:
        base_datos.cerrar_conexion()

if __name__ == '__main__':
    ejemplo_uso_sqlite()
