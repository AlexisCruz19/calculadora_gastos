gastos = []

def agregar_gasto(nombre, cantidad):
    gastos.append((nombre, cantidad))
    print("Gasto agregado.")

def ver_gastos():
    print("\nLista de gastos:")
    for i, (nombre, cantidad) in enumerate(gastos, start=1):
        print(f"{i}. {nombre}: ${cantidad}")

def total_gastado():
    total = sum(cantidad for _, cantidad in gastos)
    print(f"\nTotal gastado: ${total}")

while True:
    print("\n1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Ver total gastado")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del gasto: ")
        try:
            cantidad = float(input("Cantidad: $"))
            agregar_gasto(nombre, cantidad)
        except ValueError:
            print("Cantidad no válida.")
    elif opcion == "2":
        ver_gastos()
    elif opcion == "3":
        total_gastado()
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")
