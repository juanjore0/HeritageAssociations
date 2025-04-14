from model.producto_control import ProductoControl

def crear_producto_control():
    registro_ica = input("Ingrese el registro ICA del producto de control: ")
    frecuencia_aplicacion = input("Ingrese la frecuencia de aplicación: ")
    return ProductoControl(registro_ica, frecuencia_aplicacion)

def mostrar_producto_control(producto: ProductoControl):
    print("\n--- Datos del Producto de Control ---")
    print(f"Registro ICA: {producto.registro_ica}")
    print(f"Frecuencia de Aplicación : {producto.frecuencia_aplicacion}")

if __name__ == "__main__":
    nuevo_producto = crear_producto_control()
    mostrar_producto_control(nuevo_producto)