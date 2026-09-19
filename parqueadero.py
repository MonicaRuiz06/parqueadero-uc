n = int(input("Cantidad de vehiculos: "))

cupos = 0

while cupos < n and cupos < 30:
    placa = input("Placa: ")

    tipo = input("Tipo de usuario(E/D/V): ")
    hora = int(input("Hora(formato 24h): "))
    permanencia = float(input("Horas de permanencia: "))

    #validacion de hora 
    if hora < 0 or hora> 23:
        print(" error, porfavor verificar la hora, debe esta entre 0 y 23")
        continue

    #validacion de tipo usuario 
    if tipo != "E" and tipo != "D" and tipo != "V":
        print("Advertencia: este usuario, se tomara como visitante.")
        tipo = "V"

    #validacion de permanencia 
    if permanencia <= 0:
        print("rechazo de registro")
        continue

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
    # Descuento nocturno (despues de las 19:00 o antes de las 6:00)
    if hora > 19 or hora < 6:
        cobro = cobro * 0.90

    cobro = round(cobro, 2)


    print("Cobro: $", cobro)

    cupos += 1
    #
if cupos == 30:
    print("PARQUEADERO LLENO")





