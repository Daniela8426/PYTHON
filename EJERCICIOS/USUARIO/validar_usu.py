def validar(user):
    cant = len(user)
    cara = user.isalnum()

    if cant < 6:
        print("El usuario no puede tener menos de 6 caracteres")
    
    elif cant > 12:
        print("El usuario no puede tener mas de 12 caracteres")

    if cara == False:
        print("El usuario contiene caracteres no validos")
    
    if cant >= 6 and cant <= 12 and cara == True:
        return True
