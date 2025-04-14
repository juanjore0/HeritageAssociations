from datetime import date
from model.fertilizante import Fertilizante
from .producto_control_ui import crear_producto_control

def crear_fertilizante_para_factura():
    print("\n--- Crear Fertilizante para Factura ---")
    base = crear_producto_control()
    try:
        año = int(input("Ingrese el año de la última aplicación: "))
        mes = int(input("Ingrese el mes de la última aplicación: "))
        dia = int(input("Ingrese el día de la última aplicación: "))
        fecha_ultima_aplicacion = date(año, mes, dia)
        return Fertilizante(base.registro_ica, base.frecuencia_aplicacion, fecha_ultima_aplicacion)
    except ValueError:
        print("Error al ingresar la fecha. Se usará la fecha actual.")
        return Fertilizante(base.registro_ica, base.frecuencia_aplicacion, date.today())

def mostrar_fertilizante(fertilizante: Fertilizante):
    print("\n--- Datos del Fertilizante ---")
    print(f"Registro ICA: {fertilizante.registro_ica}")
    print(f"Frecuencia de Aplicación (dias): {fertilizante.frecuencia_aplicacion}")
    print(f"Fecha de Última Aplicación: {fertilizante.fecha_ultima_aplicacion}")

if __name__ == "__main__":
    nuevo_fertilizante = crear_fertilizante_para_factura()
    print(nuevo_fertilizante)