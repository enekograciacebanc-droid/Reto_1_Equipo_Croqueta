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
                while 1 == 1:
                    print("===============")
                    print("Restaurantes")
                    print("===============")
                    print("1- Ali kebab")
                    print("2- Burgerwatssapp")
                    print("3- Bar pepe")
                    print("4- Bar tang-yuan-qing-song-xue-ming-jin")
                    print("5- salir")
                    restaurante_int=int(input(""))
                    if(restaurante_int==1):
                         print("Elegiste Ali Kebab")
                         print("1- kebab mixto 5€")
                         print("2- kebab de pollo 4€")
                         print("3- kebab de ternera 5€")
                         print("4- salir")
                         producto_int=int(input(""))
                        
                         if(producto_int==1):
                              dinero_flo+=5
                         elif(producto_int==2):
                              dinero_flo+=4
                         elif(producto_int==3):
                              dinero_flo+=5
                         elif(producto_int==4):
                              break

    
    else:
        print("Introduce un valor valido.")
        


print("Vuelve pronto.")
exit