# En este documento vamos a ver la conexion con base de datos mysql

MySQL es un sistema de gestión de bases de datos **relacional**, y Python proporciona diversas herramientas para interactuar con él de manera efectiva.

####  <span style="color:red">Importante!</span> Instalacion de dependencia

Utilizaremos para establecer la conexion con la base de datos la biblioteca `mysql-connector-python` con el comando.

```bash
pip install mysql-connector-python
```

#### Conexion con la base de datos
Ahora, veamos cómo establecer una conexión con una base de datos MySQL utilizando Python
y como venimos hablando, esto lo colocaremos en una clase
```python
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
            self.cursor.execute("SELECT * FROM suma")

            resultados = self.cursor.fetchall()
            print("\nDatos en la tabla:")
            for resultado in resultados:
                print(resultado)

        except mysql.connector.Error as e:
            print(f"Error al mostrar datos: {e}")
```
Este código intentará establecer una conexión con la base de datos y mostrará un mensaje indicando si la conexión fue exitosa o si ocurrió algún error.

A esto lo podemos probar colocando al final del documento (donde esta ubicada la clase) lo siguiente:

```python
if __name__ == "__main__":
    # config = {
    #     'host': 'localhost',
    #     'user': 'dev',
    #     'password': 'merlinData',
    #     'database': 'merlin'
    # }

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
```

## Creacion de una instancia de mysql con Docker