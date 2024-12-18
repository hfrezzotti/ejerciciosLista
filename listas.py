#Serie de ejercicios para practicar manejo de listas en Python

lista_colores = ["Rojo", "Verde", "Azul", "Naranja", "Marron", "Fucsia"]

print(lista_colores)
print(lista_colores[0])
print(lista_colores[0:2])
print(lista_colores[0][0])
print(f"El color favorito de Julian es: {lista_colores[2]}")
print(lista_colores[-1]) #inversa

lista_colores[0] = "Naranja"
print(lista_colores)

#Agregar al final
lista_colores.append ("Amarillo")
#Agregar en un lugar específico
lista_colores.insert(0, "Dorado")

print(lista_colores)

#si queremos vaciar la lista aplicamos clear
#si queremos eliminar algo en específico usamos POP y damos nota del indice
#si queremos eliminar elemenos por su nombre usamos remove

#para copiar una lista se hace de la siguiente manera

lista_nueva = lista_colores.copy

print(lista_colores)
print(lista_nueva)

#como puedo saber cuantas veces se repite un elemento en una lista?

print(lista_colores.count("Rojo"))

#para reversas una lista se usa el metodo inverse

lista_colores.reverse()

#ordenar alfabeticamente las listas

lista_colores.sort()

#si lo queremos en orden descendente

lista_colores.sort(reverse= True)

#para unir listas

lista_colores.extend(lista_nueva)

#las tuplas no pueden modificarse, las listas si

colores = ("rojo", "amarillo", "azul")

#no se pueden tocar

print(len(colores))