cadena1 = "Hola, soy Jenn"
cadena2 = "Soy una programadora"
cadena3 = "quiero aprender a programar"
cadena4 = "123quieroaprenderaprogramar"

#MÉTODOS PARA CONVERTIR UN VALOR:
resultado1 = cadena1.upper() #Método para convertir el valor de la variable en MAYÚSCULA.
resultado2 = cadena2.lower() #Método para convertir el valor de la variable en minúscula.
resultado3 = cadena3.capitalize() #Método para convertir la primer letra en mayúsula.

#MÉTODOS PARA BUSCAR UN VALOR: Importante: Python es casesencity.
resultado4 = cadena1.find("s") # En caso de no encntrar coincidencias arroa -1. El resultado que arroja es la posición. 
resultado5 = cadena1.index("J") #Realiza la misma busqueda que find(), pero cuando no encuentra coincidencias lanza una excepción. 

#MÉTODOS PARA CONSULTAR SI LOS DATOS SON NÚMERICOS O ALFANÚMERICOS:
resultado6 = cadena2.isnumeric() #Si el dato es númerico arroja True, sino False.
resultado7 = cadena4.isalpha() #solo retorna True si todos los caract de la cadena son letras A-Z. No permite números ni espacios ni símbolos.. 
resultado8 = cadena4.isalnum() # Devuleve True si la cadena contiene caract alfanúmericos. No se aceptan espacios.

print(resultado8)