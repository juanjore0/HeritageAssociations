from enum import Enum

class TipoAnimal(Enum):
    BOVINO = "bovino"
    CAPRINO = "caprino"
    PORCINO = "porcino"

class Antibiotico:
    def __init__(self, dosis: int, tipo_animal: TipoAnimal):
        self.dosis = dosis
        self.tipo_animal = tipo_animal

    def __str__(self):
        return f"Antibiótico - Dosis: {self.dosis}, Tipo Animal: {self.tipo_animal.value}"