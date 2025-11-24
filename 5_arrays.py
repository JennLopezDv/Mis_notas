
#!                                   __      _____   _____       __     __  __  _____ 
#!                                  /  \    |  __ \ |  __ \     /  \    \ \/ / |  ___|
#!                                 / /\ \   | |__) || |__) |   / /\ \    \  /  | |___ 
#!                                / ____ \  |  _  / |  _  /   / ____ \    ||   | __  |
#!                               / /    \ \ | | \ \ | | \ \  / /    \ \   ||    ___| |
#!                              /_/      \_\|_|  \_\|_|  \_\/_/      \_\  ||   |_____|

#TODO: CONCEPTO CLAVE:

#?En Python, los arrays (arreglos) son estructuras de datos que almacenan múltiples elementos del mismo tipo
#? en una secuencia ordenada. Aunque Python no tiene un tipo de datos de array nativo como en otros lenguajes
#? (por ejemplo, Java o C++), se pueden usar:

#! El módulo array
#? Permite trabajar con arrays de elementos del mismo tipo. Dicho tipo debe declararse cuando creo el array
#? Ojoooo, como se dijo antetiormente, los arrays solo almacenan datos del mismo tipo, 
#? a diferencia de las listas, las cuales sí aceptan datos combinados.

#TODO: NOTA IMPORTANTE: 
#? Nativamente, el módulo array no soporta multidimencionalidad, sí hay formas de trabajarlo, como un array de 
#? varias dimensiones, por ejemplo tridimensional, pero es engorroso, poso intuitivo y en realidad muy poco usado. 

#TODO: SINTAXIS Y PROCESO DE CREACIÓN:

#? 1. Lo primero que debo hacer es importar el módulo con la respectiva clase array (Llevan el mismo nombre)

# from array import array             #?Aquí ya se importó la clase array del módulo array

# mi_array = array('i', [1,2,3,2,5])  #? Se le da el nombre al array que deseo construir, que será igual a
#                                     #? utilizo la clase array y le paso dos argumentos, el primero, el tipo de datos
#                                     #? que tendrá el array y el segundo, es un iterable ordenado, como lista o tupla

# print(mi_array)                     #? ---> array('i', [1,2,3,2,5])



#TODO: NOTA!!!!
#! Aquí, todos los métodos de las listas son aplicables a los arrays, es decir:

# .append(x)	        #? Agrega un elemento al final del array.
# .extend(iterable)	    #? Agrega múltiples elementos desde un iterable.
# .insert(i, x)	        #? Inserta un elemento en la posición i.
# .remove(x)	        #? Elimina la primera aparición de x.
# .pop(i)	            #? Elimina y retorna el elemento en la posición i, si no agrego i, por dafecto elimina el último
# .index(x)	            #? Retorna el índice de la primera aparición de x.
# .reverse()	        #? Invierte los elementos del array.
# .count(x)	            #? Cuenta cuántas veces aparece x

#! Excepto tres métodos que no existen en los arrays:

#! .copy()
#? Se puede reemplazar usando slicing, tal cual como el de las listas, así:

# from array import array             #? Importamos la clase array del módulo array

# mi_array = array("i", [1,2,3,4,5])  #? Creo la variable mi_array y le asigno la clase array, pasando los argumentos
# copia_array = mi_array[:]           #? Creo la variable copia y le asigno un slice sin inicio ni fin, solo los 2 puntos
# print(f"{copia_array}")             #? ---> array('i', [1, 2, 3, 4, 5])

#? Otra forma más simple, es usando el mismo constructor de la clase array, así:

# from array import array             #? Importamos la clase array del módulo array

# mi_array = array("i", [1,2,3,4,5])  #? Creo la variable mi_array y le asigno la clase array, pasando los argumentos
# copia_array = array("i", mi_array)  #? Creo la variable copia y le asigno un nuevo array con su argumento de tipo
#                                     #? y el iterable es el array al que le quiero sacar copia
# print(f"{copia_array}")             #? ---> array('i', [1, 2, 3, 4, 5])


#! .clear()  
#? Se puede reemplazar por simplemente una nueva asignación de un array vacío a dicha variable, así:

# from array import array             #? Importamos la clase array del módulo array

# mi_array = array("i", [1,2,3,4,5])  #? Creo la variable mi_array y le asigno la clase array, pasando los argumentos
# mi_array = array('i')               #? Vuelvo a llamar la variable mi_array pero esta vez no le doy valores
# print(f"{mi_array}")                #? ---> array('i') Muestra solo el tipo de datos.


#?También se puede hacerlo usando la sentencia "del" y slicing, así:

# from array import array             #? Importamos la clase array del módulo array

# mi_array = array("i", [1,2,3,4,5])  #? Creo la variable mi_array y le asigno la clase array, pasando los argumentos
# del mi_array [:]                    #? Usamos del para eliminar y especificamos que eliminaremos desde el primero
#                                     #? hasta el último elemento al no poner índices. 
# print(f"{mi_array}")                #? ---> array('i') Muestra solo el tipo de datos.

#! .sort()
#? Tampoco existe una manera de organizar los array dando un orden como con sort en las listas, pero se puede
#? reemplazar usando directamente la función sorted, así:

# from array import array                           #? Importamos la clase array del módulo array

# mi_array = array('i', [5, 2, 9, 1, 7])            #? #? Creo la variable mi_array y le asigno la clase array, pasando los argumentos
# mi_array_ordenado = array('i', sorted(mi_array))  #? Crear un nuevo array ordenado
# print(mi_array_ordenado)                          #? ---> array('i', [1, 2, 5, 7, 9])

