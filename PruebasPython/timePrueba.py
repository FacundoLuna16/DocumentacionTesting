import time

fecha_actual = time.localtime()
print("Fecha y hora actual:", time.strftime("%Y-%m-%d %H:%M:%S", fecha_actual))

mes_actual = fecha_actual.tm_mon
print("Mes de la fecha en curso:", mes_actual)

anio_actual = fecha_actual.tm_year
print("Año de la fecha en curso:", anio_actual)


def nueva_fecha():
    fecha = time.localtime()
    anio = fecha.tm_year
    print("Año de la fecha en curso:", anio)


nueva_fecha()
