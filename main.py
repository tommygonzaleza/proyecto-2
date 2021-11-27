import json
import os

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
        crear_historieta(lista_de_historietas,
                         lista_de_seriales, lista_de_palabras)
        return False

    try:
        # Esto solo se utiliza para comprobar que sea un número
        serial_falso = int(serial)

        for i in range(len(serial)):
            if serial[i] == ' ':
                print("El valor que ingresó para el serial no puede tener espacios. Por favor ingrese un número sin otros caracteres (Letras, espacios, caracteres especiales, etc)")
                crear_historieta(lista_de_historietas,
                                 lista_de_seriales, lista_de_palabras)
                return False

        if(len(lista_de_seriales) > 0):
            for j in range(len(lista_de_seriales)):
                if lista_de_seriales[j] == serial:
                    print(
                        "El valor que ingresó para el serial ya se encuentra ocupado. Por favor ingrese un número de serial diferente.")
                    crear_historieta(lista_de_historietas,
                                     lista_de_seriales, lista_de_palabras)
                    return False

    except:
        print("El valor que ingresó para el serial no es un número. Por favor ingrese un número sin otros caracteres (Letras, espacios, caracteres especiales, etc)")
        crear_historieta(lista_de_historietas,
                         lista_de_seriales, lista_de_palabras)
        return False

    # Chequeando el título.
    titulo = input("""
    Ingrese el valor del Título
    - Debe tener un máximo de 40 caracteres (Puede tener menos)
    --> """)

    if(len(titulo) > 40 or len(titulo) < 1):
        print("El título debe tener una longitud máxima de 40 caracteres y mínima de 1 caracter.")
        crear_historieta(lista_de_historietas,
                         lista_de_seriales, lista_de_palabras)
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
        crear_historieta(lista_de_historietas,
                         lista_de_seriales, lista_de_palabras)
        return False

    try:
        precio_de_venta = int(precio_de_venta)
        if(precio_de_venta < 1):
            crear_historieta(lista_de_historietas,
                             lista_de_seriales, lista_de_palabras)
            return False
    except:
        print("El valor que ingresó para el precio de venta no es un número. Por favor ingrese un número sin otros caracteres (Letras, caracteres especiales, etc)")
        crear_historieta(lista_de_historietas,
                         lista_de_seriales, lista_de_palabras)
        return False

    # Chequeando Stock Actual
    stock_actual = input("""
    Ingrese el Stock Actual
    - Debe contener solo números, no se acepta otro tipo de caracteres.
    - El Stock Actual debe tener un máximo de 2 dígitos.
    --> """)

    if(len(stock_actual) > 2 or len(stock_actual) < 1):
        print("El Stock Actual debe tener una longitud máxima de 2 dígitos.")
        crear_historieta(lista_de_historietas,
                         lista_de_seriales, lista_de_palabras)
        return False

    try:
        stock_actual = int(stock_actual)
    except:
        print("El valor que ingresó para el Stock Actual no es un número. Por favor ingrese un número sin otros caracteres (Letras, caracteres especiales, etc)")
        crear_historieta(lista_de_historietas,
                         lista_de_seriales, lista_de_palabras)
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
    lista_de_seriales.append(
        {"posicion": len(lista_de_historietas)-1, "serial": serial})
    quick_sort(lista_de_seriales, 0, len(lista_de_seriales) - 1, "serial")

    # Agrega el nuevo elemento a la lista de palabras
    lista_titulo = titulo.split(" ")
    for k in range(len(lista_titulo)):
        lista_de_palabras.append(
            {"posicion": len(lista_de_historietas)-1, "palabra": lista_titulo[k]})
    quick_sort(lista_de_palabras, 0, len(lista_de_palabras) - 1, "palabra")

# Divide la lista en partes para poder realizar el ordenamiento con "Quick Sort".
def particion(arr, menor, mayor, elemento):
    i = (menor - 1)
    pivot = arr[mayor][elemento]
    for j in range(menor, mayor):
        if arr[j][elemento] <= pivot:
            i = i + 1
            arr[i][elemento], arr[j][elemento], arr[i]["posicion"], arr[j]["posicion"] = arr[
                j][elemento], arr[i][elemento], arr[j]["posicion"], arr[i]["posicion"]

    arr[i+1][elemento], arr[mayor][elemento], arr[i+1]["posicion"], arr[mayor]["posicion"] = arr[mayor][elemento], arr[i +
                                                                                                                       1][elemento], arr[mayor]["posicion"], arr[i + 1]["posicion"]
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
def bubleSort(num, metodo_ordenamiento):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(num)-1):
            if num[i][metodo_ordenamiento].lower() > num[i+1][metodo_ordenamiento].lower():
                num[i][metodo_ordenamiento], num[i + 1][metodo_ordenamiento] = num[i +
                                                                                   1][metodo_ordenamiento], num[i][metodo_ordenamiento]
                intercambio = True

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
def busqueda_binaria_palabras(arr, menor, mayor, palabra):
    array_palabra = []

    if mayor >= menor:
        # El doble slash "//" divide y rendondea hacia abajo
        mid = (mayor + menor) // 2
        palabra = palabra.lower()
        if arr[mid]["palabra"].lower() == palabra:
            mid1 = mid-1
            try:
                while mid < len(arr) and arr[mid]["palabra"].lower() == palabra:
                    array_palabra.append(mid)
                    mid = mid+1

                while mid1 != -1 and arr[mid1]["palabra"].lower() == palabra:
                    array_palabra.append(mid1)
                    mid1 = mid1-1

                return array_palabra
            except:
                return array_palabra

        elif arr[mid]["palabra"].lower() > palabra:
            return busqueda_binaria_palabras(arr, menor, mid - 1, palabra)

        else:
            return busqueda_binaria_palabras(arr, mid + 1, mayor, palabra)
    else:
        return -1

# Busqueda binaria de palabras interceptando dos listas
def Intercepcion_listas():
    palabras = input("""
    Introduzca el nombre del Comic que quiere buscar.
    Solo puede escribir UNA o DOS Palabras.
     """)
    palabras = palabras.split(" ")
    print(palabras)
    if(len(palabras)>2):
        print("Solo puedes insertar UNA o DOS palabras, por favor intente de nuevo.")
        Intercepcion_listas()
    lista_primera_palabra = []
    lista_segunda_palabra = []
    muestra_posiciones_1 = []
    muestra_posiciones_2 = []
    # Busca las todas las palabras de la lista
    for i in range(len(palabras)):  
        if i == 0:
            
            lista_primera_palabra = (busqueda_binaria_palabras(lista_de_palabras, 0, len(lista_de_palabras), palabras[i]))
        if i == 1:
            lista_segunda_palabra = (busqueda_binaria_palabras(
                lista_de_palabras, 0, len(lista_de_palabras)-1, palabras[i]))
    

    try:
    # Muestra las posiciones de todas las coincidencias de la primera palabra
        for i in range(len(lista_primera_palabra)):
            muestra_posiciones_1.append(
                lista_de_palabras[lista_primera_palabra[i]]["posicion"])
    
    #Muestra las posiciones de todas las coincidencias de la segunda palabra
        for i in range(len(lista_segunda_palabra)):
            muestra_posiciones_2.append(lista_de_palabras[lista_segunda_palabra[i]]["posicion"])
    #Imprime todas las historietas cuando busca por una palabra 
        if len(palabras)==1 and len(muestra_posiciones_1)>0:
            print("""
        Las Opciones disponibles son:
             """)
            for i in range(len(muestra_posiciones_1)):      
                print(i+1,"-",lista_de_historietas[muestra_posiciones_1[i]]["titulo"])
            opcion_usuario= input("Escoja el indice del Comic que quiere: ")
            try:
                opcion_usuario=int(opcion_usuario)-1
                print("\n")
                return(lista_de_historietas[muestra_posiciones_1[opcion_usuario]])
            except:
                print("No se encontro el numero escogido.")
                opcion=input("""
        Quiere volver a intentar?
        1-Volver a intentar.
        2-Volver al Inicio
        3-Salir del sistema 
        """)
                opcion = int(opcion)
                if opcion==1:
                    Intercepcion_listas()
                elif opcion==2:
                    inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)
                else:
                    print("Gracias por ingresar al sistema. Hasta luego")
                return
            

    #Imprime todas las historietas que coincidan con las dos palabras
        else:
        #Convierte los Array en objetos
            set1= set(muestra_posiciones_1)
            set2= set(muestra_posiciones_2)
        #Intercepta los Array
            set3=set1 & set2
        #Convierte el objeto en lista nuevamente
            list3= list(set3)
            print("""
            Las opciones disponibles son: 
                """)
            for i in range(len(list3)):
                print(i+1,"-",lista_de_historietas[list3[i]]["titulo"])
            opcion_usuario = input("Escoja el indice del Comic que quiere: ")
            try:
                opcion_usuario = int(opcion_usuario)-1
                print("\n")
                return(lista_de_historietas[list3[opcion_usuario]])

            except:
                print("No se encontro el numero escogido.")
                Intercepcion_listas()
            
    except:
        cadena= " ".join(palabras)
        print(f"""
        No se encontro ninguno Comic por las palabras '{cadena}' 
        """)
        opcion=input("""
        Quiere volver a intentar?
        1-Volver a intentar.
        2-Volver al Inicio
        3-Salir del sistema 
        """)
        opcion = int(opcion)
        if opcion==1:
            Intercepcion_listas()
        elif opcion==2:
            inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        else:
            print("Gracias por ingresar al sistema. Hasta luego")
            return

# Funcion que muestra las opciones de la aplicación.
def inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras):
    # Mensaje de bienvenida con las posibles opciones.
    print("""
    Opciones de la aplicación:

    1. Crear una nueva historieta.
    2. Busqueda por palabra.
    3. Salir.
    """)

    # Input para que el usuario ingrese la opción escogida.
    opcion = input("""
    Ingrese el número de la opción que desea escoger:
    --> """)

    try:
        opcion = int(opcion)
        if(opcion == 1):
            crear_historieta(lista_de_historietas,
                             lista_de_seriales, lista_de_palabras)
            inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        elif(opcion == 2):
            print(Intercepcion_listas())

        elif(opcion==3):
            return
        else:
            print("El número que ingresó no coincide con ninguna de las opciones disponibles. Por favor intente de nuevo")
            inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)
    except:
        print(
            f"La opción ({opcion}) que ingresó no es un número. Debe ingresar el número de la opción que desea escoger.")
        inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)

# Carga la lista del archivo data.txt
lista_de_historietas = descargar_lista_de_historietas()
if(len(lista_de_historietas) > 0):
    for i in range(len(lista_de_historietas)):
        lista_de_seriales.append(
            {"posicion": i, "serial": lista_de_historietas[i]["serial"]})
        lista_titulo = lista_de_historietas[i]["titulo"].split(" ")
        for k in range(len(lista_titulo)):
            lista_de_palabras.append(
                {"posicion": i, "palabra": lista_titulo[k]})
    print(lista_de_palabras)
    lista_de_palabras = sorted(
        lista_de_palabras, key=lambda x: x['palabra'].lower())
    # quick_sort(lista_de_palabras, 0, len(lista_de_palabras) - 1, "palabra")
    quick_sort(lista_de_seriales, 0, len(lista_de_seriales) - 1, "serial")

# Mensaje de Bienvenida
print("Bienvenido a nuestra tienda de historietas ARG.")

inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)

lista_de_historietas = descargar_lista_de_historietas()