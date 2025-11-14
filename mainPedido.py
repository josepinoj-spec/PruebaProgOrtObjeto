from pedido import Pedido

def mostrar_menu():
    print("\n--- MENÚ DE PEDIDO ---")
    print("1. Agregar ítem")
    print("2. Mostrar ítems")
    print("3. Mostrar detalle del pedido")
    print("4. Salir")

def main():
    pedido = Pedido()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad: "))
            pedido.agregar_item(nombre, precio, cantidad)

        elif opcion == "2":
            pedido.mostrar_items()

        elif opcion == "3":
            pedido.mostrar_detalle()

        elif opcion == "4":
            print("¡Pedido finalizado!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()