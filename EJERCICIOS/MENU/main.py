""" 
Ejercicio
hacer un menú donde la primera opción halla el área de un triangulo, segunda opción el volumen de un cubo, tercera opción calculadora básica, cuaeta opcion terminar el programa.

modelo del menu:

1 area de un triangulo
2 volumen de un cubo
3 calculadora basica
4 terminar programa 

"""


def menuT3():
    menu = int(input("-------------\nMenú: \nSeleccione una opción:\n1. Area de un triangulo.\n2. Volumen de un cubo.\n3. Calculadora básica.\n4. Terminar Programa\n"))

    while menu !=4:
        if menu == 1:

            base = int(input("Digite el valor de la base del triangulo en centímetros: "))
            altura = int(input("Digite el valor de la altura del triangulo en centímetros: "))
            print("El area de su triangulo es: ",base*altura/2)


        elif menu == 2:

            lado = int(input("Digite el valor de uno de los lados del cubo: "))
            print("El volumen de su cubo es: ",lado ** 3)


        elif menu == 3:
            num_one = int(input("Digite el valor del primer número: "))
            num_dos = int(input("Digite el valor del segundo número: "))

            print("\nLos resultados fueron:\nSuma:",num_one+num_dos,"\nResta:",num_one-num_dos,"\nMultiplicación:",num_one*num_dos,"\nDivisión:",num_one/num_dos)
        else:
            print("no digito ninguna opción")
    
        menu = int(input("-------------\nMenú: \nSeleccione una opción:\n1. Area de un triangulo.\n2. Volumen de un cubo.\n3. Calculadora básica.\n4. Terminar Programa\n"))