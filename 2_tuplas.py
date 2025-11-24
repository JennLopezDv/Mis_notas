
#!                              _______  _    _  _____   _          __      _____ 
#!                             |__   __|| |  | ||  __ \ | |        /  \    |  ___|
#!                                | |   | |  | || |__) || |       / /\ \   | |___ 
#!                                | |   | |  | ||  ___/ | |      / ____ \  | __  |
#!                                | |   | |__| || |     | |___  / /    \ \  ___| |
#!                                |_|    \____/ |_|     |_____|/_/      \_\|_____| 


#? Una tupla en Python es una estructura de datos inmutable que almacena una colección ordenada de elementos, 
#? los cuales pueden ser de tipos diferentes.\
#? Se definen utilizando paréntesis () y no se pueden modificar después de creadas, son inmutables.

#tupla = (1, 2, 3, 5)

#?Si bien puedo crear la tupla manual, así:
# tupla = (1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

#? También puede crearse por comprensión, así:
# tupla = tuple(i for i in range(1,6)) ---> (1,2,3,4,5)
#     ?Si quiero hacer una comprensión múltiple, por cada paréntesis, debo escribir la función tuple, así:
#     tupla = tuple(tuple(i for i in range(1,16))for j in range(5)) ---> ((1, 2, 3, 4, 5), (1, 2, 3, 4, 5), (1, 2, 3, 4, 5), (1, 2, 3, 4, 5), (1, 2, 3, 4, 5))

#! MÉTODOS DE LAS LISTAS: 
#? Las tuplas, al ser inmutables, tiene muy pocos métocos

#TODO: tupla.count(x) 
#?                 Este método cuenta cuántas veces el elemento (x) aparece en la tupla
#                  tupla = (1, 2, 3, 1, 5, 1, 2, 6, 10, 1)       
#                  print(tupla.count(1)) --->  4 #? porque el 1 está 4 veces en la tupla  

#TODO: tupla.index(x)  
#?                 Este método arroja el índice donde se aloja un elemento (x) dado, 
#?                 OJO, busca la primera aparición del elemento
#                  tupla = (1, 2, 3, 1, 5, 1, 2, 6, 10, 1)
#                  print(tupla.index(3)) --->  2 #? porque el elemento 3 está en el índica 2 de la tupla
#
#                  #! También puedo darle un rango de búsqueda así:    
#                  #! tupla.index(X, i, i) IGUAL A print(tupla.index(1, inicio de rango, fin de rango))
#                  #! El índice fin no cuenta dentro del rango de búsqueda, si no se da el fin del rango, va hasta el final
#                  tupla = (1, 2, 3, 1, 5, 1, 2, 6, 10, 1)
#                  print(tupla.index(1, 2, 9 )) ---> 3 #? Por que en el rango del índice 2, que es el elemento 3
#?                 hasta el índice 9 que es el número 1(No se cuenta, sino hasta el 10, se excluye a la derecha)
#?                 En ese rango, la primera aparición del elemento 1 está en el índice 3 de toda la lista. 

#!     ¡¡¡¡OJO!!!!!!

#? Si bien las listas son inmutables, hay algunos detalles a considerar con respecto a su uso. 

#TODO: Slicing: 
#?                 Esto sirve para crear una nueva tupla a partir de una existente, si deseo partes de dicha tupla
#                  tupla = (1,2,3,4,5,6,7,8,9,10)
#                  copia_tupla = tupla[2:6] #? No se tiene en cuenta el índice 6, como los rangos, sino que va hasta 5.
#                  print(tupla) ---> (1,2,3,4,5,6,7,8,9,10) 
#                  print(copia_tupla) ---> (3,4,5,6)

#TODO PUEDO CONVERTIR UNA LISTA A UNA TUPLA 

#?                 Si necesito hacer que una lista ya sea inmutable, 
#?                 puedo convertirla en una tupla con la función llamada tuple()
#                  TODO EJM:  
#                  lista=[i for i in range(15)] ---> [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14] #?Crea una lista
#                  mi_tupla = tuple(lista) ----> (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14) #? Crea una tupla a partir de la lista
#                  ! Puedo hacer slicing también de una lista y convertirlo en tupla así:
#                  lista=[i for i in range(15)] ---> [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#                  mi_tupla = tuple(lista[2:6]) ----> (2,3,4,5) #? Trajo los elementos de indice 2 a 6 convertidos en tupla


