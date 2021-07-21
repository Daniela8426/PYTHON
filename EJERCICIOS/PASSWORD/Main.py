from validar_passw import validar_password

good = False

while good == False:

    clave = input("Ingrese la contraseña: ")

    if validar_password(clave) == True:
        print("Contraseña segura")
        good = True