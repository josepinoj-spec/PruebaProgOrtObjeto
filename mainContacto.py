from Agenda import agenda

def mostrar_menu():
    print("\n--- MENÚ DE AGENDA ---")
    print("1. Agregar contacto")
    print("2. Mostrar contacto")
    print("3. Buscar contacto")
    print("4. Buscar por coincidencia")
    print("5. Eliminar contacto")
    print("6. Salir")

def main():
    agenda = Agenda()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agenda.agregar_contacto(nombre, telefono, email)

        elif opcion == "2":
            agenda.mostrar_contacto()

        elif opcion == "3":
            dato = input("Ingresa nombre o email a buscar: ")
            agenda.buscar_contacto(dato)

        elif opcion == "4":
            texto = input("Texto para búsqueda parcial: ")
            agenda.buscar_por_lista(texto)

        elif opcion == "5":
            nombre = input("Nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()