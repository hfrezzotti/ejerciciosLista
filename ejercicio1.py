lista_numeros = [10, 45, 55, 76]

print(lista_numeros[3])

print(f"El valor mas pequeño en la lista es el {lista_numeros[0]}. El mas grande es el {lista_numeros[3]}")

lista_colores = ["Rojo", "Azul", "Verde", "Amarillo"]

print(lista_colores[1][2])
print(len(lista_colores))

lista_colores = ["Rojo", "Azul", "Verde", "Amarillo"]

lista_colores.insert(0, "Gris")
lista_colores.append("Rosa")
lista_colores.insert(3, "Naranja")
print(lista_colores)

lista_colores.pop(1)
lista_colores.pop(3)
lista_colores.pop(3)
print(lista_colores)

lista_nueva = lista_colores.copy()

print(lista_nueva)

lista_numeros = [10, 45, 356, 10, 10, 10, 46, 67,45, 10, 10, 43, 10, 65, 10, 10]

print(lista_numeros.count(10))

print(lista_numeros.index(356))

lista_numeros.sort()
print(lista_numeros)

lista_numeros.reverse()
print(lista_numeros)

print(len(lista_numeros))