""" 
1. Escribir un programa que pregunte al usuario su nombre y su edad, si es mayor de edad pida el numero de cedula y muestre el nombre, la edad y el número de cédula ingresado, si no es mayor de edad, debe mostrar un mensaje que diga Lo siento Pepito, eres menor de edad. 

"""
def mayorEdadT2 ():
    name = str(input("Ingrese su nombre: "))
    age = int(input("Ingrese su edad: "))

    if age >= 18:
        docu = int(input("Ingrese su número de documento: "))
        print(f"DATOS INGRESADOS \n Nombre: {name}\n Edad: {age} \n N° de Cédula: {docu}")
    else:
        print(f"Lo siento {name}, eres menor de edad. ")




"""
2. Escribir un programa que pida al usuario dos números realizar la división entre estos dos y mostrar el resultado. Si el divisor es cero el programa debe mostrar un error.

""" 
def dividirT2 ():
    one = int(input("Ingrese el primer número: "))
    two = int(input("Ingrese el segundo número: "))

    if two != 0:
        print(one/two)
    else:
        print("El divisor no puede ser cero")



""" 
3. Escribir un programa que pida al usuario un número entero y muestre un mensaje si el número es par o impar.

"""
def parImparT2 ():
    numer = int(input("Ingrese un número: "))

    if numer % 2 == 0:
        print("El número", numer, "es par.")
    else:
        print("El número", numer, "es impar.")
 


""" 4. Escribir un programa que pida al usuario que ingrese una contraseña, luego solicitar que escriba de nuevo la contraseña, imprimir un mensaje que indique si la contraseña coincide o no.
"""

def validarPassT2 ():
    password = input("Ingrese su contraseña: ")
    password_confi = input("Confirme su contraseña: ")

    if password == password_confi:
        print("Las contraseñas coinciden")
    else:
        print("Las contraseñas NO coinciden") 



""" 
5. Escribir un programa que solicite al usuario un carácter y, si se ingresa mas de un carácter, imprimir un mensaje que indique que solo debe ser un carácter. si se ingresa un solo carácter y ese carácter es una vocal imprimir el mensaje “es una vocal”.  
"""

def caracterT2 ():
    caracter = input("Ingrese un caracter: ").lower()

    if len(caracter) > 1:
        print("Solo es permitido ingresar un caracter")
    elif caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u": #caracter in "aeiuo":
        print("El caracter que usted ingreso es una vocal") 
    else:
        print(f"Usted ingreso el caracter: {caracter}") 