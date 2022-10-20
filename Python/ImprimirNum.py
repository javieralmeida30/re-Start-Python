"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

"""
lista = list(range(1, 11))
print(lista)
for i in range(len(lista) - 1, -1, -1):
    print(lista[i], sep=',')