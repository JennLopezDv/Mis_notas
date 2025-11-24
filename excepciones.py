
#!                      _____  __   __  _____  _____  _____    _____  __    ___   _    _  _____  _____  
#!                     |  ___| \ \ / / / ____||  ___||  __ \  / ____||  |  / _ \ | \  | ||  ___||  ___| 
#!                     | |___   \   / | |     | |___ | |__) || |     |  | | | | ||  \ | || |___ | |___  
#!                     |  ___|   | |  | |     |  ___||  ___/ | |     |  | | | | ||   \| ||  ___|| __  | 
#!                     | |___   /   \ | |____ | |___ | |     | |____ |  | | |_| || |\   || |___  ___| | 
#!                     |_____| /_/ \_\ \_____||_____||_|      \_____||__|  \___/ |_| \__||_____||_____|

#? Hay momentos en nuestro código en el que el resultado de una operación no es válido, por ejemplo dividir entre cero
#? eso rompería nuestro código y nos haría arrancarlo desde cero, lo cual sería muy inconveniente, también podría
#? pasar cuando le pedimos a un usuario que ingrese su edad y esperamos que ingrese números, pero resulta ingresando
#? su nombre, esto también reventaría el código. Para este tipo de situaciones se crean las excepciones, que es
#? agarrar el pedazo de código que sabemos puede generar error y meterlo entre la sintaxis correspondiente a cada
#? tipo de excepción, de modo que el código no se rompa, sino que muestre un mensaje al usuario de error y le 
#? permita volver a intentar ingresar el dato o corregir las acciones. 

#TODO: TIPOS DE EXCEPCIONES:
#? Para todo tipo de error hay una excepción en específico, por ejemplo, divisiones por cero, un valor entero cuando
#? se esperaba un String, la solicitud de una clave inexistente en un diccionario, entre muchas otras, para hablar
#? de la sintaxis usaremos la excepción base, la cual acoje todas las excepcione, pero OJO!! Esta excepción la 
#? usaremos solo a modo de ejemplo de la sintaxis, ya que......... 
#! Siempre se tiene que usar el tipo de excepción asociada al error que se espera se pueda presentar, para eso
#! existe una excepción específica para cada error.  

#TODO: SINTAXIS

# try:                            #? Primero empleamos la palabra try para encapsular el código normal de nuestra app
#     print(10 / 0)               #? Este es el código de nuestra app.                             
# except Exception as e:          #? Si hay un error en ese código capturado en el try, dale manejo con esta excepción            
#     print(f"Hay un error: {e}") #? una vez manejado, muéstra un mensaje confirmando el error 
                                        #?El as e: en nuestro código se usa para guardar el error en una variable
                                        #? y poder tener más detalles de dicho error usando dicha variable. 

#TODO: Explicación de la sintaxis: 
#? Cuando sepamos que nuestro código puede llegar a generar un error, lo metemos dentro de un try, ese try intenta
#? correr nuestro código, solo si hay un error, hay que capturarlo, esa captura se hace con el except seguido por
#? el tipo de error, en esta ocasión, se empleó el error general Exception, pero debe usarse uno específico, 
#? en este caso sería ZeroDivisionError. 

#TODO: Lista de los errores que se pueden presentar en python y so respectiva excepción:

# BaseException	        #? Clase base para todas las excepciones en Python. (NO usar)
# Exception	            #? Clase base para todas las excepciones que pueden ser manejadas. (Usar como última instancia)
# ArithmeticError	    #? Clase base para errores matemáticos como división por cero.
# ZeroDivisionError	    #? Error al dividir un número por cero.
# ValueError	        #? Valor no válido para una operación o función.
# TypeError	            #? Operación o función aplicada a un tipo incompatible.
# IndexError	        #? Índice fuera de rango en una lista o secuencia.
# KeyError	            #? Clave no encontrada en un diccionario.
# NameError	            #? Identificador no declarado o no definido.
# AttributeError	    #? Atributo no existente en un objeto.
# ImportError	        #? Error al importar un módulo.
# ModuleNotFoundError	#? Subclase de ImportError, el módulo no existe.
# FileNotFoundError	    #? Archivo o directorio no encontrado.
# IOError	            #? Error de entrada/salida, relacionado con archivos.
# OSError	            #? Error del sistema operativo.
# RuntimeError	        #? Error general en tiempo de ejecución.
# StopIteration	        #? Final de un iterador.
# OverflowError	        #? Resultado matemático demasiado grande para representarse.
# MemoryError	        #? Falta de memoria disponible.
# AssertionError	    #? Falla en una declaración assert.
# KeyboardInterrupt	    #? Interrupción del programa por el usuario (Ctrl+C).
# SystemExit	        #? Solicitud para salir del intérprete de Python.

#! Excepciones que son muy comunes y probablemente sí usarás en tu diaria programación:

#####################TODO: ValueError

#? Al manejar entradas del usuario o convertir datos (ej. de cadenas a números).
#! Frecuencia: Alta.
#? Ejemplo típico: Validar que el usuario ingrese un número.

# try:
#     variable = int(input("Por favor ingrese un número"))  #? Si el usuario ingresa algo diferente a un entero
# except ValueError:                                        #? se captura el error y se muestra el mensaje
#     print(f"El valor ingresado debe ser un número")

#####################TODO: TypeError

#? Al realizar operaciones con tipos incompatibles (ej. sumar una cadena con un número).
#! Frecuencia: Moderada.
#? Ejemplo típico: Procesar datos que vienen de múltiples fuentes.

# try:
#     resultado = 5 + "hola"             #? No se puede sumar un entero con una cadena
# except TypeError as e:
#     print(f"Error de tipo: {e}")       #? ---> Error de tipo: unsupported operand type(s) for +: 'int' and 'str'

#####################TODO: ZeroDivisionError

#? Al realizar divisiones y no validar previamente que el divisor no sea cero.
#!Frecuencia: Moderada.
#? Ejemplo típico: Calcular promedios o tasas en bases de datos o estadísticas.

# try:
#     numero = 10
#     divisor = int(input("Ingresa el divisor: "))  #? El usuario ingresa 0
#     resultado = numero / divisor
#     print(f"El resultado es {resultado}")
# except ZeroDivisionError as e:
#     print(f"Error: No se puede dividir por cero. Detalles: {e}")

#####################TODO: IndexError

#? Al trabajar con listas y no validar si el índice solicitado existe.
#! Frecuencia: Alta.
#? Ejemplo típico: Acceder a elementos de una lista de forma dinámica.

# try:
#     lista = ["manzana", "banana", "cereza"]
#     indice = int(input("Ingresa un índice de la lista: "))  #? El usuario ingresa 5, el cual no existe en la lista
#     print(f"El elemento es: {lista[indice]}")
# except IndexError as e:
#     print(f"Error: Índice fuera de rango. Detalles: {e}")

#####################TODO: KeyError

#? Al trabajar con diccionarios y no validar si una clave está presente.
#! Frecuencia: Alta.
#? Ejemplo típico: Procesar datos JSON o estructuras anidadas.

# try:
#     diccionario = {"nombre": "Juan", "edad": 25}
#     clave = input("Ingresa la clave que deseas buscar: ")  #? El usuario ingresa "altura", dicha clave no existe
#     print(f"El valor es: {diccionario[clave]}")
# except KeyError as e:
#     print(f"Error: La clave '{e}' no existe en el diccionario.")

##################### TODO: FileNotFoundError

#? Al intentar abrir archivos que podrían no existir.
#! Frecuencia: Alta (si trabajas con archivos).
#? Ejemplo típico: Leer configuraciones o datos desde archivos externo

# try:
#     archivo = open("archivo_inexistente.txt", "r")  #? Archivo inexistente
#     contenido = archivo.read()
#     print(contenido)
# except FileNotFoundError as e:
#     print(f"Error: No se encontró el archivo. Detalles: {e}")