##### Datos compuestos #####


#Comienza en la posición (indice) cero, que sería el elemento Jennifer.
#Lista:
lista = ["Jennifer", "López", "29", 1.63, True]
print(lista[3])


#Tuplas, NO SE PUEDEN MODIFICAR.
tupla = ("Jennifer", "López", "29", 1.63, True)
print(tupla[3])


#EJEMPLO 
lista [1] = "David"
print(lista)

# tupla [0] = "Carlos" #Marca error porque la tupla no se puede modificar.
# print(tupla)

# CONJUNTO (set) -- se puede modificar el conjunto en general, PERO NO un elemento en particular. 
conjunto = {"Jennifer", "López", "29", 1.63, True, "Jennifer"} #Imprime la info de manera aleatoria.
print(conjunto) #No permite mostrar por indice, debe ser el conjunto completo, y no imprime datos duplicados.


#Diccionario: Su estructura es, key : value
diccionario = {
    "nombre" : "Jennifer", 
    "edad" : 29,
    "apellido": "López",
    "dato_duplicado" : "Jennifer"
}

print(diccionario["nombre"])