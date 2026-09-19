n = int(input("Cantidad de vehiculos: "))

cupos = 0

while cupos < n and cupos < 30:
    placa = input("Placa: ")
    tipo = input("Tipo (E/D/V): ")
    hora = float(input("Hora(formato 24h): "))
    permanencia = float(input("Horas de permanencia: "))

    cupos += 1