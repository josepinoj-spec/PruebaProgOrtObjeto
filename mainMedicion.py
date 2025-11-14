from sensor import Sensor

def mostrar_menu():
    print("\n--- MENÚ DE SENSOR ---")
    print("1. Agregar medición")
    print("2. Mostrar promedio")
    print("3. Mostrar máximo")
    print("4. Mostrar mínimo")
    print("5. Salir")

def main():
    nombre_sensor = input("Ingrese el nombre del sensor: ")
    sensor = Sensor(nombre_sensor)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            valor = float(input("Ingrese el valor de la medición: "))
            sensor.agregar_medicion(valor)

        elif opcion == "2":
            promedio = sensor.obtener_promedio()
            if promedio is not None:
                print(f"Promedio de mediciones: {promedio:.2f}")

        elif opcion == "3":
            maximo = sensor.obtener_maximo()
            if maximo is not None:
                print(f"Valor máximo: {maximo}")

        elif opcion == "4":
            minimo = sensor.obtener_minimo()
            if minimo is not None:
                print(f"Valor mínimo: {minimo}")

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
