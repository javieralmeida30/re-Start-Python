#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
#y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase 
#en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
#DiccEnglishSpanish = []
#Condition = "Yes"
DiccEspanolIngles = []
Condicion = "Si"
while Condicion == "Si":
    Palabra = str(input("Palabra en español:Palabra en ingles"))
    DiccEspanolIngles.append(Palabra)
    Condicion = str(input("Añadir más palabras?: Si/No"))
print(DiccEspanolIngles)


"""
while Condition == "Yes":
    word = str(input("Word in english :"))
    DiccEnglishSpanish.append(word)
    word2 = str(input("World in spanish :"))
    DiccEnglishSpanish.append(word2)
    Condition = str(input("add more words? type: Yes/No"))

print(DiccEnglishSpanish)
















"""
"""diccEspanol = []
diccIngles = []
Condicion = "Si"
while Condicion == "Si":
     espanol = str(input("Inserte la palabra en español"))
     diccEspanol.apeend(espanol)
     ingles = str(input("In english pls"))
     diccIngles.apeend(ingles)
     frase = espanol + ingles
     Condicion = str(input("Añadir otra palabra digite: Si/No"))


print(diccEspanol)
print(diccIngles)
print(frase)
"""