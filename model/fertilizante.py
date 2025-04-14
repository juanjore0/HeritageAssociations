from datetime import date
from .producto_control import ProductoControl  # Importa la clase base

class Fertilizante(ProductoControl):
    def __init__(self, registro_ica: str, frecuencia_aplicacion: str, fecha_ultima_aplicacion: date):
        super().__init__(registro_ica, frecuencia_aplicacion)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion

    def __str__(self):
        return f"Fertilizante - Registro ICA: {self.registro_ica}, Frecuencia Aplicación: {self.frecuencia_aplicacion}, Última Aplicación: {self.fecha_ultima_aplicacion}"