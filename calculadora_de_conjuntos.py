import random
import string


def pedir_numero_validado(mensaje):
    """
    Solicita un número al usuario y repite la solicitud si la entrada no es un entero válido.
    """
    while True:
        entrada = input(mensaje)

        try:
            #Intenta convertir la entrada (string) a un número entero (int)
            numero = int(entrada)

            #Si la conversión fue exitosa, salimos del bucle
            return numero

        except ValueError:
            #Si ocurre un ValueError (porque la entrada no es un número),
            #se ejecuta este bloque y el bucle vuelve a empezar.
            print("❌ ¡Error! Por favor, ingresa solo alguno de los números que se solicitan.\n")
            #El bucle While True se repite automáticamente

def pedir_letra_validada(mensaje):
    while True:
        entrada = input(mensaje).strip()  # .strip() quita espacios extra al inicio y final

        #Comprueba si es una letra (isalpha()) Y si solo tiene un carácter (len() == 1)
        if entrada.isalpha() and len(entrada) == 1:
            # Si es una única letra, se sale de la función y devuelve la letra en minúsculas
            return entrada.lower()

        #Si la validación falla, se muestra un error y el bucle vuelve a empezar
        else:
            print("❌ ¡Error! Por favor, ingresa solo s o n.")

def numeros_manuales():
    pregunta1 = pedir_letra_validada("¿Deseas agregar un elemento al conjunto? [s/n]: ")
    conjunto = [] #Inicia el conjunto en vacío

    validacion = True
    while validacion:
        if  pregunta1 == "s" or pregunta1 == "n": #Valida que la entrada sea s o n
            validacion = False
            while pregunta1 == "s":
                elemento1 = pedir_numero_validado("Ingresa el elemento a agregar(1-100): ")
                validacion2 = True
                while validacion2:
                    if 0<=elemento1<=100:
                        validacion2 = False
                        conjunto.append(elemento1)
                    else:
                        print("Valor incorrecto, ingresa un número entre 1 y 100")
                        elemento1 = pedir_numero_validado("Ingrese el elemento a agregar(1-100): ")

                pregunta1 = pedir_letra_validada("¿Deseas agregar un elemento al conjunto? [s/n]: ")
        else:
            print("Opción no válida.")
            pregunta1 = pedir_letra_validada("¿Desea agregar un elemento al conjunto? [s/n]: ")

    conjunto.sort()
    return conjunto

def conjunto_corregido(conjunto):
    conjunto.sort()
    conjunto_correcto = []
    for i in range(len(conjunto)):  # Hace que el conjunto no tenga elementos repetidos
        if conjunto[i] not in conjunto_correcto:
            conjunto_correcto.append(conjunto[i])
        else:
            continue
    return conjunto_correcto

def numeros_aleatorios():
    limite = pedir_numero_validado("¿Cuántos elementos quieres que tenga el conjunto? (0-30) ")
    conjunto = []

    validacion = True
    while validacion:
        if 0 <= limite <= 30:
            validacion = False
            for i in range(limite):
                elemento = random.randint(1,100)
                conjunto.append(elemento)
        else:
            print("Opción no válida. Ingresa un número entre 0 y 30.\n")
            limite = pedir_numero_validado("¿Cuántos elementos quieres que tenga el conjunto? (0-30) ")

    conjunto.sort()
    return conjunto

def pedir_caracter(mensaje):
    """
    Solicita una entrada al usuario y repite la solicitud hasta que ingrese
    solamente un solo carácter (letra o símbolo), excluyendo números.
    """
    while True:
        entrada = input(mensaje).strip()  #Se eliminan espacios

        #Valida que sea exactamente un solo carácter.
        if len(entrada) != 1:
            print("❌ ¡Error! Debes ingresar solamente un caracter (letra o símbolo).")
            continue

        #See sabe que 'entrada' es un único carácter.
        caracter = entrada[0]

        #Revisa si el único carácter es un número.
        if caracter.isdigit():
            print("❌ ¡Error! No puedes ingresar un número. Debe ser una letra o un símbolo.")
        else:
            #Si tiene longitud 1 y no es un dígito, es válido.
            return caracter

def caracteres_manuales():
    pregunta = pedir_letra_validada("¿Deseas agregar un elemento al conjunto? [s/n]: ")
    conjunto = []  # Inicia el conjunto en vacío

    validacion = True
    while validacion:
        if pregunta == "s" or pregunta == "n":  # Valida que la entrada sea s o n
            validacion = False
            while pregunta == "s":
                elemento = pedir_caracter("Ingresa el caracter a agregar: ")
                conjunto.append(elemento)

                pregunta = pedir_letra_validada("¿Desea agregar un elemento al conjunto? [s/n]: ")
        else:
            print("Opción no válida.")
            pregunta = pedir_letra_validada("¿Desea agregar un elemento al conjunto? [s/n]: ")

    conjunto.sort()
    return conjunto

def crear_caracter_aleatorio():
    letras = string.ascii_letters #Incluye letras minúsculas y mayúsculas
    simbolos = string.punctuation #Incluye símbolos
    caracteres = letras + simbolos #los combina
    caracter_aleatorio = random.choice(caracteres)
    return caracter_aleatorio #Elije un caracter aleatoriamente y lo regresa

def caracteres_aleatorios():
    numero = pedir_numero_validado("¿Cuántos elementos quieres que tenga el conjunto? (0-15) ")
    conjunto = []
    validacion = True
    while validacion:
        if 0 <= numero <= 15: #Valida que el límite sea 15
            validacion = False
            for i in range(numero):
                elemento = crear_caracter_aleatorio()
                conjunto.append(elemento)
        else:
            print("Valor incorrecto. Por favor ingresa un número entre 0 y 15.")
    conjunto.sort()
    return conjunto

def palabras_manuales():
    pregunta1 = pedir_letra_validada("¿Deseas agregar un elemento al conjunto? [s/n]: ")
    conjunto = []  # Inicia el conjunto en vacío

    validacion = True
    while validacion:
        if pregunta1 == "s" or pregunta1 == "n":  # Valida que la entrada sea s o n
            validacion = False
            while pregunta1 == "s":
                elemento1 = str(input("Ingresa la palabra a agregar: "))
                conjunto.append(elemento1)

                pregunta1 = pedir_letra_validada("¿Deseas agregar un elemento al conjunto? [s/n]: ")
        else:
            print("Opción no válida.")
            pregunta1 = pedir_letra_validada("¿Desea agregar un elemento al conjunto? [s/n]: ")

    return conjunto

def pedir_palabras_aleatorias():
    validacion = 0
    tipo = str(input("¿De qué tipo quieres que sean las palabras? (frutas, colores o nombres): "))
    tipo = tipo.lower()
    while validacion == 0:
        if tipo == "frutas" or tipo == "colores" or tipo == "nombres": #Valida que el tipo sea una de esas 3 palabras
            validacion = 1
        else:
            print("La palabra es incorrecta. Intenta de nuevo.")
            tipo = str(input("¿De qué tipo quieres que sean las palabras? (frutas, colores o nombres): "))
            tipo = tipo.lower()

    cantidad = pedir_numero_validado("¿Cuántas palabras quieres que tenga el conjunto? (0-12) ")
    validacion2 = 0
    while validacion2 == 0:
        if 0<=cantidad<=12: #Valida que la cantidad no sea más de 12
            validacion2 = 1
        else:
            print("El valor ingresado es incorrecto. Intenta de nuevo.")
            cantidad = pedir_numero_validado("¿Cuántas palabras quieres que tenga el conjunto? (0-12) ")

    conjunto = palabras_aleatorias(tipo,cantidad)
    return conjunto

def palabras_aleatorias(tipo,cantidad):
    if tipo == "frutas":
        frutas = ["uva","fresa","manzana","mango","zarzamora","pera","kiwi","frambuesa","plátano","cereza","sandía","melón"]
        conjunto = random.choices(frutas,k=cantidad) #crea un conjunto con elementos aleatorios
        return conjunto
    elif tipo == "nombres":
        nombres = ["Pedro", "Juan", "Sofía", "Julia", "Omar", "María", "José", "Andrea", "Alicia", "Jorge", "Max", "Alexa"]
        conjunto = random.choices(nombres,k=cantidad)
        return conjunto
    elif tipo == "colores":
        colores = ["azul","rojo","amarillo","morado","rosa","naranja","verde","turquesa","café","gris","dorado","vino"]
        conjunto = random.choices(colores,k=cantidad)
        return conjunto

def imprimir_con_llaves(lista):
    return str(lista).replace("[","{").replace("]","}")

def mostrar_menu_principal():
    print("\nIngresa un número de acuerdo a las siguientes opciones:")
    return pedir_numero_validado("1 - Ejecutar el programa\n2 - Terminar el programa\n\n")

def mostrar_menu_secundario():
    print("\nPara crear conjuntos nuevos, regresa al menú principal")
    print("\nIngresa un número de acuerdo a las siguientes opciones:")
    return pedir_numero_validado("1 - Operaciones de conjuntos\n2 - Funciones de verificación de conjuntos"
                                 "\n3 - Volver al menú principal\n\n")
def union(conjunto1f,conjunto2f):
    conjunto = conjunto1f + conjunto2f #Se unen los dos conjuntos
    conjunto_final = []
    for i in range(len(conjunto)): #Se eliminan los elementos repetidos
        if conjunto[i] not in conjunto_final:
            conjunto_final.append(conjunto[i])
        else:
            continue
    conjunto_final.sort()
    return conjunto_final

def interseccion(conjunto1f,conjunto2f):
    conjunto1_c = conjunto_corregido(conjunto1f)
    conjunto2_c = conjunto_corregido(conjunto2f)
    conjunto_final = []
    if len(conjunto1_c) <= len(conjunto2_c):
        for i in range (len(conjunto1_c)):
            if conjunto1_c[i] in conjunto2_c:
                conjunto_final.append(conjunto1_c[i])
            else:
                continue
    else:
        for i in range (len(conjunto2_c)):
            if conjunto2_c[i] in conjunto1_c:
                conjunto_final.append(conjunto2_c[i])
            else:
                continue
    conjunto_final.sort()
    return conjunto_final

def diferencia(conjunto1f,conjunto2f):
    conjunto1_c = conjunto_corregido(conjunto1f)
    conjunto2_c = conjunto_corregido(conjunto2f)
    conjunto_final = []
    for i in range (len(conjunto1_c)):
        if conjunto1_c[i] not in conjunto2_c:
            conjunto_final.append(conjunto1_c[i])
        else:
            continue
    conjunto_final.sort()
    return conjunto_final

def diferencia_simetrica(conjunto1f,conjunto2f):
    conjunto1_c = conjunto_corregido(conjunto1f)
    conjunto2_c = conjunto_corregido(conjunto2f)
    conjunto_final = union(conjunto1_c,conjunto2_c)
    conjunto_interseccionf = interseccion(conjunto1_c,conjunto2_c)
    for i in range (len(conjunto_interseccionf)):
        conjunto_final.remove(conjunto_interseccionf[i])

    conjunto_final.sort()
    return conjunto_final

def complemento(conjuntopr,conjuntos1,conjuntos2):
    union1 = union(conjuntopr,conjuntos1)
    universo = union(union1,conjuntos2)
    for i in range (len(conjuntopr)):
        universo.remove(conjuntopr[i])

    universo.sort()
    return universo

def subconjunto(conjunto1f,conjunto2f):
    conjunto1_c = conjunto_corregido(conjunto1f)
    conjunto2_c = conjunto_corregido(conjunto2f)
    if len(conjunto1_c) > len(conjunto2_c):
        return False
    elif len(conjunto1_c) == 0:
        return True
    else:
        for i in range (len(conjunto1_c)):
            if conjunto1_c[i] in conjunto2_c:
                continue
            else:
                return False
    return True

def igualdad(conjunto1f,conjunto2f):
    conjunto1_c = conjunto_corregido(conjunto1f)
    conjunto2_c = conjunto_corregido(conjunto2f)
    if len(conjunto1_c) != len(conjunto2_c):
        return False
    else:
        for i in range(len(conjunto1_c)):
            if conjunto1_c[i] == conjunto2_c[i]:
                continue
            else:
                return False
    return True

#Aquí comienza el programa!!!

valor = mostrar_menu_principal()

while valor != 2: #si se ingresa 2, se termina el programa
    if valor == 1:
        print("Iniciando programa...\n")
        print ("¿Qué tipo de elementos desea que haya en el conjunto A? ") #Comenzar con el primer conjunto

        operacion = pedir_numero_validado("1 - Números enteros (1-100)\n2 - Caracteres (letras o símbolos)\n"
                    "3 - Palabras\n\n")
        c1 = True
        while c1:
            if operacion == 1 or operacion == 2 or operacion == 3: #Validar que el valor en operacion sea 1, 2 0 3
                c1 = False
                continue
            else:
                print("El número es incorrecto. Intenta de nuevo.")
                operacion = pedir_numero_validado("\n1 - Números enteros (1-100)\n2 - Caracteres (letras o símbolos)\n"
                                                  "3 - Palabras\n\n")

        elementos = pedir_numero_validado("Seleccione una opción:\n1 - Ingresar los elementos manualmente\n"
                              "2 - Generar elementos de manera aleatoria\n\n")

        if operacion == 1:
            c2 = True #Validar que el valor en elementos sea 1 o 2
            while c2:
                if elementos == 1: #Si el usuario quiere ingresar los valores
                    c2 = False
                    conjunto_A1 = numeros_manuales()
                    print("\nEl conjunto A es: " + imprimir_con_llaves(conjunto_A1))
                    conjunto_A = conjunto_corregido(conjunto_A1)

                elif elementos == 2: #Si el usuario quiere que sea de manera aleatoria
                    c2 = False
                    conjunto_A1 = numeros_aleatorios()
                    print("\nEl conjunto A es: " + imprimir_con_llaves(conjunto_A1))
                    conjunto_A = conjunto_corregido(conjunto_A1)
                else:
                    print("Opción incorrecta. Por favor ingresa 1 o 2\n")
                    elementos = pedir_numero_validado(
                        "Seleccione una opción:\n1 - Ingresar los elementos manualmente\n"
                        "2 - Generar elementos de manera aleatoria\n\n")

        elif operacion == 2:
            c3 = True
            while c3: #Validar que el valor en elementos sea 1 o 2
                if elementos == 1:
                    c3 = False
                    conjunto_A1 = caracteres_manuales()
                    print("\nEl conjunto A es: " + imprimir_con_llaves(conjunto_A1))
                    conjunto_A = conjunto_corregido(conjunto_A1)
                elif elementos == 2:
                    c3 = False
                    conjunto_A1 = caracteres_aleatorios()
                    print("\nEl conjunto A es: " + imprimir_con_llaves(conjunto_A1))
                    conjunto_A = conjunto_corregido(conjunto_A1)
                else:
                    print("Opción incorrecta. Por favor ingresa 1 o 2\n")
                    elementos = pedir_numero_validado(
                        "Seleccione una opción:\n1 - Ingresar los elementos manualmente\n"
                        "2 - Generar elementos de manera aleatoria\n\n")

        elif operacion == 3:
            c4 = True
            while c4: #Validar que el valor en elementos sea 1 o 2
                if elementos == 1:
                    c4 = False
                    conjunto_A1 = palabras_manuales()
                    print("\nEl conjunto A es: " + imprimir_con_llaves(conjunto_A1))
                    conjunto_A = conjunto_corregido(conjunto_A1)
                elif elementos == 2:
                    c4 = False
                    conjunto_A1 = pedir_palabras_aleatorias()
                    print("\nEl conjunto A es: " + imprimir_con_llaves(conjunto_A1))
                    conjunto_A = conjunto_corregido(conjunto_A1)
                else:
                    print("Opción incorrecta. Por favor ingresa 1 o 2\n")
                    elementos = pedir_numero_validado(
                        "Seleccione una opción:\n1 - Ingresar los elementos manualmente\n"
                        "2 - Generar elementos de manera aleatoria\n\n")

    #Aquí termina el conjunto A y comienza el conjunto B!!!

        continuar = 0
        quieres_continuar = pedir_letra_validada("\n¿Deseas continuar con la creación de conjuntos? [s/n]: ")
        while continuar == 0:
            if quieres_continuar == "n": #Preguntar al usuario si quiere continuar con el programa
                continuar = 1
                conjunto_B = []
                conjunto_C = []
            else: #Si quiere continuar, comienza con el conjunto B
                print("\n¿Qué tipo de elementos deseas que haya en el conjunto B? ")  # Comenzar con el primer conjunto

                operacion2 = pedir_numero_validado("1 - Números enteros (1-100)\n2 - Caracteres (letras o símbolos)\n"
                                                  "3 - Palabras\n\n")
                c5 = True
                while c5:
                    if operacion2 == 1 or operacion2 == 2 or operacion2 == 3:  # Validar que el valor en operacion sea 1, 2 0 3
                        c5 = False
                        continue
                    else:
                        print("El número es incorrecto. Intenta de nuevo.")
                        operacion2 = pedir_numero_validado(
                            "\n1 - Números enteros (1-100)\n2 - Caracteres (letras o símbolos)\n"
                            "3 - Palabras\n\n")

                elementos2 = pedir_numero_validado("Seleccione una opción:\n1 - Ingresar los elementos manualmente\n"
                                                  "2 - Generar elementos de manera aleatoria\n\n")

                if operacion2 == 1:
                    c6 = True  # Validar que el valor en elementos sea 1 o 2
                    while c6:
                        if elementos2 == 1:  # Si el usuario quiere ingresar los valores
                            c6 = False
                            conjunto_B1 = numeros_manuales()
                            print("\nEl conjunto B es: " + imprimir_con_llaves(conjunto_B1))
                            conjunto_B = conjunto_corregido(conjunto_B1)

                        elif elementos2 == 2:  # Si el usuario quiere que sea de manera aleatoria
                            c6 = False
                            conjunto_B1 = numeros_aleatorios()
                            print("\nEl conjunto B es: " + imprimir_con_llaves(conjunto_B1))
                            conjunto_B = conjunto_corregido(conjunto_B1)
                        else:
                            print("Opción incorrecta. Por favor ingresa 1 o 2\n")
                            elementos2 = pedir_numero_validado(
                                "Seleccione una opción:\n1 - Ingresar los elementos manualmente\n"
                                "2 - Generar elementos de manera aleatoria\n\n")

                elif operacion2 == 2:
                    c7 = True
                    while c7:  # Validar que el valor en elementos sea 1 o 2
                        if elementos2 == 1:
                            c7 = False
                            conjunto_B1 = caracteres_manuales()
                            print("\nEl conjunto B es: " + imprimir_con_llaves(conjunto_B1))
                            conjunto_B = conjunto_corregido(conjunto_B1)
                        elif elementos2 == 2:
                            c7 = False
                            conjunto_B1 = caracteres_aleatorios()
                            print("\nEl conjunto B es: " + imprimir_con_llaves(conjunto_B1))
                            conjunto_B = conjunto_corregido(conjunto_B1)
                        else:
                            print("Opción incorrecta. Por favor ingresa 1 o 2\n")
                            elementos2 = pedir_numero_validado(
                                "Seleccione una opción:\n1 - Ingresar los elementos manualmente\n"
                                "2 - Generar elementos de manera aleatoria\n\n")

                elif operacion2 == 3:
                    c8 = True
                    while c8:  # Validar que el valor en elementos sea 1 o 2
                        if elementos2 == 1:
                            c8 = False
                            conjunto_B1 = palabras_manuales()
                            print("\nEl conjunto B es: " + imprimir_con_llaves(conjunto_B1))
                            conjunto_B = conjunto_corregido(conjunto_B1)
                        elif elementos2 == 2:
                            c8 = False
                            conjunto_B1 = pedir_palabras_aleatorias()
                            print("\nEl conjunto B es: " + imprimir_con_llaves(conjunto_B1))
                            conjunto_B = conjunto_corregido(conjunto_B1)
                        else:
                            print("Opción incorrecta. Por favor ingresa 1 o 2\n")
                            elementos2 = pedir_numero_validado(
                                "Seleccione una opción:\n1 - Ingresar los elementos manualmente\n"
                                "2 - Generar elementos de manera aleatoria\n\n")



    #Aquí termina el conjunto B y comienza el C!!!

                continuar2 = 0
                quieres_continuar2 = pedir_letra_validada("\n¿Deseas continuar con la creación de conjuntos? [s/n]: ")
                while continuar2 == 0: #Preguntar al usuario si quiere continuar con el programa
                    if quieres_continuar2 == "n":
                        continuar2 = 1
                        conjunto_C = []
                    else: #Si quiere continuar, comienza con el conjunto C
                        print("\n¿Qué tipo de elementos deseas que haya en el conjunto C? ")  # Comenzar con el primer conjunto

                        operacion3 = pedir_numero_validado("1 - Números enteros (1-100)\n2 - Caracteres (letras o símbolos)\n"
                                                           "3 - Palabras\n\n")
                        c9 = True
                        while c9:
                            if operacion3 == 1 or operacion3 == 2 or operacion3 == 3:  # Validar que el valor en operacion sea 1, 2 0 3
                                c9 = False
                                continue
                            else:
                                print("El número es incorrecto. Intenta de nuevo.")
                                operacion3 = pedir_numero_validado(
                                    "\n1 - Números enteros (1-100)\n2 - Caracteres (letras o símbolos)\n"
                                    "3 - Palabras\n\n")

                        elementos3 = pedir_numero_validado("Seleccione una opción:\n1 - Ingresar los elementos manualmente\n"
                                                           "2 - Generar elementos de manera aleatoria\n\n")

                        if operacion3 == 1:
                            c10 = True  # Validar que el valor en elementos sea 1 o 2
                            while c10:
                                if elementos3 == 1:  # Si el usuario quiere ingresar los valores
                                    c10 = False
                                    conjunto_C1 = numeros_manuales()
                                    print("\nEl conjunto C es: " + imprimir_con_llaves(conjunto_C1))
                                    conjunto_C = conjunto_corregido(conjunto_C1)

                                elif elementos3 == 2:  # Si el usuario quiere que sea de manera aleatoria
                                    c10 = False
                                    conjunto_C1 = numeros_aleatorios()
                                    print("\nEl conjunto C es: " + imprimir_con_llaves(conjunto_C1))
                                    conjunto_C = conjunto_corregido(conjunto_C1)
                                else:
                                    print("Opción incorrecta. Por favor ingresa 1 o 2\n")
                                    elementos3 = pedir_numero_validado(
                                        "Seleccione una opción:\n1 - Ingresar los elementos manualmente\n"
                                        "2 - Generar elementos de manera aleatoria\n\n")

                        elif operacion3 == 2:
                            c11 = True
                            while c11:  # Validar que el valor en elementos sea 1 o 2
                                if elementos3 == 1:
                                    c11 = False
                                    conjunto_C1 = caracteres_manuales()
                                    print("\nEl conjunto C es: " + imprimir_con_llaves(conjunto_C1))
                                    conjunto_C = conjunto_corregido(conjunto_C1)
                                elif elementos3 == 2:
                                    c11 = False
                                    conjunto_C1 = caracteres_aleatorios()
                                    print("\nEl conjunto C es: " + imprimir_con_llaves(conjunto_C1))
                                    conjunto_C = conjunto_corregido(conjunto_C1)
                                else:
                                    print("Opción incorrecta. Por favor ingresa 1 o 2\n")
                                    elementos3 = pedir_numero_validado(
                                        "Seleccione una opción:\n1 - Ingresar los elementos manualmente\n"
                                        "2 - Generar elementos de manera aleatoria\n\n")

                        elif operacion3 == 3:
                            c12 = True
                            while c12:  # Validar que el valor en elementos sea 1 o 2
                                if elementos3 == 1:
                                    c12 = False
                                    conjunto_C1 = palabras_manuales()
                                    print("\nEl conjunto C es: " + imprimir_con_llaves(conjunto_C1))
                                    conjunto_C = conjunto_corregido(conjunto_C1)
                                elif elementos3 == 2:
                                    c12 = False
                                    conjunto_C1 = pedir_palabras_aleatorias()
                                    print("\nEl conjunto C es: " + imprimir_con_llaves(conjunto_C1))
                                    conjunto_C = conjunto_corregido(conjunto_C1)
                                else:
                                    print("Opción incorrecta. Por favor ingresa 1 o 2\n")
                                    elementos3 = pedir_numero_validado(
                                        "Seleccione una opción:\n1 - Ingresar los elementos manualmente\n"
                                        "2 - Generar elementos de manera aleatoria\n\n")

                    continuar2 = 1
            continuar = 1

#Aquí termina el código de pedir conjuntos. Comienzan las operaciones!!!

        valor2 = mostrar_menu_secundario()
        while valor2 != 3:
            if valor2 == 1: #Comienzan operaciones de conjuntos!!!
                operacion = pedir_numero_validado("\nSelecciona una opción:\n1 - Unión\n2 - Intersección\n"
                                           "3 - Diferencia\n4 - Diferencia simétrica\n5 - Complemento\n\n")
                rf = 0
                while rf == 0: #Validar que el número de operación sea 1-5
                #OPERACION UNION
                    if operacion == 1:
                        rf = 1
                        conjunto1 = pedir_letra_validada("Ingresa la letra del primer conjunto a utilizar (A,B o C):\n\n")
                        r = 0
                        while r == 0: #Valida que la letra ingresada sea A, B o C
                            if conjunto1 == "a":
                                r = 1
                                conjunto1_correcto = conjunto_A
                            elif conjunto1 == "b":
                                r = 1
                                conjunto1_correcto = conjunto_B
                            elif conjunto1 == "c":
                                r = 1
                                conjunto1_correcto = conjunto_C
                            else:
                                print("\nLetra no válida. Por favor ingresa A, B o C")
                                conjunto1 = pedir_letra_validada("Ingresa la letra del primer conjunto a utilizar (A,B o C):\n")


                        conjunto2 = pedir_letra_validada("Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        r1 = 0
                        while r1 == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == conjunto2: #Si los conjuntos son iguales, se vuelve a pedir el segundo
                                print("\nError, el conjunto 1 debe ser diferente de " + str(conjunto1).upper())
                                conjunto2 = pedir_letra_validada("Ingresa la letra del primer conjunto a utilizar (A,B o C):\n")
                                continue

                            if conjunto2 == "a":
                                r1 = 1
                                conjunto2_correcto = conjunto_A
                            elif conjunto2 == "b":
                                r1 = 1
                                conjunto2_correcto = conjunto_B
                            elif conjunto2 == "c":
                                r1 = 1
                                conjunto2_correcto = conjunto_C
                            else:
                                print("Letra no válida. Por favor ingresa A, B o C\n")
                                conjunto2 = pedir_letra_validada("Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        conjunto_unido = union(conjunto1_correcto, conjunto2_correcto) #se llama a la función de unión
                        print("\n" + str(conjunto1.upper()) + " ∪ " + str(conjunto2.upper()) + ": " + imprimir_con_llaves(conjunto_unido))

                    #OPERACION INTERSECCION
                    elif operacion == 2:
                        rf = 1
                        conjunto1 = pedir_letra_validada("Ingresa la letra del primer conjunto a utilizar (A,B o C):\n\n")
                        r = 0
                        while r == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == "a":
                                r = 1
                                conjunto1_correcto = conjunto_A
                            elif conjunto1 == "b":
                                r = 1
                                conjunto1_correcto = conjunto_B
                            elif conjunto1 == "c":
                                r = 1
                                conjunto1_correcto = conjunto_C
                            else:
                                print("\nLetra no válida. Por favor ingresa A, B o C")
                                conjunto1 = pedir_letra_validada(
                                    "Ingresa la letra del primer conjunto a utilizar (A,B o C):\n")

                        conjunto2 = pedir_letra_validada("Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        r1 = 0
                        while r1 == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == conjunto2:  # Si los conjuntos son iguales, se vuelve a pedir el segundo
                                print("\nError, el conjunto 1 debe ser diferente de " + str(conjunto1).upper())
                                conjunto2 = pedir_letra_validada(
                                    "Ingresa la letra del primer conjunto a utilizar (A,B o C):\n")
                                continue

                            if conjunto2 == "a":
                                r1 = 1
                                conjunto2_correcto = conjunto_A
                            elif conjunto2 == "b":
                                r1 = 1
                                conjunto2_correcto = conjunto_B
                            elif conjunto2 == "c":
                                r1 = 1
                                conjunto2_correcto = conjunto_C
                            else:
                                print("Letra no válida. Por favor ingresa A, B o C\n")
                                conjunto2 = pedir_letra_validada(
                                    "Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        conjunto_interseccion = interseccion(conjunto1_correcto, conjunto2_correcto)  # se llama a la función de intersección
                        print(
                            "\n" + str(conjunto1.upper()) + " ∩ " + str(conjunto2.upper()) + ": " + imprimir_con_llaves(
                                conjunto_interseccion))

                    #OPERACION DIFERENCIA!!!
                    elif operacion == 3:
                        rf = 1
                        conjunto1 = pedir_letra_validada("Ingresa la letra del primer conjunto a utilizar (A,B o C):\n\n")
                        r = 0
                        while r == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == "a":
                                r = 1
                                conjunto1_correcto = conjunto_A
                            elif conjunto1 == "b":
                                r = 1
                                conjunto1_correcto = conjunto_B
                            elif conjunto1 == "c":
                                r = 1
                                conjunto1_correcto = conjunto_C
                            else:
                                print("\nLetra no válida. Por favor ingresa A, B o C")
                                conjunto1 = pedir_letra_validada(
                                    "Ingresa la letra del primer conjunto a utilizar (A,B o C):\n")

                        conjunto2 = pedir_letra_validada(
                            "Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        r1 = 0
                        while r1 == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == conjunto2:  # Si los conjuntos son iguales, se vuelve a pedir el segundo
                                print("\nError, el conjunto 1 debe ser diferente de " + str(conjunto1).upper())
                                conjunto2 = pedir_letra_validada(
                                    "Ingresa la letra del primer conjunto a utilizar (A,B o C):\n")
                                continue

                            if conjunto2 == "a":
                                r1 = 1
                                conjunto2_correcto = conjunto_A
                            elif conjunto2 == "b":
                                r1 = 1
                                conjunto2_correcto = conjunto_B
                            elif conjunto2 == "c":
                                r1 = 1
                                conjunto2_correcto = conjunto_C
                            else:
                                print("Letra no válida. Por favor ingresa A, B o C\n")
                                conjunto2 = pedir_letra_validada(
                                    "Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        conjunto_diferencia = diferencia(conjunto1_correcto,conjunto2_correcto)  # se llama a la función de diferencia
                        print(
                            "\n" + str(conjunto1.upper()) + " - " + str(conjunto2.upper()) + ": " + imprimir_con_llaves(
                                conjunto_diferencia))

                    #OPERACION DIFERENCIA SIMETRICA!!!
                    elif operacion == 4:
                        rf = 1
                        conjunto1 = pedir_letra_validada("Ingresa la letra del primer conjunto a utilizar (A,B o C):\n\n")
                        r = 0
                        while r == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == "a":
                                r = 1
                                conjunto1_correcto = conjunto_A
                            elif conjunto1 == "b":
                                r = 1
                                conjunto1_correcto = conjunto_B
                            elif conjunto1 == "c":
                                r = 1
                                conjunto1_correcto = conjunto_C
                            else:
                                print("\nLetra no válida. Por favor ingresa A, B o C")
                                conjunto1 = pedir_letra_validada(
                                    "Ingresa la letra del primer conjunto a utilizar (A,B o C):\n")

                        conjunto2 = pedir_letra_validada("Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        r1 = 0
                        while r1 == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == conjunto2:  # Si los conjuntos son iguales, se vuelve a pedir el segundo
                                print("\nError, el conjunto 1 debe ser diferente de " + str(conjunto1).upper())
                                conjunto2 = pedir_letra_validada("Ingresa la letra del primer conjunto a utilizar (A,B o C):\n")
                                continue

                            if conjunto2 == "a":
                                r1 = 1
                                conjunto2_correcto = conjunto_A
                            elif conjunto2 == "b":
                                r1 = 1
                                conjunto2_correcto = conjunto_B
                            elif conjunto2 == "c":
                                r1 = 1
                                conjunto2_correcto = conjunto_C
                            else:
                                print("Letra no válida. Por favor ingresa A, B o C\n")
                                conjunto2 = pedir_letra_validada(
                                    "Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        conjunto_diferencia_simetrica = diferencia_simetrica(conjunto1_correcto,conjunto2_correcto)  # se llama a la función de diferencia simétrica
                        print("\n" + str(conjunto1.upper()) + " Δ " + str(conjunto2.upper()) + ": " + imprimir_con_llaves(
                            conjunto_diferencia_simetrica))

                    #OPERACION COMPLEMENTO!!!
                    elif operacion == 5:
                        rf = 1
                        conjunto1 = pedir_letra_validada("Ingresa la letra del conjunto a utilizar (A,B o C):\n\n")
                        r = 0
                        while r == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == "a":
                                r = 1
                                conjunto_complemento = complemento(conjunto_A,conjunto_B,conjunto_C)
                                print("\n" + str(conjunto1.upper()) + "’: " + imprimir_con_llaves(
                                    conjunto_complemento))
                            elif conjunto1 == "b":
                                r = 1
                                conjunto_complemento = complemento(conjunto_B, conjunto_A, conjunto_C)
                                print("\n" + str(conjunto1.upper()) + "’: " + imprimir_con_llaves(
                                    conjunto_complemento))
                            elif conjunto1 == "c":
                                r = 1
                                conjunto_complemento = complemento(conjunto_C, conjunto_B, conjunto_A)
                                print("\n" + str(conjunto1.upper()) + "’: " + imprimir_con_llaves(
                                    conjunto_complemento))
                            else:
                                print("\nLetra no válida. Por favor ingresa A, B o C")
                                conjunto1 = pedir_letra_validada(
                                    "Ingresa la letra del primer conjunto a utilizar (A,B o C):\n")

                    else:
                        print("\nNúmero incorrecto. Por favor ingresa un número entre 1 y 5")
                        operacion = pedir_numero_validado("\nSelecciona una opción:\n1 - Unión\n2 - Intersección\n"
                                                          "3 - Diferencia\n4 - Diferencia simétrica\n5 - Complemento\n\n")

            elif valor2 == 2: #Comienzan las verificaciones!!!
                operacion = pedir_numero_validado("\nSelecciona una opción:\n1 - Subconjunto\n2 - Subconjunto propio\n"
                                                  "3 - Conjuntos disjuntos\n4 - Igualdad de conjuntos\n")
                rf = 0 #Validar que el número ingresado sea correcto
                while rf == 0:
                    #SUBCONJUNTO!!!
                    if operacion == 1:
                        rf = 1
                        conjunto1 = pedir_letra_validada(
                            "\nIngresa la letra del primer conjunto a utilizar (A,B o C):\n")
                        r = 0
                        while r == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == "a":
                                r = 1
                                conjunto1_correcto = conjunto_A
                            elif conjunto1 == "b":
                                r = 1
                                conjunto1_correcto = conjunto_B
                            elif conjunto1 == "c":
                                r = 1
                                conjunto1_correcto = conjunto_C
                            else:
                                print("\nLetra no válida. Por favor ingresa A, B o C")
                                conjunto1 = pedir_letra_validada(
                                    "\nIngresa la letra del primer conjunto a utilizar (A,B o C):\n")

                        conjunto2 = pedir_letra_validada(
                            "Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        r1 = 0
                        while r1 == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == conjunto2:  # Si los conjuntos son iguales, se vuelve a pedir el segundo
                                print("\nError, el conjunto 1 debe ser diferente de " + str(conjunto1).upper())
                                conjunto2 = pedir_letra_validada(
                                    "Ingresa la letra del primer conjunto a utilizar (A,B o C):\n")
                                continue

                            if conjunto2 == "a":
                                r1 = 1
                                conjunto2_correcto = conjunto_A
                            elif conjunto2 == "b":
                                r1 = 1
                                conjunto2_correcto = conjunto_B
                            elif conjunto2 == "c":
                                r1 = 1
                                conjunto2_correcto = conjunto_C
                            else:
                                print("Letra no válida. Por favor ingresa A, B o C\n")
                                conjunto2 = pedir_letra_validada(
                                    "Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        evaluar_subconjunto = subconjunto(conjunto1_correcto,conjunto2_correcto)
                        if evaluar_subconjunto:
                            print("\n" + str(conjunto1.upper()) + " ⊆ " + str(conjunto2.upper()))
                            print(str(conjunto1.upper())+" es subconjunto de "+str(conjunto2.upper()))
                        else:
                            print("\n" + str(conjunto1.upper()) + " ⊄ " + str(conjunto2.upper()))
                            print(str(conjunto1.upper()) + " no es subconjunto de " + str(conjunto2.upper()))

                    #SUBCONJUNTO PROPIO
                    elif operacion == 2:
                        rf = 1
                        conjunto1 = pedir_letra_validada(
                            "\nIngresa la letra del primer conjunto a utilizar (A,B o C):\n")
                        r = 0
                        while r == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == "a":
                                r = 1
                                conjunto1_correcto = conjunto_A
                            elif conjunto1 == "b":
                                r = 1
                                conjunto1_correcto = conjunto_B
                            elif conjunto1 == "c":
                                r = 1
                                conjunto1_correcto = conjunto_C
                            else:
                                print("\nLetra no válida. Por favor ingresa A, B o C")
                                conjunto1 = pedir_letra_validada(
                                    "\nIngresa la letra del primer conjunto a utilizar (A,B o C):\n")

                        conjunto2 = pedir_letra_validada(
                            "Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        r1 = 0
                        while r1 == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == conjunto2:  # Si los conjuntos son iguales, se vuelve a pedir el segundo
                                print("\nError, el conjunto 1 debe ser diferente de " + str(conjunto1).upper())
                                conjunto2 = pedir_letra_validada(
                                    "Ingresa la letra del primer conjunto a utilizar (A,B o C):\n")
                                continue

                            if conjunto2 == "a":
                                r1 = 1
                                conjunto2_correcto = conjunto_A
                            elif conjunto2 == "b":
                                r1 = 1
                                conjunto2_correcto = conjunto_B
                            elif conjunto2 == "c":
                                r1 = 1
                                conjunto2_correcto = conjunto_C
                            else:
                                print("Letra no válida. Por favor ingresa A, B o C\n")
                                conjunto2 = pedir_letra_validada(
                                    "Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        if conjunto1_correcto == conjunto2_correcto:
                            print("\n" + str(conjunto1.upper()) + " ⊄ " + str(conjunto2.upper()))
                            print(str(conjunto1.upper()) + " no es subconjunto propio de " + str(conjunto2.upper()))
                        else:
                            evaluar_subconjunto = subconjunto(conjunto1_correcto, conjunto2_correcto)
                            if evaluar_subconjunto:
                                print("\n" + str(conjunto1.upper()) + " ⊂ " + str(conjunto2.upper()))
                                print(str(conjunto1.upper()) + " es subconjunto propio de " + str(conjunto2.upper()))
                            else:
                                print("\n" + str(conjunto1.upper()) + " ⊄ " + str(conjunto2.upper()))
                                print(str(conjunto1.upper()) + " no es subconjunto propio de " + str(conjunto2.upper()))

                    #CONJUNTOS DISJUNTOS!!!
                    elif operacion == 3:
                        rf = 1
                        conjunto1 = pedir_letra_validada(
                            "\nIngresa la letra del primer conjunto a utilizar (A,B o C):\n")
                        r = 0
                        while r == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == "a":
                                r = 1
                                conjunto1_correcto = conjunto_A
                            elif conjunto1 == "b":
                                r = 1
                                conjunto1_correcto = conjunto_B
                            elif conjunto1 == "c":
                                r = 1
                                conjunto1_correcto = conjunto_C
                            else:
                                print("\nLetra no válida. Por favor ingresa A, B o C")
                                conjunto1 = pedir_letra_validada(
                                    "\nIngresa la letra del primer conjunto a utilizar (A,B o C):\n")

                        conjunto2 = pedir_letra_validada(
                            "Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        r1 = 0
                        while r1 == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == conjunto2:  # Si los conjuntos son iguales, se vuelve a pedir el segundo
                                print("\nError, el conjunto 1 debe ser diferente de " + str(conjunto1).upper())
                                conjunto2 = pedir_letra_validada(
                                    "Ingresa la letra del primer conjunto a utilizar (A,B o C):\n")
                                continue

                            if conjunto2 == "a":
                                r1 = 1
                                conjunto2_correcto = conjunto_A
                            elif conjunto2 == "b":
                                r1 = 1
                                conjunto2_correcto = conjunto_B
                            elif conjunto2 == "c":
                                r1 = 1
                                conjunto2_correcto = conjunto_C
                            else:
                                print("Letra no válida. Por favor ingresa A, B o C\n")
                                conjunto2 = pedir_letra_validada(
                                    "Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        interseccion_conjunto = interseccion(conjunto1_correcto, conjunto2_correcto)
                        if len(interseccion_conjunto) == 0:
                            print("\n" + str(conjunto1.upper()) + " ∩ " + str(conjunto2.upper()) + " = ∅")
                            print("Sí son conjuntos disjuntos")
                        else:
                            print("\n" + str(conjunto1.upper()) + " ∩ " + str(conjunto2.upper()) + " ≠ ∅")
                            print("No son conjuntos disjuntos")

                    #IGUALDAD!!!
                    elif operacion == 4:
                        rf = 1
                        conjunto1 = pedir_letra_validada(
                            "\nIngresa la letra del primer conjunto a utilizar (A,B o C):\n")
                        r = 0
                        while r == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == "a":
                                r = 1
                                conjunto1_correcto = conjunto_A
                            elif conjunto1 == "b":
                                r = 1
                                conjunto1_correcto = conjunto_B
                            elif conjunto1 == "c":
                                r = 1
                                conjunto1_correcto = conjunto_C
                            else:
                                print("\nLetra no válida. Por favor ingresa A, B o C")
                                conjunto1 = pedir_letra_validada(
                                    "\nIngresa la letra del primer conjunto a utilizar (A,B o C):\n")

                        conjunto2 = pedir_letra_validada(
                            "Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        r1 = 0
                        while r1 == 0:  # Valida que la letra ingresada sea A, B o C
                            if conjunto1 == conjunto2:  # Si los conjuntos son iguales, se vuelve a pedir el segundo
                                print("\nError, el conjunto 1 debe ser diferente de " + str(conjunto1).upper())
                                conjunto2 = pedir_letra_validada(
                                    "Ingresa la letra del primer conjunto a utilizar (A,B o C):\n")
                                continue

                            if conjunto2 == "a":
                                r1 = 1
                                conjunto2_correcto = conjunto_A
                            elif conjunto2 == "b":
                                r1 = 1
                                conjunto2_correcto = conjunto_B
                            elif conjunto2 == "c":
                                r1 = 1
                                conjunto2_correcto = conjunto_C
                            else:
                                print("Letra no válida. Por favor ingresa A, B o C\n")
                                conjunto2 = pedir_letra_validada(
                                    "Ingresa la letra del segundo conjunto a utilizar (A,B o C):\n")

                        igualdad_conjunto = igualdad(conjunto1_correcto, conjunto2_correcto)
                        if igualdad_conjunto:
                            print("\n" + str(conjunto1.upper()) + " = " + str(conjunto2.upper()))
                            print(str(conjunto1.upper()) + " es igual a " + str(conjunto2.upper()))
                        else:
                            print("\n" + str(conjunto1.upper()) + " ≠ " + str(conjunto2.upper()))
                            print(str(conjunto1.upper()) + " no es igual a " + str(conjunto2.upper()))

                    else:
                        print("\nNúmero incorrecto. Por favor ingresa un número entre 1 y 4")
                        operacion = pedir_numero_validado("\nSelecciona una opción:\n1 - Subconjunto\n2 - Subconjunto propio\n"
                                                  "3 - Conjuntos disjuntos\n4 - Igualdad de conjuntos\n")

            else:
                print("Opción no válida. Por favor ingresa 1, 2 o 3")

            valor2 = mostrar_menu_secundario()

    else:
        print("Opción no válida. Por favor ingresa 1 o 2")

    valor = mostrar_menu_principal()

print("Porgrama terminado.")