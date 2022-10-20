import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
#Coloque el cursor en la línea siguiente a la segunda instrucción print(). Luego,
#escriba una instrucción que generará un número aleatorio entre 1 y 10 mediante el uso de la función randint() del módulo random.
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

""" Pseudocodigo: Si el usuario no ha adivinado la respuesta correcta, ingrese el bucle.

Pida al usuario que adivine el número.

¿Es el número correcto?

Si la respuesta es correcta, dígaselo al usuario y salga del bucle.

Si no ha adivinado el número, indique al usuario que fue una suposición incorrecta y continúe con el bucle. """