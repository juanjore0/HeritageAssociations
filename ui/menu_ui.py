from .factura_ui import crear_factura, mostrar_factura, mostrar_historial_facturas_cliente
from .cliente_ui import mostrar_cliente  # Solo necesitamos mostrar el cliente
from .control_plagas_ui import mostrar_control_plagas
from .fertilizante_ui import mostrar_fertilizante
from .antibiotico_ui import mostrar_antibiotico

clientes = {}  # Diccionario para almacenar clientes (simulación)

def mostrar_menu_principal():
    print("--- Gestión Agrícola ---")

    while True:
        print("\nSeleccione una acción:")
        print("1. Crear Factura")
        print("2. Mostrar Factura de un Cliente")
        print("3. Mostrar Historial de Facturas de un Cliente")
        print("4. Mostrar Información de un Cliente")
        print("5. Salir")

        opcion = input("Ingrese el número de la acción: ")

        if opcion == '1':
            factura = crear_factura()
            if factura and factura.cliente.cedula not in clientes:
                clientes[factura.cliente.cedula] = factura.cliente
            elif factura:
                clientes[factura.cliente.cedula].agregar_factura(factura)
            if factura:
                mostrar_factura(factura)
        elif opcion == '2':
            cedula_buscar = input("Ingrese la cédula del cliente para mostrar su factura: ")
            if cedula_buscar in clientes and clientes[cedula_buscar].historial_facturas:
                
                mostrar_factura(clientes[cedula_buscar].historial_facturas[-1])
            else:
                print("Cliente no encontrado o no tiene facturas.")
        elif opcion == '3':
            cedula_historial = input("Ingrese la cédula del cliente para ver el historial de facturas: ")
            if cedula_historial in clientes:
                mostrar_historial_facturas_cliente(clientes[cedula_historial])
            else:
                print("Cliente no encontrado.")
        elif opcion == '4':
            cedula_mostrar = input("Ingrese la cédula del cliente a mostrar: ")
            if cedula_mostrar in clientes:
                mostrar_cliente(clientes[cedula_mostrar])
            else:
                print("Cliente no encontrado.")
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu_principal()
