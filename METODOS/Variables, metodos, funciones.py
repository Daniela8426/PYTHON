"""
CLASE 11/06/2021
 #TIPOS DE VARIABLES 
a = "Daniela"
b = 19
c = True 


#METODOS
mayus = a.upper() # Convertir todo en mayusculas
minus = a.lower() # Convertir todo en  minusculas
print (mayus, minus)

busca = a.rfind("") # Buscador - devuelve indice del carecter a buscar
print (busca)

#Funciones
print(type(a)) # Conocer el tipo de dato de la variable

frase = "David nunca se acuesta temprano"
corregir 


palabra = "abcdefghijklmnopq"
print (" ".join(palabra)) #agrega espacio en cada uno de los caracteres de la cadena de texto


# Entradas de datos
entry = input("Ingrese su nombre: ") #Entrada para dato Str
entry_two = int(input("Digite su edad: ")) #Entrada para dato Númerico


# validar correo
correo = input("Ingrese su correo: ")
busca_one = correo.rfind("@") 
busca_two = correo.rfind(".") 


if busca_one and busca_two != -1:
    print("Correo Valido")
else:
    print("Correo Invalido")
 

#Cambio de correo

correo = input("Ingrese su correo: ")
buscar_gmail = correo.rfind("gmail")
buscar_hotmail = correo.rfind("hotmail")

if buscar_gmail != -1:
    print("Correo Aceptado")
    
elif buscar_hotmail != -1:
    print("Cambio a gmail")
    cambio = correo.replace("hotmail", "gmail")
    print(cambio)
    
else:
    print("Correo no existe")
    


# Edad con candiciones
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    suma = edad + 10
    print("Su edad es: ", edad, "Su edad final es: ", suma)
    print(f"Su edad es: {edad} Su edad final es: {suma}")
else:
    resta = edad - 10
    print("Su edad es: ", edad, "Su edad final es: ", resta)
    print("Su edad es: " + str(edad)  + "Su edad final es: " + str(suma))

"""

# Edad 2
# Solicitar la edad y nombre de una persona. si es mayor a 20 solicitar su profesion e imprimir nombre, edad  
# Menor a 20 solicitar su profesion y validar si es ingeneria, si es verdadero imprimir "Excelente carrera" sino "siga adelante"


age = int(input("Ingrese su edad: "))
name = str(input("Ingrese su nombre: "))

if age > 20:
    profesion = str(input("Ingrese su profesión: "))
    print (f"Nombre: {name} \n Edad: {age} \n Profesión: {profesion} ")
else:
    profesion = str(input("Ingrese lo que se encuentre estudiando: "))
    validar = profesion.rfind("software")
    if validar != -1:
        print ("Excelente carrera")
    else:
        print ("Animo, Siga adelante")