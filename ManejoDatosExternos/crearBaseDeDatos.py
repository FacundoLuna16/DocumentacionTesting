import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('datosSuma.db')
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS suma (
        a INTEGER,
        b INTEGER,
        resultado INTEGER
    )
''')

# Insertar datos
cursor.execute("INSERT INTO suma (a, b, resultado) VALUES (2, 3, 5)")
cursor.execute("INSERT INTO suma (a, b, resultado) VALUES (0, 0, 0)")
cursor.execute("INSERT INTO suma (a, b, resultado) VALUES (-1, 1, 0)")

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
