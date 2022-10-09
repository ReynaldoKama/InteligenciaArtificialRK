def menu_principal():
    biografia()
    diccionario = {1: "Volver a imprimir biografía", 0: "Salir"}
    mostrar_menu(diccionario)
    operaciones(diccionario)


def mostrar_menu(diccionario):
    print("Seleccione una opción: ")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor} ")

def biografia():
    print("\nBIOGRAFIA:")
    print("\t'hola' mi nombre es Reynaldo Kama Copa, Nací en Yamparaez-Chuquisaca un 19 de junio de 1998, mi niñez lo viví asistiendo\n \ta una escuela de una de las comunidades de esta provincia, para posteirormente pasar al colegio doroteo Hernandez en Yotala.")
    print("\tSaliendo de colegio me dediqué a trabajar de electricista en instalaciones domiciliarias para así costearme los estudios,\n \tactualmente soy estudiante de la carrera de Ing. en Ciencias de la Computación e Ing. Civil cursando el quinto semestre en \n \tlas dos carreras\n")
    print("\tNombre completo: Reynaldo Kama Copa")
    print("\tEdad: 24 años")
    print("\tDedicación: estudio y trabajo\n")


def operaciones(diccionario):
    while True:
        while (a := int(input("Opción: "))) not in diccionario:
            print("Opción no existente\n Seleccione opción:")
        if a == 1:
            biografia()
        else:
            print("\n\tGracias por visitar mi biografía...")
            break
        mostrar_menu(diccionario)

if __name__ == '__main__':
    menu_principal()