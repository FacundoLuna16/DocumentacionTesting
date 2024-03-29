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


if __name__ == "__main__":
    config = {
        'host': 'localhost',
        'user': 'dev',
        'password': 'merlinData',
        'database': 'merlin'
    }

    cargador = CargadorDatosMySQL("localhost", "dev", "merlinData", "merlin")
    # o tambien
    # cargador = CargadorDatosMySQL(**config)
    print(f"instanciado")

    cargador.conectar()
    print(f"conectado")

    cargador.mostrar_datos()
    print(f"mostrado")

    cargador.desconectar()
    print(f"desconectado")
