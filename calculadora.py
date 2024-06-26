num1 = int(input("numero 1: ")) 
num2 = int(input("numero 2: ")) 
num3 = int(input("numero 3: "))

valor = 0
while True:
    print("""seleccione opcion
            1.- Suma 
            2.- Resta
            3.- Multiplicacion
            4.- Divisón
            5.- Suma 3 valores
            6.- Salir del programa
        """)

    valor = int(input("Elige una opcion:\n --> ") )     

    if valor == 1:
        print("La suma es: ",num1+num2)
    elif valor == 2:
        print("La resta es: ",num1-num2)
    elif valor == 3:
        print("La multiplicación es: ",num1*num2)
    elif valor == 4:
        print("La división es: ",num1/num2)
    elif valor == 5:
        print("La suma de los tres valores es: ",num1+num2+num3)
    elif valor == 6:
        print("Saliendo...")
        break
    else:
        print("Opcion incorrecta")