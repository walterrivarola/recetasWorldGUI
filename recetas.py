import os
from os import system
from pathlib import Path

nombre = input("Ingrese tu nombre: ")
print(f"Bievenido {nombre} a RecetasWorld")

cantidad = 0

for txt in Path("Recetas").glob("**/*.txt"):
    cantidad +=1

print(f"Las recetas están dividas en diferentes categorías y hay un total de {cantidad} productos.")


def Menu():
    contador = 0
    print("Elegi una de las siguientes opciones utilizando sólo el número")
    print("[1]- Leer receta")
    print("[2]- Crear receta")
    print("[3]- Crear categoría")
    print("[4]- Eliminar receta")
    print("[5]- Salir")



def Elegir(opcion):
    indice = 0
    categoria = 0
    recetas = []
    if opcion == '1':
        system('cls')
        print("Las categorías disponibles son:")
        listaCategorias = []
        for carpetas in os.scandir("Recetas"):
            print(f"[{indice}]- {carpetas.name}")
            indice += 1
            listaCategorias.append(carpetas.name)
        ingresarCategoria = input("\nQue menu quieres ver? ")
        opcionCategoria = int(ingresarCategoria)
        elegido = listaCategorias[opcionCategoria]
        ruta = f'Recetas/{elegido}'
        indiceFichero = 0
        listaRecetas = []
        system('cls')
        with os.scandir(ruta) as ficheros:
            for fichero in ficheros:
                print(f"[{indiceFichero}]- {fichero.name}")
                listaRecetas.append(fichero.name)
                indiceFichero +=1
        ingresarReceta = input("Cual recetas quieres abrir? ")
        opcionReceta = int(ingresarReceta)
        #print(listaRecetas[opcionReceta])
        rutaFichero = Path(f'Recetas/{elegido}/{listaRecetas[opcionReceta]}')
        system('cls')
        print(rutaFichero.read_text())

    elif opcion == '2':
        system('cls')
        for carpetas in os.scandir("Recetas"):
            indice += 1
            print(f"[{indice}]- {carpetas.name}")
            recetas.append(carpetas.name)

        categoria = input("Elegi primeramente la categoría utilizando el nombre: ").capitalize()

        for cate in recetas:
            if cate == categoria:
                nombreReceta = input("Ingrese nombre de la receta: ").capitalize()
                recetaNueva = open(f'Recetas/{categoria}/{nombreReceta}.txt', 'w+')
                textoReceta = input("Ingrese el texto de la nueva receta: ")
                recetaNueva.write(textoReceta)
                print("Felicidades creaste una nueva receta")
        else:
            print("Primero debes crear una categoría")
    elif opcion == '3':
        system('cls')
        nuevaCategoria = input("Ingrese la nueva categoria: ")
        while os.path.exists(f'Recetas/{nuevaCategoria}'):
            print("La categoria existe")
            nuevaCategoria = input("Ingrese la nueva categoria: ").capitalize()
        os.makedirs(f'Recetas/{nuevaCategoria}')
    elif opcion == '4':
        system('cls')
        nombreReceta = []
        enumeracionReceta = 0
        for txt in Path("Recetas").glob("**/*.txt"):
            nombreReceta.append(txt)
            print(f"[{enumeracionReceta}]- {txt.stem}")
            enumeracionReceta += 1
        eliminarReceta = input("Ingrese el número de la receta a eliminar: ")
        indiceReceta = 0
        while len(nombreReceta) > indiceReceta:
            if indiceReceta == int(eliminarReceta):
                os.remove(nombreReceta[indiceReceta])
                print("¡Receta eliminada exitosamente!")
                break
            indiceReceta += 1
        else:
            print("Receta no encontrada")


Menu()
opcion = input("Elegir opción: ")
system('cls')
Elegir(opcion)