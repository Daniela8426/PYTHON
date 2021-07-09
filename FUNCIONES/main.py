""" crear una fucnion que muestre el nombre y el apellido """

""" def nom (name, apellido):
    print("Hola", name,apellido)

name = input("Digite su Nombre: ")
ape = input("Digite su Apellido: ")
nom(name, ape)

"""


""" 
def f1():
    x=100
    print(x)

x=+1

f1() 

"""


""" 
EJERCICIOS DE CLASE

1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@". 

"""

""" def validarCorreo(a):
    buscar = a.rfind("@")

    if buscar < 0:
        print("Correo Invalido")
    
    else:
        print("Correo Valido")


correo = input("Ingrese su correo: ")
validarCorreo(correo)
 """


""" 
2 Escribir una función que, dado un número  de CC y el nombre, retorne el documento y el nombre si el número es válido y False retorne el mensaje "documento equivocado". Para que un número de CC sea válido debe tener entre 9 y 11 dígitos.

"""

def validarCorreo(docu,name):

    cuenta = len(docu)

    if cuenta in range(9, 11): #9 <= cuenta <= 11:
        print(f"---------\nDatos\nN° documento:{docu}\nNombre: {name}")
    
    else:
        print("Documento Equivocado")


docu = input("Ingrese su número de documento: ")
name = input("Ingrese su nombre completo: ")
validarCorreo(docu,name)