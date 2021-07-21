from validar_usu import validar

good = False

while good == False:

    user = input("Ingrese nombre de usuario: ")

    if validar(user) == True:
        print("usuario fue creado con exito")
        good = True