import os

def clear_console():
    """Limpia la consola para una mejor experiencia del usuario."""
    os.system("cls" if os.name == "nt" else "clear")

def convert_length():
    """Convierte entre unidades de longitud."""
    print("\n📏 Conversión de Longitud")
    print("1. Metros a Kilómetros")
    print("2. Kilómetros a Millas")
    print("3. Millas a Metros")

    choice = input("Selecciona una opción (1-3): ").strip()
    try:
        value = float(input("Ingresa el valor a convertir: "))
        if choice == "1":
            print(f"{value} metros = {value / 1000} kilómetros")
        elif choice == "2":
            print(f"{value} kilómetros = {value * 0.621371} millas")
        elif choice == "3":
            print(f"{value} millas = {value * 1609.34} metros")
        else:
            print("⚠️ Opción inválida.")
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")

def convert_weight():
    """Convierte entre unidades de peso."""
    print("\n⚖️ Conversión de Peso")
    print("1. Kilogramos a Libras")
    print("2. Libras a Kilogramos")
    print("3. Gramos a Onzas")

    choice = input("Selecciona una opción (1-3): ").strip()
    try:
        value = float(input("Ingresa el valor a convertir: "))
        if choice == "1":
            print(f"{value} kilogramos = {value * 2.20462} libras")
        elif choice == "2":
            print(f"{value} libras = {value / 2.20462} kilogramos")
        elif choice == "3":
            print(f"{value} gramos = {value * 0.035274} onzas")
        else:
            print("⚠️ Opción inválida.")
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")

def convert_temperature():
    """Convierte entre unidades de temperatura."""
    print("\n🌡️ Conversión de Temperatura")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Celsius a Kelvin")

    choice = input("Selecciona una opción (1-3): ").strip()
    try:
        value = float(input("Ingresa el valor a convertir: "))
        if choice == "1":
            print(f"{value} °C = {(value * 9/5) + 32} °F")
        elif choice == "2":
            print(f"{value} °F = {(value - 32) * 5/9} °C")
        elif choice == "3":
            print(f"{value} °C = {value + 273.15} K")
        else:
            print("⚠️ Opción inválida.")
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")

def main_menu():
    """Menú principal del programa."""
    while True:
        clear_console()
        print("🌍 Convertidor de Unidades")
        print("1. Conversión de Longitud")
        print("2. Conversión de Peso")
        print("3. Conversión de Temperatura")
        print("4. Salir")

        choice = input("\nSelecciona una opción (1-4): ").strip()

        if choice == "1":
            convert_length()
            input("\nPresiona Enter para continuar...")
        elif choice == "2":
            convert_weight()
            input("\nPresiona Enter para continuar...")
        elif choice == "3":
            convert_temperature()
            input("\nPresiona Enter para continuar...")
        elif choice == "4":
            print("👋 ¡Gracias por usar el Convertidor de Unidades!")
            break
        else:
            print("⚠️ Opción inválida. Inténtalo de nuevo.")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main_menu()
