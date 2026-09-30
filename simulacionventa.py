#Programa de prueba simulando un menú para pedir comida

dinero_flo = 0

while 1==1:
    print("======================")
    print("Menú de Venta (Prueba)")
    print("======================")
    print("")
    print("0- Cerrar programa")
    print("1- Pedir")
    seleccion_int = int(input())

    if(seleccion_int == 0):
        break

    elif(seleccion_int == 1):
        while 1==1:
            print("===============")
            print("¿Tienes hambre?")
            print("===============")
            print("")
            print("0- Volver")
            print("1- Ver Carrito")
            print("2- Ver Productos")
            seleccion_int = int(input())

            if(seleccion_int == 0):
                    break
            
            elif(seleccion_int == 1):
                    break
            
            elif(seleccion_int == 2):
                    break
                 

    else:
        print("Introduce un valor valido.")  
        


print("Vuelve pronto.")
exit