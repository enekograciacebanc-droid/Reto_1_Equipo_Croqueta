x_actual_flo = float(0)
y_actual_flo = float(0)
z_actual_flo = float(0)

posicion_usuario_x_flo = float(0)
posicion_usuario_y_flo = float(0)
posicion_usuario_z_flo = float(0)

mcdonalds = ["mcdonalds",-1000,-500,2] #Nombre/X/Y/Z
rascacielos_alto = ["rascacielos_alto",100,650,20]
casa_de_pedro = ["casa_de_pedro",-50,10,2]
avion_que_por_algun_motivo_no_se_mueve = ["avion_que_por_algun_motivo_no_se_mueve",1500,-200,1200]
localizacion_usuario_1 = ["localizacion_usuario_1",0,0,0]
localizacion_usuario_2 = ["localizacion_usuario_2",0,0,0]
localizacion_usuario_3 = ["localizacion_usuario_3",0,0,0]

listadelistas_list = [mcdonalds,rascacielos_alto,casa_de_pedro,avion_que_por_algun_motivo_no_se_mueve,localizacion_usuario_1,localizacion_usuario_2,localizacion_usuario_3]
listadelistas_custom_list = [localizacion_usuario_1,localizacion_usuario_2,localizacion_usuario_3]

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
        print("¿Quieres moverte o añadir una localización?")
        print("0- volver")
        print("1- Mover dron")
        print("2- Modificar localización")
        eleccion_int = int(input(""))

        if(eleccion_int == 0):
            continue
        elif(eleccion_int == 1):
            print("Localizaciones actuales")
            print("")
            for x in listadelistas_list:
                print(x[0])
            print("")
            print("Escribe el nombre exacto de la localización a la que quieras moverte")
            eleccion_localizacion_str = input("")

            for x in listadelistas_list:
                if x[0] == eleccion_localizacion_str:
                    posicion_usuario_x_flo = float(x[1])
                    posicion_usuario_y_flo = float(x[2])
                    posicion_usuario_z_flo = float(x[3])
                    break

        elif(eleccion_int == 2):
            print("Localizaciones personalizadas actuales")
            print("")
            for x in listadelistas_custom_list:
                print(x[0])

            print("")
            print("Puedes modificar una de estas 3 localizaciones. ¿Cual quieres modificar? (escribe 1, 2 o 3)")
            eleccion_int = int(input())
            print("Selecciona el nombre de la localización (Se recomienda usar solo minusculas, no usar espacion y no usar tildes.)")
            customname_str = str(input())
            print("Selecciona la posición X (Min. -2000 Max. 2000)")
            customx_flo = float(input())
            if(customx_flo > 2000):
                print("Posición incorrecta, X se ajustará a 2000")
                customx_flo = float(2000)
            elif(customx_flo < -2000):
                print("Posición incorrecta, X se ajustará a -2000")
                customx_flo = float(-2000)
            
            print("Selecciona la posición Y (Min. -2000 Max. 2000)")
            customy_flo = float(input())
            if(customy_flo > 2000):
                print("Posición incorrecta, Y se ajustará a 2000")
                customy_flo = float(2000)
            elif(customy_flo < -2000):
                print("Posición incorrecta, Y se ajustará a -2000")
                customy_flo = float(-2000)
            
            print("Selecciona la posición Z (Min. 0 Max. 2000)")
            customz_flo = float(input())
            if(customz_flo > 2000):
                print("Posición incorrecta, Z se ajustará a 2000")
                customz_flo = float(2000)
            elif(customz_flo < 0):
                print("Posición incorrecta, Z se ajustará a 0")
                customz_flo = float(0)

            if(eleccion_int == 1):
                localizacion_usuario_1[0] = customname_str
                localizacion_usuario_1[1] = customx_flo
                localizacion_usuario_1[2] = customy_flo
                localizacion_usuario_1[3] = customz_flo
                print("Tu nueva localización es",localizacion_usuario_1)
                continue
            elif(eleccion_int == 2):
                localizacion_usuario_2[0] = customname_str
                localizacion_usuario_2[1] = customx_flo
                localizacion_usuario_2[2] = customy_flo
                localizacion_usuario_2[3] = customz_flo
                print("Tu nueva localización es",localizacion_usuario_2)
                continue
            elif(eleccion_int == 3):
                localizacion_usuario_3[0] = customname_str
                localizacion_usuario_3[1] = customx_flo
                localizacion_usuario_3[2] = customy_flo
                localizacion_usuario_3[3] = customz_flo
                print("Tu nueva localización es",localizacion_usuario_3)
                continue
            else:
                print("Seleccion incorrecta")
                continue

        else:
            print("Seleccion incorrecta")
            continue

    elif(eleccion_int == 2):

        print("Elige a que ubicación quieres que el dron se dirija con los ejes. Ejes X e Y (maximo 2000 y minimo -2000) eje Z (maximo 2000 y minimo 0)")
        print("Si se elige una posición no valida, el programa eligirá una automáticamente.")
        print("")
        print("Posicion X")
        posicion_usuario_x_flo = float(input(""))
        if(posicion_usuario_x_flo > 2000):
            print("Posición incorrecta, X se ajustará a 2000")
            posicion_usuario_x_flo = float(2000)
        elif(posicion_usuario_x_flo < -2000):
            print("Posición incorrecta, X se ajustará a -2000")
            posicion_usuario_x_flo = float(-2000)

        print("Posicion Y")
        posicion_usuario_y_flo = float(input(""))
        if(posicion_usuario_y_flo > 2000):
            print("Posición incorrecta, Y se ajustará a 2000")
            posicion_usuario_y_flo = float(2000)
        elif(posicion_usuario_y_flo < -2000):
            print("Posición incorrecta, Y se ajustará a -2000")
            posicion_usuario_y_flo = float(-2000)

        print("Posicion Z")
        posicion_usuario_z_flo = float(input(""))
        if(posicion_usuario_z_flo > 2000):
            print("Posición incorrecta, Z se ajustará a 2000")
            posicion_usuario_z_flo = float(2000)
        elif(posicion_usuario_z_flo < 0):
            print("Posición incorrecta, Z se ajustará a 0")
            posicion_usuario_z_flo = float(0)
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

    x_actual_flo = posicion_usuario_x_flo
    y_actual_flo = posicion_usuario_y_flo
    z_actual_flo = posicion_usuario_z_flo

print("Cerrando el programa.")