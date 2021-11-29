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
        "stock_actual": stock_actual,
        "existe": True,
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
    lista_de_palabras = sorted(
        lista_de_palabras, key=lambda x: x['palabra'].lower())
    print(lista_de_palabras)

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

#Busqueda binaria por posicion
def busqueda_binaria(arr, menor, mayor, serial, lista_de_historietas):
    if mayor >= menor:
        # El doble slash "//" divide y rendondea hacia abajo
        mid = (mayor + menor) // 2
        if arr[mid]["serial"] == serial:
            return arr[mid]["posicion"]

        elif arr[mid]["serial"] > serial:
            return busqueda_binaria(arr, menor, mid - 1, serial, lista_de_historietas)

        else:
            return busqueda_binaria(arr, mid + 1, mayor, serial, lista_de_historietas)
    else:
        return -1


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
            lista_primera_palabra = (busqueda_binaria_palabras(lista_de_palabras, 0, len(lista_de_palabras)-1, palabras[i]))
        if i == 1:
            lista_segunda_palabra = (busqueda_binaria_palabras(
                lista_de_palabras, 0, len(lista_de_palabras)-1, palabras[i]))
    

    try:
    # Muestra las posiciones de todas las coincidencias de la primera palabra
        for i in range(len(lista_primera_palabra)):
            if lista_de_historietas[lista_de_palabras[lista_primera_palabra[i]]["posicion"]]["existe"]==True:
                muestra_posiciones_1.append(
                    lista_de_palabras[lista_primera_palabra[i]]["posicion"])
    
    #Muestra las posiciones de todas las coincidencias de la segunda palabra
        for i in range(len(lista_segunda_palabra)):
            if lista_de_historietas[lista_de_palabras[lista_segunda_palabra[i]]["posicion"]]["existe"] == True:
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
                return(muestra_posiciones_1[opcion_usuario])
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
            if len(list3)==0:
                print("No existen Historietas por ese nombre")
                return Intercepcion_listas()
            print("""
            Las opciones disponibles son: 
                """)
            for i in range(len(list3)):
                print(i+1,"-",lista_de_historietas[list3[i]]["titulo"])
            opcion_usuario = input("Escoja el indice del Comic que quiere: ")
            try:
                opcion_usuario = int(opcion_usuario)-1
                print("\n")
                return(list3[opcion_usuario])

            except:
                print("No se encontro el numero escogido.")
                return Intercepcion_listas()
            
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
            return Intercepcion_listas()
        elif opcion==2:
            return inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        else:
            print("Gracias por ingresar al sistema. Hasta luego")
            return
def busqueda_serial():
    serial = input("Ingrese el serial que desea buscar: ")
    try:
        serial_evaluacion = int(serial)
    except:
        print("Ingrese un Numero.")
        busqueda_serial()
    
    serial_encontrado = busqueda_binaria(lista_de_seriales,0,len(lista_de_seriales)-1,serial,lista_de_historietas)
    if lista_de_historietas[serial_encontrado]["existe"] == False:
        print("Serial no encontrado, por favor verifique e intente de nuevo")
        return busqueda_serial()
    if serial_encontrado==-1:
        print("Serial no encontrado, por favor verifique e intente de nuevo")
        busqueda_serial()
    else:
        return serial_encontrado

def busqueda_historieta():
    
    opcion=input("""
    Indique como quiere buscar la historieta:
    1-Por Serial
    2-Por Palabras 
    """)
    try:
        opcion=int(opcion)
        if opcion==1:
            return busqueda_serial()
        elif opcion==2:
            return Intercepcion_listas()
    except:
        print("Ingrese un Numero.")
        return busqueda_historieta()

#Funcion que compra que tiene como parametro la lista encontrada en la funcion Intercepcion_listas
def compra(lista_de_historietas):
    
    #Contiene informacion de la historieta que se quiere comprar
    a_comprar_indice = busqueda_historieta()
    a_comprar_original = str(lista_de_historietas[a_comprar_indice])
    a_comprar = str(a_comprar_original).replace("{","").replace("}","").split(",")
        
    #Contiene el serial de la historieta como un str
    serial = (a_comprar[0]).replace("'serial': ","").replace(" ", "").replace("'","")
    
    #Contiene el Titulo de la historieta como un str
    titulo = (a_comprar[1]).replace(" 'titulo': ","").replace("'","")
        
    #Contiene el precio de venta como un str
    precio_de_venta = (a_comprar[2]).replace("'precio_de_venta': ","").replace(" ", "").replace("'","")
    
    #Contiene el stock_disponible como un str, stock_disponible_entero como un int
    stock_disponible = (a_comprar[3]).replace("'stock_actual': ","").replace(" ","")
    stock_disponible_entero = int(stock_disponible)
        
    print("Disponible: " + stock_disponible + " Stocks " + "En la historieta con el titulo de: " + titulo)          
    if stock_disponible_entero > 0:
        while True:    
            try:
                stock_solicitados = int(input("""
                                            
                Por favor, ingrese el numero de Stocks que desea comprar: 
                > """))
                if stock_solicitados > 0:
                    if stock_solicitados <= stock_disponible_entero:                       
                        break
                    elif stock_solicitados >= stock_disponible_entero:
                        print("No puedes comprar mas stocks de los que hay disponibles")
                elif stock_solicitados == 0:
                    print("No se efectuara compra de stocks")
                    return
            except:
                print("""
                    
                    Dato invalido, solo se aceptan enteros                  
                    
                    """)  
        
        
        sin_cambiar = {
            "serial": serial,
            "titulo": titulo,
            "precio_de_venta": int(precio_de_venta),
            "stock_actual": stock_disponible_entero            
        }
        
        cambio_hecho = {
            "serial": serial,
            "titulo": titulo,
            "precio_de_venta": int(precio_de_venta),
            "stock_actual": stock_disponible_entero - stock_solicitados           
        }
        lista_de_historietas[a_comprar_indice]["stock_actual"] = stock_disponible_entero - stock_solicitados
        actualizar_lista_de_historieta(lista_de_historietas)
        print("Compra exitosa")
        # for i in range(len(lista_de_historietas)):
        #     if str(sin_cambiar) == str(lista_de_historietas[i]):
        #         lista_de_historietas[i] = cambio_hecho
        #         actualizar_lista_de_historieta(lista_de_historietas)      
        #         print("Compra exitosa") 
        #         print(cambio_hecho)
        
        return    
    
    return
def modificar_stock():
    historieta_selecionada= busqueda_historieta()
    
    stock_usuario=input("""Ingrese cuantas historietas quiere colocar: """)
    try:
        stock_usuario=int(stock_usuario)
    except:
        print("Debe ingresar un numero entero.")
    suma_stock = lista_de_historietas[historieta_selecionada]["stock_actual"] + stock_usuario
    if suma_stock>99:
        print("No puedes tener mas de 99 historietas en el Stock.")
        modificar_stock()
    
    lista_de_historietas[historieta_selecionada]["stock_actual"] = suma_stock
    actualizar_lista_de_historieta(lista_de_historietas)
    
def borrador_logico():
    historieta_seleccionada=busqueda_historieta()
    opcion=input(f"""
    Seguro que quiere borrar la historieta '{lista_de_historietas[historieta_seleccionada]["titulo"]}':
        1- Si
        2- No 
    """)
    try:
        opcion=int(opcion)
        if opcion==1:
            lista_de_historietas[historieta_seleccionada]["existe"]=False
            actualizar_lista_de_historieta(lista_de_historietas)
            print("Elemento borrado")
        if opcion==2:
            return inicio(lista_de_historietas,lista_de_seriales,lista_de_palabras)
    except:
        print("Porfavor ingrese un numero valido")
        return borrador_logico()
        

# Funcion que muestra las opciones de la aplicación.
def inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras):
    # Mensaje de bienvenida con las posibles opciones.
    print("""
    Opciones de la aplicación:

    1. Crear una nueva historieta.
    2. Busqueda de Historietas.
    3. Comprar Historieta.
    4. Modificar Stock.
    5. Borrar Historieta.
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
            print(lista_de_historietas[busqueda_historieta()])
            inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        elif(opcion==3):
            compra(lista_de_historietas)
            inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        elif(opcion==4):
            modificar_stock()
            inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        elif(opcion==5):
            borrador_logico()
            inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)
        elif(opcion==6):
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
    # print(lista_de_palabras)
    lista_de_palabras = sorted(
        lista_de_palabras, key=lambda x: x['palabra'].lower())
    # quick_sort(lista_de_palabras, 0, len(lista_de_palabras) - 1, "palabra")
    quick_sort(lista_de_seriales, 0, len(lista_de_seriales) - 1, "serial")

# Mensaje de Bienvenida
print("Bienvenido a nuestra tienda de historietas ARG.")
inicio(lista_de_historietas, lista_de_seriales, lista_de_palabras)

lista_de_historietas = descargar_lista_de_historietas()


