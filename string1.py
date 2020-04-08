#Este metodo nos permite ingresar a la posicion de una cadena de caracteres.

#string = "Te amo mucho Cangurito"
string = input("Escribe un mensaje: ")
primer_letra = string[0] #Nos muestra la primera letra del texto
longitud = len(string)  #Nos muestra la longitud del texto
ultimo_valor = string[len(string) - 1] #string[-1] es lo mismo que lo anterior y nos muestra el ultimo valor del texto

print(primer_letra)

#Slices (Rebanada)
mensaje = "Estoy aprendiendo a programar en python"
slicito1 = mensaje[17:] #Nos muestra el texto a partir de la posicion ingresada
slicito2 = mensaje[:19] #Nos muestra las primeras 18 posiciones del texto
slicito3 = mensaje[6:9] #Nos muestra el valor que se encuentra entre la posicion 6 y 9
print(slicito1)
print(slicito2)
print(slicito3)

splited = mensaje.split("e") #Nos muestra el texto acorde a la variable que definamos entre las comillas ""
print(splited)
print(splited[3])

#Listas
lista = ["Palabra", 3, 5.43, True, ["Soy", "Otra", "Lista"]]
print(lista[4][1]) #De esta forma ingresamos a la posicion de una lista anidada (Metodo resumido)

lista_anidada = lista[4] #Metodo
print(lista_anidada[1])         #Largo

print(lista)

#Quitamos el ultimo elemento de la lista
lista.pop()
nueva_lista = lista.pop() #Te permite ingresar al ultimo elemento de una lista
print(lista)

#Agregamos un elemento a la lista
lista.append(False) #Agrega un elemento a nuestra lista
print(lista)


lista_string = ["1", "2", "3", "4"]
separador = "+"

#join toma una lista de string forzosamente y lo convierte a un string con base en la variable que ingresemos
lista_joineada = separador.join(lista_string)
print(lista_joineada)


