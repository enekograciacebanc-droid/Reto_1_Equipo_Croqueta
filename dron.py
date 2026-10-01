x_actual_flo = float(0)
y_actual_flo = float(0)
z_actual_flo = float(0)

import math

while True:
    print("Posicion actual del dron",x_actual_flo,", ",y_actual_flo,", ",z_actual_flo,".")
    print("")

    print("¿Prefieres escoger una posición predefinida o introducir manualmente las coordenadas?")
    print("0- Cerrar Programa")
    print("1- Posición Predefinida")
    print("2- Coordenadas Manuales")
    eleccion_int = int(input(""))

    if(eleccion_int == 0):
        break
    elif(eleccion_int == 1):
        break
    elif(eleccion_int == 2):

        print("Elige a que ubicación quieres que el dron se dirija con los ejes. Ejes X e Y (maximo 2000 y minimo -2000) eje Z (maximo 2000 y minimo 0)")
        print("Si se elige una posición no valida, el programa eligirá una automáticamente.")
        print("")
        print("Posicion X")
        posicion_usuario_x_flo = float(input(""))
        if(posicion_usuario_x_flo > 2000):
            print("Posición incorrecta, X se ajustará a 2000")
            posicion_usuario_x_flo = 2000
        elif(posicion_usuario_x_flo < -2000):
            print("Posición incorrecta, X se ajustará a -2000")
            posicion_usuario_x_flo = -2000

        print("Posicion Y")
        posicion_usuario_y_flo = float(input(""))
        if(posicion_usuario_y_flo > 2000):
            print("Posición incorrecta, Y se ajustará a 2000")
            posicion_usuario_y_flo = 2000
        elif(posicion_usuario_y_flo < -2000):
            print("Posición incorrecta, Y se ajustará a -2000")
            posicion_usuario_y_flo = -2000

        print("Posicion Z")
        posicion_usuario_z_flo = float(input(""))
        posicion_usuario_z_flo = float(input(""))
        if(posicion_usuario_z_flo > 2000):
            print("Posición incorrecta, Z se ajustará a 2000")
            posicion_usuario_z_flo = 2000
        elif(posicion_usuario_z_flo < 0):
            print("Posición incorrecta, Z se ajustará a 0")
            posicion_usuario_z_flo = 0
    else:
        print("Seleccion incorrecta")
        continue

    distancia_z_flo = z_actual_flo + posicion_usuario_z_flo
    tiempo_estimado_z_flo = distancia_z_flo / 100

    print("En subir, el dron tardará", tiempo_estimado_z_flo, "minutos.")

    distancia_xy_flo = math.sqrt(math.pow((posicion_usuario_x_flo - x_actual_flo),2) + math.pow((posicion_usuario_y_flo - y_actual_flo),2))
    tiempo_estimado_xy_flo = distancia_xy_flo / 100

    print("En llegar a su destino, el dron tardará", tiempo_estimado_xy_flo, "minutos.")
    print("En total, el dron tardará", tiempo_estimado_xy_flo + tiempo_estimado_z_flo, "minutos.")
    print("")

print("Cerrando el programa.")