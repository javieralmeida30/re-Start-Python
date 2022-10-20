"""
IMPRESORA DE CHEQUES: 
- escribir un programa que le pida al usuario una cifra en numeros y el programa lo imprima en letras: 
 ejemplo: 
    input:   1950523
    output:  un millon novecientos cincuentamil quinientos veintitres dolares

"""
import math
n= int(input("Introduce un numero de 2 cifras"))
decena = math.trunc(n/10)
unidad = n % 10
if decena==1:
    print("")
    else if decena==2:
        print("veinti", end="2")
         print("veinti", end="3")
          print("veinti", end="3")
           print("veinti", end="4")
            print("veinti", end="5")
             print("veinti", end="6")
              print("veinti", end="7")
               print("veinti", end="8")
                print("veinti", end="9")
                else:
                    print("")