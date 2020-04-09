# Metodos de listas

lista = ['Juan', 'Luis', 'Pedro']
print(lista)

# Nos regresa el índice del elemento que queremos buscar en una lista, si es que existe
luis_index = lista.index('Luis') # 1
print(luis_index)

# Agregar un elemento al final de la lista
lista.append('Pablito') # ['Juan', 'Luis', 'Pedro', 'Pablito']
print(lista)

# 'Extiende' una lista agregando al final todos los elementos de otra lista
lista_extra = ['Melo', 'Topi', 'Arturo']
lista.extend(lista_extra)
print(lista)

# Inserta un elemento a lista en el índice indicado
lista.insert(luis_index, 'Luis')
print(lista)

# Regresa el número de veces que encuentra un elemento en una lista
luis_count = lista.count('Luis')
print(luis_count)

# Eliminar el primer elemento de la lista que concuerde con el parametro recibido
lista.remove('Pablito')
print(lista)

# Elimina un elemento de la lista en el indice indica y regresa el elemento eliminado
# Si no se le pasa un índice a pop(), tomará por defecto -1, eliminando el último elemento de nuestra lista
elemento_arturo = lista.pop()
print(lista)
print(elemento_arturo)

lista.pop(luis_index)
print(lista)

# Invertir el orden de los elementos en una lista
lista.reverse()
print(lista)

# Ordena los elementos de una lista en un orden específico: Ascendente o Descendente
lista.sort(reverse=True)
print(lista)

# Regresa una copia de una lista
copy = lista.copy()
print(copy)

# Comprobamos que no se modificó la copia gracias a el método copy()
lista.append('Yagel')
print(lista)
print(copy)

# Elimina todos los elementos de una lista
lista.clear()
print(lista)