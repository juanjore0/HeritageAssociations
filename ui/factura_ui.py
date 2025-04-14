from datetime import date
from model.factura import Factura
from model.cliente import Cliente
from .control_plagas_ui import crear_control_plagas_para_factura
from .fertilizante_ui import crear_fertilizante_para_factura
from .antibiotico_ui import crear_antibiotico_para_factura

def crear_cliente_para_factura():
    nombre = input("Ingrese el nombre del cliente para la factura: ")
    cedula = input("Ingrese la cédula del cliente para la factura: ")
    return Cliente(nombre, cedula)

def crear_factura():
    cliente = crear_cliente_para_factura()
    fecha_factura = date.today()
    factura = Factura(cliente, fecha_factura)

    print("\n--- Agregar productos a la factura ---")
    while True:
        print("\nSeleccione el tipo de producto a agregar:")
        print("1. Control de Plagas")
        print("2. Fertilizante")
        print("3. Antibiótico")
        print("4. Terminar de agregar productos")
        opcion = input("Ingrese el número de la opción: ")

        if opcion == '1':
            producto = crear_control_plagas_para_factura()
            if producto:
                try:
                    precio = float(input(f"Ingrese el precio de {producto}: "))
                    factura.agregar_item(str(producto), precio)
                except ValueError:
                    print("Precio inválido.")
        elif opcion == '2':
            producto = crear_fertilizante_para_factura()
            if producto:
                try:
                    precio = float(input(f"Ingrese el precio de {producto}: "))
                    factura.agregar_item(str(producto), precio)
                except ValueError:
                    print("Precio inválido.")
        elif opcion == '3':
            producto = crear_antibiotico_para_factura()
            if producto:
                try:
                    precio = float(input(f"Ingrese el precio de {producto}: "))
                    factura.agregar_item(str(producto), precio)
                except ValueError:
                    print("Precio inválido.")
        elif opcion == '4':
            break
        else:
            print("Opción inválida.")

    cliente.agregar_factura(factura) # Asociar la factura al cliente
    return factura

def mostrar_factura(factura: Factura):
    print("\n--- Detalles de la Factura ---")
    print(factura)

def mostrar_historial_facturas_cliente(cliente: Cliente):
    cliente.mostrar_historial_facturas()