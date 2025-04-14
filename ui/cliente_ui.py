from model.cliente import Cliente
from ui.compra_ui import crear_compra, mostrar_compra

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    cedula = input("Ingrese la cédula del cliente: ")
    return Cliente(nombre, cedula)

def mostrar_cliente(cliente: Cliente):
    print("\n--- Datos del Cliente ---")
    print(f"Nombre: {cliente.nombre}")
    print(f"Cédula: {cliente.cedula}")
    if cliente.historial_compras:
        cliente.mostrar_historial_compras()

def agregar_compra_cliente(cliente: Cliente):
    print(f"\n--- Agregar Compra a {cliente.nombre} ---")
    compra = crear_compra()
    if compra:
        cliente.agregar_compra(compra)
        print("Compra agregada al historial del cliente.")

def mostrar_historial_cliente(cliente: Cliente):
    cliente.mostrar_historial_compras()

if __name__ == "__main__":
    nuevo_cliente = crear_cliente()
    mostrar_cliente(nuevo_cliente)

    agregar_compra_cliente(nuevo_cliente)
    mostrar_cliente(nuevo_cliente)

    agregar_compra_cliente(nuevo_cliente)
    mostrar_historial_cliente(nuevo_cliente)