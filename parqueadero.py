n = int(input("Cantidad de vehiculos: "))

cupos = 0

while cupos < n and cupos < 30:
    placa = input("Placa: ")
    tipo = input("Tipo de usuario(E/D/V): ")
    hora = int(input("Hora(formato 24h): "))
    permanencia = float(input("Horas de permanencia: "))

    # Calculo de tarifa segun tipo de usuario
    if tipo == "E":
        if permanencia <= 2:
            cobro = 0.0
        else:
            cobro = (permanencia - 2) * 800
    elif tipo == "D":
        cobro = permanencia * 500
    else:
        if permanencia <= 1:
            cobro = 1500.0
        else:
            cobro = 1500 + (permanencia - 1) * 1200

    print("Cobro: $", cobro)

    cupos += 1