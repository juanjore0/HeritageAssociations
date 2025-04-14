class ProductoControl:
    def __init__(self, registro_ica: str, frecuencia_aplicacion: str):
        self.registro_ica = registro_ica
        self.frecuencia_aplicacion = frecuencia_aplicacion

    def __str__(self):
        return f"Producto Control - Registro ICA: {self.registro_ica}, Frecuencia Aplicación: {self.frecuencia_aplicacion}"