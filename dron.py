X_MIN_FLO = float(-2000)
Y_MIN_FLO = float(-2000)
Z_MIN_FLO = float(0)

X_MAX_FLO = float(2000)
Y_MAX_FLO = float(2000)
Z_MAX_FLO = float(2000)

x_actual_flo = float(0)
y_actual_flo = float(0)
z_actual_flo = float(0)

while True:
    print("Posicion actual del dron",x_actual_flo,", ",y_actual_flo,", ",z_actual_flo,".")
    print("Elige tu ubicacion introduciendo el eje X e Y (X e Y maximo 2000 y minimo -2000) y (Z maximo 2000 y minimo 0)")
    
    print("Dime tu posicion X")
    posicion_usuario_x_flo = float(input(""))

    print("Dime tu posicion Y")
    posicion_usuario_y_flo = float(input(""))

    print("Dime tu posicion Z")
    posicion_usuario_z_flo = float(input(""))

    