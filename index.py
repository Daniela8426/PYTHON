from EJERCICIOS.MENU.main import *
from EJERCICIOS.TAREAS.clase_two import *
from EJERCICIOS.TAREAS.clase_one import *


def salir():
    print("Usted ha salido.")

opciones = {
    #Nombre de las funciones a ejecutar
	1: buscaVocalT1,
	2: mayusT1,
	3: mayorEdadT2,
	4: dividirT2,
	5: parImparT2,
	6: validarPassT2,
	7: caracterT2,
    8: menuT3,
    9: salir
}


menu = int(input("-------------\nMenú: \nSeleccione el ejercicio que desee ejecutar:\n1. Remplaza letras.\n2. MAYUSCULAS y minusculas.\n3. Valida tu edad.\n4. División de números.\n5. Par o Impar.\n6. Validación de contraseña. \n7. Buscar la vocal. \n8. Menú de navegación. \n9. salir. \n"))


opciones.get(menu, "no digito ninguna opción")()
