from model.antibiotico import Antibiotico, TipoAnimal

def crear_antibiotico_para_factura():
    print("\n--- Crear Antibiótico para Factura ---")
    try:
        dosis = int(input("Ingrese la dosis del antibiótico (entre 400Kg y 600Kg): "))
        tipo_animal = None
        while tipo_animal is None:
            print("Seleccione el tipo de animal:")
            print("1. Bovino")
            print("2. Caprino")
            print("3. Porcino")
            opcion = input("Ingrese el número de la opción: ")
            if opcion == '1':
                tipo_animal = TipoAnimal.BOVINO
            elif opcion == '2':
                tipo_animal = TipoAnimal.CAPRINO
            elif opcion == '3':
                tipo_animal = TipoAnimal.PORCINO
            else:
                print("Opción inválida. Por favor, intente nuevamente.")
        return Antibiotico(dosis, tipo_animal)
    except ValueError:
        print("Error al ingresar la dosis. Por favor, ingrese un número válido.")
        return crear_antibiotico_para_factura()

def mostrar_antibiotico(antibiotico: Antibiotico):
    print("\n--- Datos del Antibiótico ---")
    print(f"Dosis: {antibiotico.dosis}")
    print(f"Tipo Animal: {antibiotico.tipo_animal.value}")

if __name__ == "__main__":
    nuevo_antibiotico = crear_antibiotico_para_factura()
    print(nuevo_antibiotico)