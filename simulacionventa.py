#Programa de prueba simulando un menú para pedir comida

dinero_flo = 0
producto_elegido_list = [] #Aqui empezamos con la lista de los productos
total = 0

while True: #Menu principal del programa de aqui se ramifica todo 
    print("======================")
    print("Menú de Venta (Prueba)")
    print("======================")
    print("")
    print("0- Cerrar programa")
    print("1- Pedir")
    print("2- Pagar")
    seleccion_int = int(input())

    if seleccion_int == 0:
        break
    elif seleccion_int == 1:   #este es el segundo menu donde se ramifican los restaurantes y los menus 
        while True:
            print("===============")
            print("¿Tienes hambre?")
            print("===============")
            print("")
            print("0- Volver")
            print("1- Ver Carrito")
            print("2- Ver Productos")
            seleccion_int = int(input())

            if seleccion_int == 0:
                break
            elif seleccion_int == 1:
                print("El total de lo gastado es", total)
                print(" Y sus productos elegidos son: ")
                for producto in producto_elegido_list:
                    print("- ", producto)
            elif seleccion_int == 2:
                while True:
                    print("===============")
                    print("Restaurantes")
                    print("===============")
                    print("1- Ali kebab")
                    print("2- Burgerwatssapp")
                    print("3- Bar pepe")
                    print("4- Bar tang-yuan-qing-song-xue-ming-jin")
                    print("5- Ver Carrito")
                    print("6- volver")
                    restaurante_int = int(input(""))

                    if restaurante_int == 1:
                        while True:
                            print("Elegiste Ali Kebab")
                            print("1- kebab mixto 5€")
                            print("2- kebab de pollo 4€")
                            print("3- kebab de ternera 5€")
                            print("4- volver")
                            producto_int = int(input(""))

                            if producto_int == 1:
                                total += 5
                                producto_elegido_list.append("kebab mixto")   #append se utiliza para añadir datos a la lista en este caso kebab mixto
                                print("añadido al carro")
                            elif producto_int == 2:
                                total += 4
                                producto_elegido_list.append("kebab de pollo")
                                print("añadido al carro")
                            elif producto_int == 3:
                                total += 5
                                producto_elegido_list.append("kebab de ternera")
                                print("añadido al carro")
                            elif producto_int == 4:
                                break
                            else:
                                print("Introduce un valor valido.")

                    elif restaurante_int == 2:
                        while True:
                            print("Elige un producto de Burgerwatssapp")
                            print("1- Hamburguesa de whatsapp 5€")
                            print("2- Menu super hyper mega deluxe whatsapp 20€")
                            print("3- Hamburguesa super loquendo_777 10€")
                            print("4- volver")
                            producto_int = int(input(""))

                            if producto_int == 1:
                                total += 5
                                producto_elegido_list.append("Hamburguesa de whatsapp")
                                print("añadido al carro")
                            elif producto_int == 2:
                                total += 20
                                producto_elegido_list.append("Menu super hyper mega deluxe whatsapp")
                                print("añadido al carro")
                            elif producto_int == 3:
                                total += 10
                                producto_elegido_list.append("Hamburguesa super loquendo_777")
                                print("añadido al carro")
                            elif producto_int == 4:
                                break
                            else:
                                print("Introduce un valor valido.")

                    elif restaurante_int == 3:
                        while True:
                            print("Elige su producto de Bar Pepe")
                            print("1- Bocata lomo ya 5€")
                            print("2- Bocadillo de tortilla 4€")
                            print("3- Bocadillo de chope 5€")
                            print("4- volver")
                            producto_int = int(input(""))

                            if producto_int == 1:
                                total += 5
                                producto_elegido_list.append("Bocata lomo ya")
                                print("añadido al carro")
                            elif producto_int == 2:
                                total += 4
                                producto_elegido_list.append("Bocadillo de tortilla")
                                print("añadido al carro")
                            elif producto_int == 3:
                                total += 5
                                producto_elegido_list.append("Bocadillo de chope")
                                print("añadido al carro")
                            elif producto_int == 4:
                                break
                            else:
                                print("Introduce un valor valido.")

                    elif restaurante_int == 4:
                        while True:
                            print("Elige su producto del bar tang-yuan-qing-song-xue-ming-jin")
                            print("1- Menu Tang(pastel Hu) 10€")
                            print("2- menu Yuan(hot pot de cordero) 10€")
                            print("3- menu Qing(Jiu Zhuan Da Chang) 10€")
                            print("4- volver")
                            producto_int = int(input(""))

                            if producto_int == 1:
                                total += 10
                                producto_elegido_list.append("Menu Tang")
                                print("añadido al carro")
                            elif producto_int == 2:
                                total += 10
                                producto_elegido_list.append("Menu Yuan")
                                print("añadido al carro")
                            elif producto_int == 3:
                                total += 10
                                producto_elegido_list.append("Menu Qing")
                                print("añadido al carro")
                            elif producto_int == 4:
                                break
                            else:
                                print("Introduce un valor valido.")

                    elif(restaurante_int == 5):
                         print("-----SU CARRITO-----")
                    
                         if len(producto_elegido_list) == 0:
                               print("Su carro esta vacio")
                    
                         else:
                              for producto in producto_elegido_list:
                                   print("- " + producto)
                                   print("El total de lo gastado es " +str(total) + "€")
                                            #El bucle imprime cada producto de tu lista uno a uno con un guión (- producto), pero como la línea del total está dentro del bucle, el precio se repetirá debajo de cada comida Para mostrar el precio una sola vez al final, saca la línea del total del bucle quitándole espacios a la izquierda


                    
                    elif restaurante_int == 6:
                        break  #si le das al 6 rompe el bucle y vuelve al menu anterior 
                    
                    else:
                        print("Introduce un valor valido.")
                        break
            else:
                print("Introduce un valor valido.")
#Ese bloque se activa cuando el usuario pulsa el 2. Primero muestra el precio total acumulado (str(total)) y el texto de introducción. Después, el bucle for lee tu lista producto_elegido_list e imprime cada comida en una línea independiente con un guión delante. Está perfectamente redactado porque el mensaje del dinero solo sale una vez antes de desplegar toda la lista de productos.
    elif seleccion_int == 2:
        print("El total de lo gastado es " + str(total))
        print(" Y sus productos elegidos son: ")
        for producto in producto_elegido_list:
            print("- " + producto)
       
        break

    else:
        print("Introduce un valor valido.")# si sale un numero que no concuerda pasa esto 

print("Vuelve pronto.")
input("Presione para salir")