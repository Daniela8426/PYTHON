"""
1- El usuario debe ingrese una cadena de texto, y si la cadena de texto tiene la vocal "a" 
hay que remplazar por la vocal "o"
"""


def buscaVocalT1():
    cadena = input("Ingrese la oración: ")

    busca_one = cadena.rfind("a") 

    if busca_one != -1:
        cadena_nueva = cadena.replace("a", "o")
        print("Las letras a de su oración fueron remplazadas por o, Resultado: ",cadena_nueva)
        
    else:
        print("Usted escribio: ", cadena)
 


"""
2- pedir al usuario que ingrese nombre de un país, y validar si esta escrito en mayúscula toda la palabra 
e imprimir un mensaje que diga esta escrito en mayúscula o minúscula toda la palabra e imprimir un mensaje 
que diga esta escrito en minuscula

"""

def mayusT1():
    pais = input("Ingrese nombre de un país: ")

    #MAYUSCULA
    if pais.isupper() == True:
        print("Usted escribio en MAYUSCULAS")
    #Adicional
    #elif pais[0].isupper() == True:
    #print("Usted escribio en la primera letra de la palabra en mayuscula ") 
    else:
        print("Usted escribio en minusculas")