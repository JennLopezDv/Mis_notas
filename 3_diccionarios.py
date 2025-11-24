
#!              ____   __   _____   _____  __   ___   _    _      __      _____   __   ___   _____  
#!             |  _ \ |  | / ____| / ____||  | / _ \ | \  | |    /  \    |  __ \ |  | / _ \ |  ___| 
#!             | | | ||  || |     | |     |  || | | ||  \ | |   / /\ \   | |__) ||  || | | || |___  
#!             | | | ||  || |     | |     |  || | | ||   \| |  / ____ \  |  _  / |  || | | || __  | 
#!             | |_| ||  || |____ | |____ |  || |_| || |\   | / /    \ \ | | \ \ |  || |_| | ___| | 
#!             |____/ |__| \_____| \_____||__| \___/ |_| \__|/_/      \_\|_|  \_\|__| \___/ |_____| 

#TODO: DEFINICIÓN:

#? Un diccionario es una estructura de datos en Python que almacena pares de clave: valor. 
#? Cada clave es única y se utiliza para acceder a su valor asociado. Los diccionarios son mutables, 
#? lo que significa que sus contenidos pueden cambiarse después de su creación.


#TODO: SINTAXIS: 
#! Los diccionarios se definen con llaves

# diccionario = {} #? Puedo crear un diccionario vació para llenar luego

diccionario = {               #? Primero se define el nombre del diccionario, que será igual a lo que hay entre
    "clave1": "valor1",       #? las llaves, se puede ver que el diccionario al igual que un diccionario común
    "clave2": "valor2",       #? consta de una palabra clave y su valor correspondiente, como un diccionario
    "clave3": "valor3"        #? Ingles - Español. La clave a la izquierda, el valor a la derecha después de :
}

#! LAS CLAVES DE UN DICCIONARIO SON ÚNICAS E INMUTABLES:
#? Las claves deben ser String, enteros, números flotantes o tuplas.

#! PERO LOS VALORES SÍ PUEDEN CAMBIAR Y TENER CUALQUIER VALOR QUE QUIERA ASIGNARLES:
#? Los valores sí pueden ser String, números, funciones, tuplas, listas, flotantes y cualquier otro tipo de dato

#TODO: Ejemplo de un diccionario simple:

# mi_diccionario = {
#     "nombre": "Juan",
#     "edad": 25,
#     "ciudad": "Madrid"
# }




#                         #TODO: PARA ACCEDER A LOS VALORES DE UNA CLAVE
# mi_diccionario["nombre"]      #? Para acceder al valor correspondiente a esa clave ---> Juan
# mi_diccionario.get("nombre")  #? Arroja el mismo resultado, acceso al valor de la clave ---> Juan
# print(mi_diccionario.get("universidad", "Dato no guardado"))  #!OJO CON ESTO: 
                                                            #? Ojo aquí, mi diccionario, en realidad, no tiene
                                                            #? una clave llamada universidad, por lo que puedo
                                                            #? darle un valor por defecto, pero, ese valor no queda
                                                            #? guardado, solo se mostrará en esa consulta.

#                                   #TODO: PARA MODIFICAR UN DICCIONARIO
# mi_diccionario["edad"] = 26               #? Cambia el valor correspondiente a la clave edad, pasa de 25 a 26
# mi_diccionario["profesión"] = "Ingeniero" #? Agrega una nueva clave con su respectivo valor a mi diccionario
# del mi_diccionario["ciudad"]              #? Esto borra la clave y su valor correspondiente. 

#                                #TODO: MÉTODOS A USAR CON LOS DICCIONARIOS

#!          .get(clave)     .get(clave, valor_por_defecto)
#? Este se usa para adquirir el valor correspondiente a una clave que es la que se pone entre los paréntesis
#? Si no existe el resultado es None, pero puedo ponerle un resultado por defecto si no existe ticha clave
#? En el ejemplo, c no existe como clave, pero para que no me diga None, le pongo un valor por defecto

#TODO: Ejemplo práctico:

# diccionario = {
#     "a": 1,
#     "b": 2
#     }

# print(diccionario.get("a"))                         #? Output: 1
# print(diccionario.get("b"))                         #? Output: 2
# print(diccionario.get("c"))                         #? Output: None
# print(diccionario.get("d", "Clave no encontrada"))  #? Output: Clave no encontrada

#||||||||||||||||||||||||||||||||||||||||||||||||||||||

#!           diccionario.keys()
#? Devuelve una vista con todas las claves del diccionario.

#TODO: Ejemplo práctico:

# diccionario = {
#     "a": 1, 
#     "b": 2
#     }

# print(diccionario.keys())  #? Output: dict_keys(['a', 'b']) | Arroja horizontalmente solo las claves del diccionario

#||||||||||||||||||||||||||||||||||||||||||||||||||||

#!          diccionario.values()
#? Devuelve una vista con todos los valores del diccionario como lista.

#TODO: Ejemplo práctico:

# diccionario = {"a": 1, "b": 2}
# print(diccionario.values())  #? Output: dict_values([1, 2]) | Arroja solo los valores del diccionario, no las claves

#||||||||||||||||||||||||||||||||||||||||||||||||||||

#!          diccionario.items()

#? Devuelve una vista con pares clave-valor como tuplas.

#TODO: Ejemplo práctico:

# diccionario = {"a": 1, "b": 2}
# print(diccionario.items())               #? Output: dict_items([('a', 1), ('b', 2)])

#||||||||||||||||||||||||||||||||||||||||||||||||||||       

#!          diccionario.update(otro_diccionario)
#? DE esta manera puedo fusionar dos diccionarios, los pares (clave-valor) del diccionario entre el paréntesis 
#? se insertan en el diccionario que está invocando el método, si hay claves que ya existen en el diccionario
#? principal, su valor se reemplaza por el valor correspondiente a esa clave en el diccionario en paréntesis. 

#TODO: Ejemplo práctico, creando el diccionario directamente en los paréntesis:

# diccionario = {"a": 1}
# diccionario.update({"b": 2, "a": 3})
# print(diccionario)  # Output: {'a': 3, 'b': 2}

#TODO: Ejemplo práctico, ingresando otro diccionario previamente creado en los paréntesis:

# mi_diccionario = {"a": 1}                   #? Diccionario inicial

# otro_diccionario = {"b": 2, "a": 3}         #? Segundo diccionario

# mi_diccionario.update(otro_diccionario)     #? No creo el diccionario sino que meto en paréntesis uno ya creado
# print(mi_diccionario)                       #? Ouput:{'a': 3, 'b': 2}

#|||||||||||||||||||||||||||||||||||||||||||||||||||| 

#!          dict.pop(clave[, valor_predeterminado])
#? Elimina una clave y devuelve su valor. Si la clave no existe, devuelve el valor predeterminado si se especifica, 
#? o lanza un error KeyError.

diccionario = {                                     #?Creo el diccionario
    "a": 1,
    "b": 2
    }
print(diccionario.pop("a"))  # Output: 1            #? Aplico el método para eliminar la clave a y muestra el valor eliminado
print(diccionario)  # Output: {'b': 2}              #? Ahora el diccionario solo tiene el par clave-valor 'b': 2
print(diccionario.pop("c", "Clave no existente"))   #? Si intento eliminar c, no existe, para evitar un error
                                                    #? tipo keyerror, le asigno el valor por defecto que sea mostrado
                                                    #? en este caso el valor es "Clave no existe"

#|||||||||||||||||||||||||||||||||||||||||||||||||||| 

#!          dict.popitem()
#?Elimina y devuelve el último par clave-valor insertado como una tupla 
#? (en versiones ≥ 3.7, respeta el orden de inserción).

#TODO: Ejemplo práctico:

diccionario = {"a": 1, "b": 2, "c": 3}
print(diccionario.popitem())  # Output: ('c', 3)    #? Elimina el último clave valor ingresado
print(diccionario.popitem)  # Output: ('b': 2)      #? Elimina de nuevo el último y lo devuelve
print(diccionario)  # Output: {'a': 1}              #? Solo quedó la primera inserción. 

#|||||||||||||||||||||||||||||||||||||||||||||||||||| 

#!          dict.clear()
#?Elimina todos los elementos del diccionario.

#TODO: Ejemplo práctico:

diccionario = {"a": 1, "b": 2}          #? Creo el diccionario
diccionario.clear()                     #? Con este método elimino todos los elementos del diccionario
print(diccionario)  # Output: {}        #? EL resultado es un diccionario vacío.

#||||||||||||||||||||||||||||||||||||||||||||||||||||

#!          dict.copy()
#? Devuelve una copia superficial del diccionario.

#TODO: Ejemplo práctico:

diccionario = {"a": 1, "b": 2}                          #? Creo el diccionario
nuevo_diccionario = diccionario.copy()                  #? Creo una variable nueva y le asigno el dic.copy()
print(nuevo_diccionario)  # Output: {'a': 1, 'b': 2}    #? Ahora esa variable es un diccionario copia del inicial

#||||||||||||||||||||||||||||||||||||||||||||||||||||

#!          dict.fromkeys(iterable[, valor])
#?Crea un nuevo diccionario con claves de un iterable y valores opcionales iguales para todas las claves.

claves = ["a", "b", "c"]                    #? Creo una lista de Strings con las letras a b c
diccionario = dict.fromkeys(claves, 0)      #? Creo una variable a la que le asigno el nuevo diccionario que se crea 
                                            #? del método de la clase dict.fromkeys(claves, 0) el primer argumento
                                            #? asigna las claves que vienen de la lista llamada claves, el segundo
                                            #? argumento determina el valor que se repetirá en todas las claves
print(diccionario)  # Output: {'a': 0, 'b': 0, 'c': 0} #? Se observa todas las letras con un mismo valor

#||||||||||||||||||||||||||||||||||||||||||||||||||||

#!          diccionario.setdefault(clave[, valor_predeterminado])
#? Este método permite validar si existe una clave en el diccionario, si existe la muestra, como si fuera un .get
#? Si no existe, permite darle un valor determinado y tanto la clave buscada como el valor asignado se agregarán
#? al diccionario. 

diccionario = {"a": 1}                              #? Creo el diccionario con un solo par clave-valor
print(diccionario.setdefault("b", 2))  # Output: 2  #? Consulto si existe la clave b y le asigno un valor si no existe 
print(diccionario)  # Output: {'a': 1, 'b': 2}      #? La clave no existía, por lo que se inserta al diccionario.
                                                    #! Si la clave existiera, simplemente muestra su valor sin 
                                                    #! cambiarlo por el predeterminado en el método.


