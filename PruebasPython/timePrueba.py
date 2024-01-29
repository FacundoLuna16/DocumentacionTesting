def parsear_dni(cuil):
    partes = cuil.split("-")
    return {'DNI': partes[1]}

# Ejemplo
cuil= "20-12345678-9"
info_DNI = parsear_dni(cuil)
print(info_DNI)