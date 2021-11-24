import json, os

lista_de_historietas = []

# Descarga la lista que esta en el archivo data.txt
def descargar_lista_de_historietas():
    if(os.path.exists("data.txt")):
        with open('data.txt') as json_file:
            data = json.load(json_file)
            return data

# Carga la lista nueva en el archivo data.txt
def actualizar_lista_de_historieta(lista_nueva):
    with open('data.txt', 'w') as outfile:
        json.dump(lista_nueva, outfile)

def crear_historieta(lista_de_historietas):
    print("Para crear una historieta se requiere que ingresé los valores del serial, título, precio de venta y stock actual.")
    # Chequeando el serial.
    serial = input("""
    Ingrese el valor del Serial
    - Debe contener solo números, no se acepta otro tipo de caracteres.
    - El serial debe tener exactamente 8 dígitos (No más, ni menos).
    --> """)

    if(len(serial) != 8):
        print("El serial debe tener una longitud de 8 dígitos.")
        crear_historieta(lista_de_historietas)
        return False

    try:
        serial = int(serial)
    except:
        print("El valor que ingresó para el serial no es un número. Por favor ingrese un número sin otros caracteres (Letras, caracteres especiales, etc)")
        crear_historieta(lista_de_historietas)
        return False

    # Chequeando el título.
    titulo = input("""
    Ingrese el valor del Título
    - Debe tener un máximo de 40 caracteres (Puede tener menos)
    --> """)

    if(len(titulo) > 40 or len(titulo) < 1):
        print("El título debe tener una longitud máxima de 40 caracteres y mínima de 1 caracter.")
        crear_historieta(lista_de_historietas)
        return False
    
    # Chequeando el precio de venta.
    precio_de_venta = input("""
    Ingrese el Precio de Venta
    - Debe contener solo números, no se acepta otro tipo de caracteres.
    - El Precio de Venta debe tener un máximo de 3 dígitos.
    - El Precio de Venta debe ser mayor de 0.
    --> """)

    if(len(precio_de_venta) > 3 or len(precio_de_venta) < 1):
        print("El precio de venta debe tener una longitud máxima de 3 dígitos.")
        crear_historieta(lista_de_historietas)
        return False

    try:
        precio_de_venta = int(precio_de_venta)
        if(precio_de_venta < 1):
            crear_historieta(lista_de_historietas)
            return False
    except:
        print("El valor que ingresó para el precio de venta no es un número. Por favor ingrese un número sin otros caracteres (Letras, caracteres especiales, etc)")
        crear_historieta(lista_de_historietas)
        return False

    # Chequeando Stock Actual
    stock_actual = input("""
    Ingrese el Stock Actual
    - Debe contener solo números, no se acepta otro tipo de caracteres.
    - El Stock Actual debe tener un máximo de 2 dígitos.
    --> """)

    if(len(stock_actual) > 2 or len(stock_actual) < 1):
        print("El Stock Actual debe tener una longitud máxima de 2 dígitos.")
        crear_historieta(lista_de_historietas)
        return False

    try:
        stock_actual = int(stock_actual)
    except:
        print("El valor que ingresó para el Stock Actual no es un número. Por favor ingrese un número sin otros caracteres (Letras, caracteres especiales, etc)")
        crear_historieta(lista_de_historietas)
        return False
    
    historieta = {
        "serial": serial,
        "titulo": titulo,
        "precio_de_venta": precio_de_venta,
        "stock_actual": stock_actual
    }
    
    lista_de_historietas.append(historieta)
    actualizar_lista_de_historieta(lista_de_historietas)

def inicio(lista_de_historietas):
    # Carga la lista del archivo data.txt
    lista_de_historietas = descargar_lista_de_historietas()

    # Mensaje de bienvenida con las posibles opciones.
    print("""
    Bienvenido a nuestra tienda de historietas ARG.

    Opciones de la aplicación:

    1. Crear una nueva historieta.""")

    # Input para que el usuario ingrese la opción escogida.
    opcion = input("""
    Ingrese el número de la opción que desea escoger:
    --> """)

    try:
        opcion = int(opcion)
        if(opcion == 1):
            crear_historieta(lista_de_historietas)
        else:
            print("El número que ingresó no coincide con ninguna de las opciones disponibles. Por favor intente de nuevo")
            inicio(lista_de_historietas)
    except:
        print(f"La opción ({opcion}) que ingresó no es un número. Debe ingresar el número de la opción que desea escoger.")
        inicio(lista_de_historietas)

inicio(lista_de_historietas)

lista_de_historietas = descargar_lista_de_historietas()

print(lista_de_historietas)