from catalogo import Catalogo

def mostrar_menu():
    print("\n--- MENÚ DE CATÁLOGO DE PELÍCULAS ---")
    print("1. Agregar película")
    print("2. Mostrar catálogo")
    print("3. Buscar por título")
    print("4. Filtrar por género")
    print("5. Salir")

def main():
    catalogo = Catalogo()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título de la película: ")
            genero = input("Género: ")
            año = input("Año de lanzamiento: ")
            catalogo.agregar_pelicula(titulo, genero, año)

        elif opcion == "2":
            catalogo.mostrar_catalogo()

        elif opcion == "3":
            titulo = input("Título a buscar: ")
            catalogo.buscar_por_titulo(titulo)

        elif opcion == "4":
            genero = input("Género a filtrar: ")
            catalogo.filtrar_por_genero(genero)

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()