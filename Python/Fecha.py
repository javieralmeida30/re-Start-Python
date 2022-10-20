from datetime import datetime
from datetime import date 
def calcular_edad (nacimiento):
fechaActual  = date.today()
resultado = fechaActual.year - nacimiento.year
return resultado
fecha_nacimiento_javier= date(2000, 5, 27)

edad = calcular_edad (fecha_nacimiento_Javier)

print('Javier tiene ', edad)
