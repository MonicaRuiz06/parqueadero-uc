n = int(input("Cantidad de vehiculos: "))

cupos = 0
total_recaudado = 0.0
estudiantes = 0
docentes = 0
visitantes = 0
suma_horas = 0.0

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
        cobro = 5000
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

    total_recaudado += cobro
    suma_horas += permanencia
    if tipo == "E":
        estudiantes += 1
    elif tipo == "D":
        docentes += 1
    else:
        visitantes += 1

    cupos += 1
    
if cupos == 30:
    print("PARQUEADERO LLENO")
if cupos > 0:
    promedio = suma_horas / cupos
else:
    promedio = 0.0
ocupacion = cupos / 30 * 100



print("\n====== RESUMEN DEL DIA ======")
print("Vehiculos registrados:", str(cupos) + "/30")
print("Ocupacion:", str(round(ocupacion, 1)) + "%")
print("Recaudo total: $" + str(round(total_recaudado, 2)))
print("Estudiantes:", estudiantes, "| Docentes:", docentes, "| Visitantes:", visitantes)
print("Promedio de permanencia:", round(promedio, 1), "horas")
print("==============================")
    



