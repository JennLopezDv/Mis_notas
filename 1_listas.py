
#!                              _      __  _____  _______      __      _____ 
#!                             | |    |  ||  ___||__   __|    /  \    |  ___|
#!                             | |    |  || |___    | |      / /\ \   | |___ 
#!                             | |    |  || __  |   | |     / ____ \  | __  |
#!                             | |___ |  | ___| |   | |    / /    \ \  ___| |
#!                             |_____||__||_____|   |_|   /_/      \_\|_____| 


#TODO: Ejemplo para todo el ejercicio de listas:
# lista = [1, 2, 3] #? Creo una lista manualmente
# mi_lista = [i for i in range(20, 32)] #?Esto, si quiero llenar una lista con un rango de valores

#TODO: TAMAÑO DE UNA LISTA
# lista = [1, 2, 3]
# len(lista) #? El tamaño de las listas se conoce con la función len(nombre de la lista)

#TODO: MOSTRAR LA LISTA, ACCESO A LA LISTA: print es para mostrar, pero puede haber alguna otra función en su lugar

# lista = [1, 2, 3]
# print(lista) #? Puedo acceder a toda la lista con un print solamente
# print(lista[0]) #? De esta manera puedo acceder al elemento 0 de la lista, o sea el primero. Resultado: 1
# print(lista[-1]) #?Esto muestra el último elemento de la lista, funciona también [-2] y así sucesivamente
# print(lista[0:-1]) #? De esta manera puedo acceder a un conjunto de valores dentro de mi lista indices 1 y 2 ---> [2,3]
# print(lista [1:]) #? Esto me trae todos los valores desee el indice 1, al no tener límite va hasta el final
# print(lista[-3:]) #? Esto me trae los últimos tres elementos, -3 trae el antepenultimo, al no tener límite, va al final

#TODO: OOOJOOOO, si uso la instrucción del  antes de todo esto, 
#TODO: lo que hace es borrar todo lo que está después de ese del
        #? """del""" es una instrucción del legunaje que solo elimina lo que esté al frente

#TODO:       EJEMPLO PRÁCTICO: 
# numero = 5
# del numero  #?Esto elimina la variable número.
# lista = [1, 2, 3]
# del lista  #? Esto elimina la lista
# del lista[0]  #? Esto elimina el valor que hay en el índice 0 de mi lista 
# del lista[1:3]  #?Esto elimina los valores que hay en los índices 1 y 2 de mi lista
# del lista[1:] #? Esto elimina los valores en los índices desde el 1 hasta el final pues no tiene rango final

#TODO: REEMPLAZAR LOS VALORES DE LA LISTA:

# lista = [0,1,2,3]
# !Puedo cambiar el valor de un índice así:
# lista[0] = 2  #? El resultado pasa de [1, 2, 3] a ---> [2, 2, 3]
# !También puedo reemplazar su valor por otra lista
# lista[0] = [4,5,6]
# !También puedo cambiar el valor de un índice por el de otro índice
# lista[0] = list[1]  #? El resultado pasa de [1, 2, 3] a ---> [2, 2, 3]
# !También puedo pedirle a un usuario que lo haga
# lista[0] = int(input("Ingrese el valor a reemplazar en el indice 0"))

#!|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#TODO: MÉTODOS EN LAS LISTAS:
#!Las siguientes instrucciones son métodos(.algo()) y se encargan de hacer algo con lo que hay antes del punto


#TODO: lista.append(x) 
                        #? Siendo x un valor cualquiera, este método agrega dicho valor al último índice de la lista
# lista = [1, 2, 3]
# lista.append(4) #----> [1,2,3,4]
    #TODO lista.append([x,y,z] 
                        #? OJO!!! También puedo agregar una lista, se agrega al último índice)
# lista = [1, 2, 3]
# lista.append([4,5,6]) #----> [1,2,3,[4,5,6]]
                        #!OJOOO, si quiero añadir otro valor a una lista dentro de una lista, debo hacerlo así:
# lista = [1,2,3,[4,5,6]]
# lista[3].append(7) #----> [1, 2, 3, [4, 5, 6, 7]] #?Fue al último índice de la sublista

#!|||||||||||||||||||||||||||||||||||||||||||||||||||
#TODO: lista.extend([x,y,z]) 
                #?Recibe un iterable como una lista [] conjunto {}, tupla () o rango: range(1, 3) y lo añade
                #? a la cola de la fila (SI O SI SOLO A LA COLA) 
                #! OJO, La diferencia entre .append y .extend es que .extend desempaqueta la lista y 
                #! añade cada uno de sus elementos al final como indiividuales, no como conjunto.
#TODO: Ejemplo práctico
# lista = [1, 2, 3]
# lista.extend([4,5,6]) #---> [1,2,3,4,5,6]

                #!PERO QUÉ PASA SI QUIERO AÑADIR LA LISTA DESEMPAQUETADA EN UN ÍNDICE QUE YO QUIERA Y NO AL FINAL?
                #? En ese caso no se unsa .extend ya que ese lo lleva al final, sino que se usa slice de listas, así:
                # lista[i:i] = [4,5,6] #? Aquí i (3) es el lugar donde quiero que se meta, sin borrar lo 
                                        #? que hay en ese indice. se reemplazan las i por el mismo número
#TODO: Ejemplo práctico
# lista = [1,2,3,7,8]
# lista[3:3] = [4,5,6]
# print(lista)
                

#!|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#TODO lista.insert(i,x)---> 
                #? La i (índice) indica el índice y la x, el valor a agregar
                #? La diferencia entre .append y .insert, es que .append agrega al último elemento de la lista,
                #? mientras que .insert, me pide ingresar un índice para poner mi elemento nuevo  
                #? en ese índice y correr los demás hacia la derecha.
#TODO: Ejemplo práctico:
#lista = [1,2,3]
#lista.insert(1,2) #---> [1,2,2,3]

                #TODO:!!! También puedo agregar una lista, usando list.insert(i,[x,y])
#TODO: Ejemplo práctico:
# lista = [1,2,3]
# lista.insert(1,[2,3]) #---> [1,[2,3],2,3]

#!|||||||||||||||||||||||||||||||||||||||||||||||||||
#TODO: list.remove(x) 
                #? Elimina la primera aparición del elemento x de la lista, si el elemento no existe, lanza un error
                #! OJO!!! Aquí, x no es el índice, sino el elemento en sí: 
#TODO: Ejemplo práctico: 
# lista_de_animales = ["caballo", "perro", "elefante", "simio", "caballo"]
# lista_de_animales.remove("caballo") #---> [ "perro", "elefante", "simio", "caballo"]
                #! OJO!! Elimina solo el primer caballo, no los demás caballo que existan.
                #?Si quiero eliminar todos los caballos, debo usar un ciclo while o for con if ASÏ:
# lista_de_animales = ["caballo", "perro", "elefante","caballo", "simio", "caballo"]
# while "caballo" in lista_de_animales: #? Mientras el elemento caballo se encuentre en la lista_de_animales
#     lista_de_animales.remove("caballo") #? Elimina "caballo"
# print(lista_de_animales) #---> ['perro', 'elefante', 'simio']

#!|||||||||||||||||||||||||||||||||||||||||||||
#TODO: list.sort() 

                #? Organiza la lista de forma ascendente si es número, de menor a mayor, si son String, de A a Z
             #TODO: Si es una lista de enteros, organiza del número menor al mayor
#TODO: Ejemplo práctico: 
# lista_enteros = [5,6,4,8,9,3,2]
# lista_enteros.sort() #----> [2, 3, 4, 5, 6, 8, 9]

             #TODO: Si es una lista de String, organiza de a hasta z
#TODO: Ejemplo práctico: 
# lista_String = ["manzana", "zanahoria", "yuca", "arroz", "pera"]
# lista_String.sort() #---> ['arroz', 'manzana', 'pera', 'yuca', 'zanahoria']

             #TODO: Si mi lista de String tiene alguno que está en mayúscula o inicia en ella, ese va primero
#TODO: Ejemplo práctico: 
# lista_String = ["manzana", "zanahoria", "Yuca", "arroz", "pera"] #? Yuca en mayúscula
# lista_String.sort() #---> ['Yuca', 'arroz', 'manzana', 'pera', 'zanahoria'] #? Yuca primero

             #TODO: key= !!!! Me permite personificar mi orden
                #!Quiero ignorar las mayúsculas y dar solo orden alfabético. debemos usar como parámetro lista.sort(key=str.lower)
#TODO: Ejemplo práctico: 
#lista_String = ["manzana", "zanahoria", "Yuca", "arroz", "pera"] #? Yuca en mayúscula
#lista_String.sort(key=str.lower) #---> ['arroz', 'manzana', 'pera', 'Yuca', 'zanahoria']
        #?Sí trae Yuca en mayúscula, pero no de primera, sino respetando orden alfabético
        
                #! Quiero ordenar por orden de tamaño (Cantidad de letras), lista.sort(key=len)
#TODO: Ejemplo práctico: 
#lista_String = ["manzana", "zanahoria", "yuca", "arroz", "pera"]
#lista_String.sort(key=len) #---> ['yuca', 'pera', 'arroz', 'manzana', 'zanahoria']

                #! OJOOOOOO hay más cosas para pasarle como parámetro con Key, pero no se verán aquí. 
                #TODO: Ejemplo  
                #lista.sort(key=abs) #?Ordena números por valor absoluto, sin tener en cuenta negativos
                #lista.sort(key=lambda x: (isinstance(x, str), x)) #? En listas mixtas pone números antes de letras 
             #TODO: reverse=True!!!! Revierte el orden que naturalmente tendría
                #!Quiero que me ordene de mayor a menor 
                        # lista = [1,2,3]
                        # lista.sort(reverse=True) ---> [3,2,1]
                #!Quiero de z A a
                        # lista_string = ["manzana", "zanahoria", "yuca", "arroz", "pera"]
                        # lista_string.sort(reverse=True) ---> ['zanahoria', 'yuca', 'pera', 'manzana', 'arroz'] #? De A a Z
             #TODO: key= , reverse=True !!!! Puedo conviner criterio de orden (key=) con el revere=True
                #!Valores absolutos de menor a mayor
                        # lista = [5,6,-8,9,-4]
                        # lista.sort(key=abs) ---> [-4,5,6,-8,9] #?Ordenada por valor absoluto, sin reverse (normal)
                #!Quiero valores absolutos pero de mayor a menor
                        #lista.sort(key=abs, reverse=True) ---> [9, -8, 6, 5, -4] #? Combinando key con reverse, me invierte el resultado
                #!Quiero me los String me los traiga por su tamaño, pero de mas largo a más corto
                        #lista_string =["manzana", "zanahoria", "yuca", "arroz", "pera"]
                        #lista_string.sort(key=len, reverse=True) ---> ['zanahoria', 'manzana', 'arroz', 'yuca', 'pera']

#!|||||||||||||||||||||||||||||||||||||||||||||||||
#TODO: lista.pop(i)  
                #? Elimina el elemento en el índice indicado, si no se indica el índice, elimina el último elemento
                #? y lo devuelve para su uso postrior si se requiere
                #TODO: Eliminando un índice especificado en el paréntesis
                        # lista = [1,2,3,4,5,6]
                        # lista.pop(2) ---> [1,2,4,5,6] #? Eliminó el 3, que estaba ubicado en el índice (2)
                #TODO: No pasando argumento al paréntesis
                        # lista = [1,2,3,4,5,6]
                        # lista.pop() ---> [1,2,3,4,5] #? Eliminó el 6, pues no se dio argumento en paréntesis. 
                #! PERO..... Qué se hace con el elemento que devuelve?
                    #?Puedo usarlo inmediatamente para mostrar lo eliminado o puedo asignarlo a una variable para después. 
                        #TODO: Para uso inmediato:
                                # lista = [1,2,3,4,5]
                                # print("El elemento eliminado es", lista.pop(2)) ---> El elemento eliminado es 3
                                # print(lista) ---> [1,2,4,5]
                        #TODO: Para uso posterior ---> Asigno el .pop a una variable
                                # lista = [1,2,3,4,5]
                                # eliminado = lista.pop(2) #? La variable eliminado puedo usarla muchas líneas abajo
                                # otra_lista = [1,2]
                                # otra_lista.append(elemento) ----> [1,2,3]     #? Tomó el elemento eliminado de lista
                                                                                #? y lo agregó al fina de otra_lista

#!||||||||||||||||||||||||||||||||||||||||
#TODO: lista.clear()  
                #? Borra todos los elementos de la lista, dejándola vacía
                # lista = [1,2,3,4,5,6]
                # lista.clear() ---> [] #? No elimina la lista, pero la vacía, elimina sus elementos

#!||||||||||||||||||||||||||||||||||||||||||||||
#TODO: lista.index(x) 
                #? Muestra el índice del primer elemento que coincida con x, es decir si ponemos 2, el primer 2 que
                #? encuentre, trae su índice(Su ubicación en la lista)
                # lista = [1,2,3,4,5,6]
                # indice = lista.index(2) ---> 1
                #TODO: OJOOO! Puedo establecer parámetros para determinar desde qué indice y hasta cual índice
                #TODO: quiero iniciar mi búsqueda. 
                # lista = [1,2,3,4,5,6]
                # indice = lista.index(x, i) #? aquí puse que me busque el índice de x desde el índice i
                # indice = lista.index(x, i, j) #? aquí puse que me busque el índice de x desde el índice i hasta el índice j
                # indice = lista.index(4, 2, -1) #? Muestra el índice donde está cuatro desde el índice 2 hasta el último
                #---> 3, Aunque hay un rango de índice 2 a -1, el índice donde está cuatro es traído de la lista completa

#!|||||||||||||||||||||||||||||||||||||||||||||
#TODO: lista.reverse() 
                #? INvierte el orden de mi lista
                # lista = [1,2,3,4,5,6]
                # lista.reverse() ---> [6,5,4,3,2,1]
                #TODO: Si quiero guardar el nuevo orden, pero en otra lista, sin alterar la original, este es el código:
                # lista = [1,2,3,4,5,6]
                # nueva_lista = lista[::-1]
                # print(lista) ---> [1,2,3,4,5,6]
                # print(nueva_lista) ---> [6, 5, 4, 3, 2, 1]

#!|||||||||||||||||||||||||||||||||||
#TODO: lista.count(x) 
                #? Devuelve la cantidad de veces que aparece x en la lista
                # lista = [1,2,3,4,2,5,6,2]
                # contador = lista.count(2)  #? En contador se guarda la cantidad de veces que aparece el 2 en mi lista
                # print(contador) ---> 3 #? El 2 está 3 veces en la lista 

#!|||||||||||||||||||||||||||||||||||||||||||
#TODO: lista.copy()
                #? Crea una copia de la lista
                # copia = lista.copy()
                # print(copia) ---> [1,2,3,4,5,6]
                #TODO: Ojooo, no es lo mismo usar .copy que asignar la variable lista a otra variable copia, si hago eso,
                #TODO: lo que hago es apuntar a la misma variable y un cambio en la copia, cambia la lista original.
                # lista = [1,2,3,4,5,6]
                # copia = lista #!Esto no me sirve si hago cambios a alguna de las dos listas, ambas reciben los cambios
                #A menos que lo haga así: Llamado slicing, esto sí hace una copia superficial de la lista, tal como copy
                # lista = [1,2,3,4,5,6]
                # copia = lista[:]
                #! OJOOOOO Con esta forma puedo copiar cierta parte de otra lista
                # lista = [1,2,3,4,5,6]
                # copia_lista_parcial = lista[2:4] ---> [3,4]
                

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! COMPRENSIÓN DE LISTAS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

#? Para llenar listas, hay una forma en la que puedo hacerlo en un solo renglon, se llamada comprensión de lista y
#? funciona con la siguiente lógica:
                # nueva_lista = [operación for elemento in iterable]
                # operación: Qué quieres hacer con cada elemento.
                # elemento: Cada valor que tomas del iterable.
                # iterable: Algo que puedes recorrer, como una lista o range().

                        #Así:

                        #?Método tradicional: CON CICLO FOR
                        # mi_lista = []
                        # for i in range(10):
                        #     mi_lista.append(i)

                        #? Con comprensión de listas
                        # mi_lista = [i for i in range(10)]

                        # print(mi_lista) ---> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                        
                        #? También puede hacerse una bidimencional y hasta tridimencional
                        # mi_lista = [[[i**2 for i in range(5)if i % 2 == 0]for j in range(5)]for k in range(5)]
                        # print(mi_lista)
                        
                        #?Resultado:
                        # [[[0, 4, 16], [0, 4, 16], [0, 4, 16], [0, 4, 16], [0, 4, 16]], [[0, 4, 16], 
                        # [0, 4, 16], [0, 4, 16], [0, 4, 16], [0, 4, 16]], [[0, 4, 16], [0, 4, 16], [0, 4, 16], 
                        # [0, 4, 16], [0, 4, 16]], [[0, 4, 16], [0, 4, 16], [0, 4, 16], [0, 4, 16], 
                        # [0, 4, 16]], [[0, 4, 16], [0, 4, 16], [0, 4, 16], [0, 4, 16], [0, 4, 16]]]
                        
                        # Eso crea una lista tridimencional con listas de 5 elementos cada sublista, pero al tener un if
                        # solo tiene en cuenta los elementos cuyo resto al dividir entre 2, sea 0, es decir, los pares.
                        #Así pues, queda en realidad de tres elementos cada uno.







