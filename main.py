import json, os

lista_de_historietas = []
lista_de_seriales = []
lista_de_palabras = []

# Descarga la lista que esta en el archivo data.txt
def descargar_lista_de_historietas():
    if(os.path.exists("data.txt") and os.stat("data.txt").st_size != 0):
        with open('data.txt') as json_file:
            data = json.load(json_file)
            return data
    return []

# Carga la lista nueva en el archivo data.txt
def actualizar_lista_de_historieta(lista_nueva):
    with open('data.txt', 'w') as outfile:
        json.dump(lista_nueva, outfile)

# Crea historietas
def crear_historieta(lista_de_historietas, lista_de_seriales, lista_de_palabras):   
    print("Para crear una historieta se requiere que ingresé los valores del serial, título, precio de venta y stock actual.")
    # Chequeando el serial.
    serial = input("""
    Ingrese el valor del Serial
    - Debe contener solo números, no se acepta otro tipo de caracteres.
    - El serial debe tener exactamente 8 dígitos (No más, ni menos).
    --> """)

    if(len(serial) != 8):
        print("El serial debe tener una longitud de 8 dígitos.")
        crear_historieta(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        return False

    try:
        # Esto solo se utiliza para comprobar que sea un número
        serial_falso = int(serial)

        for i in range(len(serial)):
            if serial[i] == ' ':
                print("El valor que ingresó para el serial no puede tener espacios. Por favor ingrese un número sin otros caracteres (Letras, espacios, caracteres especiales, etc)")
                crear_historieta(lista_de_historietas, lista_de_seriales, lista_de_palabras)
                return False
        
        if(len(lista_de_seriales) > 0):
            for j in range(len(lista_de_seriales)):
                if lista_de_seriales[j] == serial:
                    print("El valor que ingresó para el serial ya se encuentra ocupado. Por favor ingrese un número de serial diferente.")
                    crear_historieta(lista_de_historietas, lista_de_seriales, lista_de_palabras)
                    return False        

    except:
        print("El valor que ingresó para el serial no es un número. Por favor ingrese un número sin otros caracteres (Letras, espacios, caracteres especiales, etc)")
        crear_historieta(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        return False

    # Chequeando el título.
    titulo = input("""
    Ingrese el valor del Título
    - Debe tener un máximo de 40 caracteres (Puede tener menos)
    --> """)

    if(len(titulo) > 40 or len(titulo) < 1):
        print("El título debe tener una longitud máxima de 40 caracteres y mínima de 1 caracter.")
        crear_historieta(lista_de_historietas, lista_de_seriales, lista_de_palabras)
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
        crear_historieta(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        return False

    try:
        precio_de_venta = int(precio_de_venta)
        if(precio_de_venta < 1):
            crear_historieta(lista_de_historietas, lista_de_seriales, lista_de_palabras)
            return False
    except:
        print("El valor que ingresó para el precio de venta no es un número. Por favor ingrese un número sin otros caracteres (Letras, caracteres especiales, etc)")
        crear_historieta(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        return False

    # Chequeando Stock Actual
    stock_actual = input("""
    Ingrese el Stock Actual
    - Debe contener solo números, no se acepta otro tipo de caracteres.
    - El Stock Actual debe tener un máximo de 2 dígitos.
    --> """)

    if(len(stock_actual) > 2 or len(stock_actual) < 1):
        print("El Stock Actual debe tener una longitud máxima de 2 dígitos.")
        crear_historieta(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        return False

    try:
        stock_actual = int(stock_actual)
    except:
        print("El valor que ingresó para el Stock Actual no es un número. Por favor ingrese un número sin otros caracteres (Letras, caracteres especiales, etc)")
        crear_historieta(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        return False
    
    historieta = {
        "serial": serial,
        "titulo": titulo,
        "precio_de_venta": precio_de_venta,
        "stock_actual": stock_actual
    }
    
    lista_de_historietas.append(historieta)
    actualizar_lista_de_historieta(lista_de_historietas)

    # Agrega el nuevo elemento a la lista de seriales
    lista_de_seriales.append({"posicion": len(lista_de_historietas)-1, "serial": serial})
    quick_sort(lista_de_seriales, 0, len(lista_de_seriales) - 1, "serial")

    # Agrega el nuevo elemento a la lista de palabras
    lista_titulo = titulo.split(" ")
    for k in range(len(lista_titulo)):
        lista_de_palabras.append({"posicion": len(lista_de_historietas)-1, "palabra": lista_titulo[k]})
    quick_sort(lista_de_palabras, 0, len(lista_de_palabras) - 1, "palabra")

# Divide la lista en partes para poder realizar el ordenamiento con "Quick Sort".
def particion(arr, menor, mayor, elemento): 
	i = (menor - 1)
	pivot = arr[mayor][elemento]
	for j in range(menor, mayor):
		if arr[j][elemento] <= pivot:
			i = i + 1
			arr[i][elemento], arr[j][elemento], arr[i]["posicion"], arr[j]["posicion"] = arr[j][elemento], arr[i][elemento], arr[j]["posicion"], arr[i]["posicion"]

	arr[i+1][elemento], arr[mayor][elemento], arr[i+1]["posicion"], arr[mayor]["posicion"] = arr[mayor][elemento], arr[i + 1][elemento], arr[mayor]["posicion"], arr[i + 1]["posicion"]
	return (i + 1)

# Funcion de ordenamiento con el método "Quick Sort"
def quick_sort(arr, menor, mayor, elemento): 
	if menor < mayor: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = particion(arr, menor, mayor, elemento) 

		# Separately sort elements before 
		# partition and after partition 
		quick_sort(arr, menor, pi-1, elemento) 
		quick_sort(arr, pi+1, mayor, elemento) 

# Función de búsqueda binaria para los Seriales
def busqueda_binaria_serial(arr, menor, mayor, serial, lista_de_historietas):
    if mayor >= menor:
        # El doble slash "//" divide y rendondea hacia abajo 
        mid = (mayor + menor) // 2
        if arr[mid]["serial"] == serial:
            return lista_de_historietas[arr[mid]["posicion"]]
 
        elif arr[mid]["serial"] > serial:
            return busqueda_binaria_serial(arr, menor, mid - 1, serial, lista_de_historietas)

        else:
            return busqueda_binaria_serial(arr, mid + 1, mayor, serial, lista_de_historietas)
    else:
        return -1

# Función de búsqueda binaria para palabras del titulo (No lista)
def busqueda_binaria_palabras(arr, menor, mayor, palabras):
    if mayor >= menor:
        # El doble slash "//" divide y rendondea hacia abajo 
        mid = (mayor + menor) // 2
        if arr[mid] == palabras:
            return mid
 
        elif arr[mid] > palabras:
            return busqueda_binaria_palabras(arr, menor, mid - 1, palabras)

        else:
            return busqueda_binaria_palabras(arr, mid + 1, mayor, palabras)
    else:
        return -1

# Funcion que muestra las opciones de la aplicación.
def inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras):
    # Mensaje de bienvenida con las posibles opciones.
    print("""
    Opciones de la aplicación:

    1. Crear una nueva historieta.
    2. Salir.""")

    # Input para que el usuario ingrese la opción escogida.
    opcion = input("""
    Ingrese el número de la opción que desea escoger:
    --> """)

    try:
        opcion = int(opcion)
        if(opcion == 1):
            crear_historieta(lista_de_historietas, lista_de_seriales, lista_de_palabras)
            inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        elif(opcion == 2):
            return
        else:
            print("El número que ingresó no coincide con ninguna de las opciones disponibles. Por favor intente de nuevo")
            inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)
    except:
        print(f"La opción ({opcion}) que ingresó no es un número. Debe ingresar el número de la opción que desea escoger.")
        inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)

# Carga la lista del archivo data.txt
lista_de_historietas = descargar_lista_de_historietas()
if(len(lista_de_historietas) > 0):
    for i in range(len(lista_de_historietas)):
        lista_de_seriales.append({"posicion": i, "serial": lista_de_historietas[i]["serial"]})
        lista_titulo = lista_de_historietas[i]["titulo"].split(" ")
        for k in range(len(lista_titulo)):
            lista_de_palabras.append({"posicion": i, "palabra": lista_titulo[k]})
    quick_sort(lista_de_palabras, 0, len(lista_de_palabras) - 1, "palabra")
    quick_sort(lista_de_seriales, 0, len(lista_de_seriales) - 1, "serial")

# Mensaje de Bienvenida
print("Bienvenido a nuestra tienda de historietas ARG.")

inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)

lista_de_historietas = descargar_lista_de_historietas()

print(busqueda_binaria_serial(lista_de_seriales, 0, len(lista_de_seriales)-1, "11111115", lista_de_historietas))