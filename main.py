def inicio():
    # Mensaje de bienvenida con las posibles opciones.
    print("""
    Bienvenido a nuestra tienda de historietas ARG.

    Opciones adentro de la aplicación:

    1. Crear una nueva historieta.
    2. Buscar una historieta por serial.
    3. Buscar una historieta por palabras (Máximo una o dos palabras) del titulo.
    """)

    # Input para que el usuario ingrese la opción escogida.
    opcion = input("Ingrese el número de la opción que desea escoger: ")

    try:
        opcion = int(opcion)
    except:
        print(f"La opción ({opcion}) que ingresó no es un número.")


    print(opcion)