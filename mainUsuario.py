from autenticacion import Autenticacion

def mostrar_menu():
    print("\n--- MENÚ DE AUTENTICACIÓN ---")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Verificar si usuario está registrado")
    print("4. Salir")

def main():
    autentificacion = Autenticacion()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            usuario = input("Ingrese el nombre de usuario: ")
            contrasena = input("Ingrese la contraseña: ")
            print(sistema.registrar_usuario(usuario, contrasena))

        elif opcion == "2":
            usuario = input("Ingrese el nombre de usuario: ")
            contrasena = input("Ingrese la contraseña: ")
            print(sistema.login(usuario, contrasena))

        elif opcion == "3":
            usuario = input("Ingrese el nombre de usuario: ")
            print(sistema.usuario_registrado(usuario))

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
