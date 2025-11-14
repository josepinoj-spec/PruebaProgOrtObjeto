from curso import Curso

def mostrar_menu():
    print("\n--- MENÚ DEL CURSO ---")
    print("1. Inscribir alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumno")
    print("4. Eliminar alumno")
    print("5. Salir")

def main():
    curso = Curso(" Estadisticas ")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del alumno: ")
            apellidos = input("Apellidos del alumno: ")
            curso.inscribir_alumno(nombre, apellidos)

        elif opcion == "2":
            curso.listar_alumnos()

        elif opcion == "3":
            nombre = input("Nombre del alumno a buscar: ")
            apellidos = input("Apellidos del alumno a buscar: ")
            alumno = curso.buscar_alumno(nombre, apellidos)
            if alumno:
                print(f"Alumno encontrado: {alumno.nombre} {alumno.apellidos}")
            else:
                print("Alumno no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del alumno a eliminar: ")
            apellidos = input("Apellidos del alumno a eliminar: ")
            curso.eliminar_alumno(nombre, apellidos)

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()