import mysql.connector


class CargadorDatosMySQL:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos")
                self.cursor = self.conexion.cursor()

        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def desconectar(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")

    def cargar_datos_desde_dump(self, dump_file):
        try:
            with open(dump_file, 'r') as archivo_sql:
                instrucciones_sql = archivo_sql.read()

                # Ejecutar instrucciones SQL
                self.cursor.execute(instrucciones_sql)

                # Confirmar los cambios
                self.conexion.commit()
                print("Datos cargados exitosamente desde el archivo SQL")

        except mysql.connector.Error as e:
            print(f"Error al cargar datos desde el archivo SQL: {e}")

    def mostrar_datos(self):
        try:
            # Seleccionar todos los datos de la tabla
            self.cursor.execute("SELECT * FROM suma")

            # Obtener y mostrar los resultados
            resultados = self.cursor.fetchall()
            print("\nDatos en la tabla:")
            for resultado in resultados:
                print(resultado)

        except mysql.connector.Error as e:
            print(f"Error al mostrar datos: {e}")


# Ejemplo de uso
if __name__ == "__main__":
    # Configura los parámetros de conexión
    config = {
        'host': 'localhost',  # o la IP de tu máquina si estás ejecutando Docker en otro lugar
        'user': 'dev',
        'password': 'merlinData',
        'database': 'merlin'
    }

    # Crea una instancia de la clase
    cargador = CargadorDatosMySQL(**config)

    # Conecta a la base de datos
    cargador.conectar()

    # Carga los datos desde el archivo dump.sql
    cargador.cargar_datos_desde_dump('dump.sql')

    # Muestra los datos de la tabla
    cargador.mostrar_datos()

    # Desconecta cuando hayas terminado
    cargador.desconectar()
