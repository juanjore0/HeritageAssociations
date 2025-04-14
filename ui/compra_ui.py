from datetime import date
from model.compra import Compra

def crear_compra():
    productos = {}
    print("\n--- Nueva Compra ---")
    while True:
        nombre_producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if nombre_producto.lower() == 'fin':
            break
        try:
            precio_str = input(f"Ingrese el precio de {nombre_producto}: ")
            precio = float(precio_str.replace(',', '.'))
            productos[nombre_producto] = precio
        except ValueError:
            print("Precio inválido. Intente nuevamente.")
    fecha_compra = date.today()
    return Compra(fecha_compra, productos)

def mostrar_compra(compra: Compra):
    print("\n--- Detalles de la Compra ---")
    print(f"Fecha: {compra.fecha}")
    for nombre, precio in compra.productos.items():
        print(f"- {nombre}: ${precio:.2f}")
    print(f"Total de la Compra: ${compra.calcular_total():.2f}")