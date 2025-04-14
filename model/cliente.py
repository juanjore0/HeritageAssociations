class Cliente:
    def __init__(self, nombre: str, cedula: str):
        self.nombre = nombre
        self.cedula = cedula
        self.historial_compras = []  # Ya no se usará directamente desde aquí
        self.historial_facturas = [] # Nuevo historial de facturas

    def agregar_factura(self, factura):
        self.historial_facturas.append(factura)

    def mostrar_historial_facturas(self):
        if not self.historial_facturas:
            print(f"{self.nombre} no tiene historial de facturas.")
        else:
            print(f"\n--- Historial de Facturas de {self.nombre} ---")
            for factura in self.historial_facturas:
                print(factura)

    def __str__(self):
        return f"Cliente: {self.nombre} (Cédula: {self.cedula})"