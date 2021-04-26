def validar_password(clave):
    cant = len(clave) #   Longitud de la cadena
    minus = any(letra.islower() for letra in clave) # Buscar si la contraseña contiene letra minúscula
    mayus = any(letra.isupper() for letra in clave)#  Buscar si la contraseña contiene letra mayúscula
    alfa = clave.isalnum() #     Buscar carácter no alfanumérico 
    numer = any(letra.isdigit() for letra in clave) # Buscar si la contraseña contiene un numero
    espa = clave.isspace() #   Buscar si la contraseña contiene algún espacio 

    if minus == False: # Validar si la cadena contiene caracteres en minúscula
        print("La contraseña debe contener caracteres en minúsculas")
    if mayus == False:
        print("La contraseña debe contener caracteres en mayúsculas")
    if alfa == True:
        print("La contraseña debe contener caracteres espaciales")
    if numer == False:
        print("La contraseña debe contener al menos un número")
    if espa == True:
        print("La contraseña No debe contener espacios")
    if cant < 8: 
        print("La contraseña contiene menos de 8 caracteres ")
    
    if minus == True and mayus == True and alfa == False and numer == True and espa == False and cant >= 8:
        return True
    else:
        print("La contraseña no es segura")
     
    


