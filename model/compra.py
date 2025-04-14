from datetime import date

class Compra:
    def __init__(self, fecha: date, productos: dict):
        """
        Args:
            fecha (date): Fecha de la compra.
            productos (dict): Diccionario donde la clave es el nombre del producto (str)
                             y el valor es el precio del producto (float).
        """
        self.fecha = fecha
        self.productos = productos

    def calcular_total(self):
        return sum(self.productos.values())

    def __str__(self):
        productos_str = ", ".join([f"{nombre}: ${precio:.2f}" for nombre, precio in self.productos.items()])
        return f"Compra del {self.fecha} - Productos: {productos_str} - Total: ${self.calcular_total():.2f}"