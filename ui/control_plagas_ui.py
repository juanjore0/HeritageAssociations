from model.control_plagas import ControlPlagas
from .producto_control_ui import crear_producto_control

def crear_control_plagas_para_factura():
    print("\n--- Crear Control de Plagas para Factura ---")
    base = crear_producto_control()
    periodo_carencia = input("Ingrese el periodo de carencia: ")
    return ControlPlagas(base.registro_ica, base.frecuencia_aplicacion, periodo_carencia)

def mostrar_control_plagas(control: ControlPlagas):
    print("\n--- Datos del Control de Plagas ---")
    print(f"Registro ICA: {control.registro_ica}")
    print(f"Frecuencia de Aplicación (dias): {control.frecuencia_aplicacion}")
    print(f"Periodo de Carencia: {control.periodo_carencia}")

if __name__ == "__main__":
    nuevo_control = crear_control_plagas_para_factura()
    print(nuevo_control)