"""
Escribir un programa que almacene las materias de un curso (por ejemplo filosofia, ciencias, deportes, español y matematicas)
en una lista, pregunte al usuario la nota que ha sacado en cada materia, y después las muestre por pantalla con el mensaje
En <materia> has sacado <nota> donde <materia> es cada una des las materias de la lista y <nota> cada una de las
correspondientes notas introducidas por el usuario.

"""
lista_Materias = ["filosofia","ciencias","deportes","español","matematicas"]
print("Inserte su nota de cada materias")
nota1 = input(lista_Materias[0])
nota2 = input(lista_Materias[1])
nota3 = input(lista_Materias[2])
nota4 = input(lista_Materias[3])
nota5 = input(lista_Materias[4])
print(lista_Materias[0], nota1, lista_Materias[1],nota2, lista_Materias[2], nota3, lista_Materias[3], nota4, lista_Materias[4], nota5)
    """listadeMaterias = ("filosofìa", "ciencias", "matematicas", "deportes")
diccionario = {}

print("nota:\n")

for materia in listadeMaterias:
    nota = input("materia: {}\n".format(materia))
    diccionario [materia] = nota

for materia in listadeMaterias:
    print("te sacaste", diccionario[materia], "en la materia", materia)
"""