from .producto_control import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, registro_ica: str, frecuencia_aplicacion: str, periodo_carencia: str):
        super().__init__(registro_ica, frecuencia_aplicacion)
        self.periodo_carencia = periodo_carencia

    def __str__(self):
        return f"Control de Plagas - Registro ICA: {self.registro_ica}, Frecuencia Aplicación: {self.frecuencia_aplicacion}, Periodo Carencia: {self.periodo_carencia}"