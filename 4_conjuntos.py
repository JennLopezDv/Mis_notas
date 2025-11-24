
#!                          _____   ___   _    _  _______  _    _  _    _  _______   ___   _____ 
#!                         / ____| / _ \ | \  | ||__   __|| |  | || \  | ||__   __| / _ \ |  ___|
#!                        | |     | | | ||  \ | |   | |   | |  | ||  \ | |   | |   | | | || |___ 
#!                        | |     | | | ||   \| |   | |   | |  | ||   \| |   | |   | | | || __  |
#!                        | |____ | |_| || |\   | __| |   | |__| || |\   |   | |   | |_| | ___| |
#!                         \_____| \___/ |_| \__||____/    \____/ |_| \__|   |_|    \___/ |_____|

#TODO: DEFINICIÓN:
#? Un conjunto en Python es una colección no ordenada de elementos únicos. Se basa en el concepto matemático de 
#? conjuntos y es útil para operaciones como intersecciones, uniones y diferencias entre colecciones de datos.

#TODO: CARACTERÍSTICAS PRINCIPALES:

#? Elementos únicos: No permite duplicados; si intentas añadir un elemento que ya existe, no se incluirá de nuevo.

#? No ordenados: Los elementos no tienen un índice como en las listas.

#? Mutables: Puedes añadir o eliminar elementos, pero sus elementos deben ser inmutables 
#? (como números, cadenas o tuplas).


#TODO: CUÁNDO USARLOS
#? 1. Eliminar duplicados de una colección.
#? 2. Verificar pertenencia rápidamente: Las búsquedas en conjuntos son más rápidas que en listas.
#? 3. Operaciones matemáticas como unión, intersección, diferencia, etc.
#? 4. Comparaciones entre conjuntos de datos.




#TODO: SINTAXIS:

#? Con un conjunto vacío
# conjunto_vacio = set()

#? Con elementos iniciales
# conjunto = {1, 2, 3, 4}

                            #TODO: Eliminar duplicados de una lista:
#                           lista = [1, 2, 2, 3, 4, 4]              #? Esta es una lista simple. 
#                           conjunto = set(lista) ---> {1, 2, 3, 4} #? Creo un conjunto y le asigno la lista
#                                                                   #? se usa la palabra clave set(nombe_lista)
#                                                                   #? lo cual elimina duplicados. 

                            #TODO: Comprobar si un elemento está en el conjunto:
#                            conjunto = {1, 2, 3, 4}         #? Creo un conjunto

#                            print(2 in conjunto) ---> True  #? Imprimo si 2 está en el conjunto, arroja True
#                            print(5 in conjunto) ---> False #? IMprimo si 5 está en el conjunto, arroja false



                            #TODO: MÉTODOS DE LOS CONJUNTOS:


#!          .add(elemento)
#? Agrega un elemento al conjunto. Si ya existe, no lo agrega de nuevo.

# conjunto = {1,2,3,4,5}          #? Aquí se crea el conjunto

# conjunto.add(5)                 #? Aquí se intenta añadir 5 al conjunto, como ya existe, no se agrega nada. 
# conjunto.add(6)                 #? Aquí se intenta añadir 6 al conjunto, como no existe, se añade con éxito.
# print(conjunto)                 #? Mostraría {1,2,3,4,5,6} No se repite el 5 porque no se añadió pues ta existía.


#!          .remove(elemento)
#? Elimina un elemento. Lanza un error si el elemento no existe.

# conjunto = {1,2,3,4,5}          #? Aquí se crea el conjunto

# conjunto.remove(5)              #? Se elimina el elemento 5 del conjunto. 
# conjunto.remove(6)              #? Se lanza una KeyError porque el 6 no existe en el conjunto. 
# print(conjunto)                 #? Ahora mostraría ---> {1,2,3,4}


#!          .discard(elemento)
#? Elimina un elemento. No lanza error si el elemento no existe.

# conjunto = {1,2,3,4,5}          #? Aquí se crea el conjunto

# conjunto.discard(5)             #? Se elimina el elemento 5 del conjunto. 
# conjunto.discard(6)             #? Este método no lanza error aunque el 6 no exista, solo no hace nada.  
# print(conjunto)                 #? Ahora mostraría ---> {1,2,3,4}


#!          .pop()
#? Elimina y retorna un elemento aleatorio. Lanza error si el conjunto está vacío.

# conjunto = {1,2,3,4,5}          #? Aquí se crea el conjunto
# eliminado = conjunto.pop()      #? Se crea la variable eliminado y se le asigna el elemento eliminado con conjunto.pop
# print(f"Se eliminó {eliminado}, nuevo conjunto es {conjunto}") #? ---> Se eliminó 1, nuevo conjunto es {2, 3, 4, 5}


#!          .clear()	
#? Vacía el conjunto, por lo que no se elimina el conjunto, sino que queda vacío.

# conjunto = {1,2,3,4,5}          #? Aquí se crea el conjunto
# conjunto.clear()                #? Aquí, se vacía el conjunto, eliminando todos los elementos. 
# print(f"{conjunto}")            #? Imprime un conjunto ya vacío ---> set()


#TODO: NOTA MUYYYY IMPORTANTE: Los siguiente métodos claramente son aplicables a los conjuntos (set), pero hay 
#TODO: otro tipo de conjunto muy importante llamado frozenset, los cuales son inmutables, por lo que los métodos
#TODO: mencionados anteriormente arriba, no son aplicables a los FROZENSET, ya que lo modifican y lanzaría un
#TODO: error de tipo de dato, pues no es hashable, osea no se le puede asignar un valor único ya que puede cambiar. 
#TODO: Los métodos a continuación sí se aplican a los frozenset, ya que no modifica el conjunto en sí, si no que 
#TODO: Retornan un nuevo conjunto o un booleano.  

                                            #TODO: Sintaxis
                                                    # conjunto = frozenset({1,2,3,4,5,6})
                                                    #? O dentro del dicho conjunto puede ir cualquier iterable
                                                    #? como tupla, lista o un conjunto normal como en el ejemplo. 
#! El resto de los métodos de aquí en adelante son aplicaboles tanto a un conjunto normal, mutable, como al frozenset()

#!          .union(otro_conjunto)
#? Retorna un nuevo conjunto con todos los elementos únicos de los conjuntos unidos, aquellos que estén repetidos
#? no son tomados en cuenta. 


# conjunto_1 = {1,2,3}            #? Se crea el primer conjunto
# conjunto_2 = {4,5,6}            #? Se crea el segundo conjunto

# union = conjunto_1.union(conjunto_2) #? A la variable union, se le asigna la union de ambos conjunos.
# print(f"{union}")

#? Ojo!!! también se pueden unir los conjuntos que yo quiera así:

# conjunto_1 = {1,2,3}
# conjunto_2 = {4,5,6}
# conjunto_3 = {7,8,9}

# union = conjunto_1.union(conjunto_2).union(conjunto_3)  #? 1ra forma, más larga
# union2 = conjunto_1.union(conjunto_2, conjunto_3)       #? 2da forma, mucho mejor
# print(f"{union2}")

                                    #! Importante!!!!!!!!!
                                    #? Esto mismo se puede lograr, usando simplemente el operador | así:

# conjunto_1 = {1,2,3}
# conjunto_2 = {4,5,6}
# union = conjunto_1 | conjunto_2 |conjunto_3  #? En lugar del método, se usa el operador | más sencillo
# print(f"{union}")                            #? ---> {1, 2, 3, 4, 5, 6, 7, 8, 9}


#!          .intersection(otro_conjunto)	
#? Retorna un nuevo conjunto con los elementos comunes, es decir, en una variable asigno el resultado de la
#? de la interesección entre varios conjuntos, y esa variable se combertirá en un nuevo conjunto con los elementos
#? que se encuentren en todos los conjuntos. 

# conjunto_1 = {1,2,3,4}                                      #? Primer conjunto creado
# conjunto_2 = {3,4,5,6}                                      #? Segundo conjunto creado
# conjunto_3 = {5,6,8,4,3}                                    #? Tercer conjunto creado

# repetidos = conjunto_1.intersection(conjunto_2, conjunto_3) #? En la variable "repetidos" se aplica el método
#                                                             #? intersection al primer conjunto,
#                                                             #? pasando como argumentos los otros dos conjuntos
#                                                             #? solo se ejecutará sobre los elementos en común
#                                                             #? en todos los conjuntos, si bien, el elemento 5
#                                                             #? está en conjunto_2 y conjunto_3, no está en
#                                                             #? conjunto_1, por lo que no se tiene en cuenta. 

# print(f"Los valores repetidos en los conjuntos son {repetidos}")    #? ---> {3, 4} Solo el 3 y el 4 se repetían en
#                                                                     #? todos los conjuntos. 


#!          .difference(otro_conjunto)	
#? Retorna un nuevo conjunto con los elementos que están en este conjunto, pero no en el otro, es decir, solo
#? me retornará los elementos que están en mi conjunto principal que no se encuentran en el conjunto pasado como
#? argumento. Puede tomar más de un argumento, osea la comparación puede hacerse con varios conjuntos. 

# conjunto_1 = {1,2,3,4}                                      #? Primer conjunto creado
# conjunto_2 = {3,4,5,6}                                      #? Segundo conjunto creado
# conjunto_3 = {2,5,6,8,4,3}                                   #? Tercer conjunto creado

# diferencia = conjunto_1.difference(conjunto_2, conjunto_3)

# print(f"Los elementos que solo están en el primer conjunto y no en el segundo ni el tercero son: {diferencia}")


#!          .symmetric_difference(otro_conjunto)	
#? Retorna un conjunto con elementos que están en uno u otro, pero no en ambos.  OJOOO!! Este solo toma un argumento
#? O sea que la comparación puede hacerse solo con un conjunto a la vez

# conjunto_1 = {1,2,3,4}                                      #? Primer conjunto creado
# conjunto_2 = {3,4,5,6}                                      #? Segundo conjunto creado

# diferencia = conjunto_1.symmetric_difference(conjunto_2)  #? En la variable "diferencia" se almacenarán los 
#                                                           #? elementos que son únicos en cada conjunto, bien sea
#                                                           #? del primer conjunto o del segundo, los elementos que
#                                                           #? se repitan entre los conjuntos, no serán guardados en
#                                                           #? esta nueva variable.

# print(f"Los elementos que no coinciden entre estos conjuntos son: {diferencia}") #? ---> {1, 2, 5, 6}


#!          .issubset(otro_conjunto)	
#? Retorna True si todos los elementos están en el otro conjunto.

# conjunto_1 = {1,2,3,4}                                      #? Primer conjunto creado
# conjunto_2 = {1,2,3,4,5,6,8,7,9}                            #? Segundo conjunto creado

# print(f"{conjunto_1.issubset(conjunto_2)}") #? ---> True. porque todos los elementos del conjunto_1 están en conjunto_2
# print(f"{conjunto_2.issubset(conjunto_1)}") #? ---> False. Aquí evaluamos al contrario, preguntando si
#                                             #? los elementos del conjunto_2 estaban en el conjunto_1 y es falso
#                                             #? porque en el conjunto 1 no están los elementos 5,6,7,8,9


#!          .issuperset(otro_conjunto)	
#? Este es todo lo contrario al anterior, pues este evalúa si el conjunto que invoca el método contiene todos los
#? elementos del conjunto que paso como argumento a al método. Retorna True si sí están o False si no. 

# conjunto_1 = {1,2,3,4}                                      #? Primer conjunto creado
# conjunto_2 = {1,2,3,4,5,6,8,7,9}                            #? Segundo conjunto creado

# print(f"{conjunto_1.issuperset(conjunto_2)}") #? ---> False. porque evalúa si conjunto_1 contiene dentro de sí, todos
#                                               #? los elementos del conjunto_2 y no los contiene todos.

# print(f"{conjunto_2.issuperset(conjunto_1)}") #? ---> True. Aquí evaluamos al contrario, preguntando si
#                                               #? el conjunto_2  contiene en sí, a todos los elementos del conjunto_1 
#                                               #? y eso es cierto. 


#!          .isdisjoint(otro_conjunto)	
#? Retorna True si no tienen elementos en común. Es técnicamente una comparación, si no coinciden en lo absoluto,
#? arroja True, si tienen almenos un elemento en común, arrojará False. 

# conjunto_1 = {1,2,3,4}                                      #? Primer conjunto creado
# conjunto_2 = {5,6,7,8}                                      #? Segundo conjunto creado
# conjunto_3 = {1,2,3,8}                                      #? Tercer conjunto creado

# print(f"{conjunto_1.isdisjoint(conjunto_2)}")   #?---> True, ningún elemento de conjunto_1 está en el conjunto_2
# print(f"{conjunto_2.isdisjoint(conjunto_3)}")   #?---> False, El elemento 8 se repite en ambos conjuntos, por lo que
#                                                 #? estos conjuntos no son distintos. 

#!          .copy()	
#?	Retorna una copia del conjunto.

# conjunto_1 = {1,2,3,4,5,6}                                      #? Creo el conjunto original

# copia_del_conjunto = conjunto_1.copy()                          #? En la variable copia, guardo el resultado de
#                                                                 #? lo que dará conjunto_1.copy() que es una copia
#                                                                 #? exacta del conjunto_1
                                                                
# print(f"La copia del conjunto_1 es: {copia_del_conjunto}")      #? ---> La copia del conjunto_1 es: {1, 2, 3, 4, 5, 6}