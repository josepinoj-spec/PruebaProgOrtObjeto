from biblioteca import Biblioteca

def mostrar_menu():
    print("\n--- MENÚ DE BIBLIOTECA ---")
    print("1. Registrar libro")
    print("2. Mostrar catálogo")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Estado de un libro")
    print("6. Salir")

def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            copias = int(input("Número de copias: "))
            biblioteca.registrar_libro(titulo, autor, copias)

        elif opcion == "2":
            biblioteca.mostrar_catalogo()

        elif opcion == "3":
            titulo = input("Título del libro a prestar: ")
            biblioteca.prestar_libro(titulo)

        elif opcion == "4":
            titulo = input("Título del libro a devolver: ")
            biblioteca.devolver_libro(titulo)

        elif opcion == "5":
            titulo = input("Título del libro: ")
            biblioteca.estado_libro(titulo)

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()