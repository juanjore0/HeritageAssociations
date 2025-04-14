from datetime import date
from .cliente import Cliente

class Factura:
    def __init__(self, cliente: Cliente, fecha: date):
        self.cliente = cliente
        self.fecha = fecha
        self.items = []  # Lista para almacenar los productos con su precio

    def agregar_item(self, producto_nombre: str, precio: float):
        self.items.append({"nombre": producto_nombre, "precio": precio})

    def calcular_total(self):
        return sum(item["precio"] for item in self.items)

    def __str__(self):
        items_str = "\n  - ".join([f"{item['nombre']}: ${item['precio']:.2f}" for item in self.items])
        return f"Factura para {self.cliente.nombre} ({self.cliente.cedula})\nFecha: {self.fecha}\nProductos:\n  - {items_str}\nTotal: ${self.calcular_total():.2f}"