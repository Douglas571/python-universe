# Realizar un programa donde se determine si un estudiante es mayor
# de edad utilizando POO

class Estudiante:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def es_mayor_de_edad(self):
    return self.edad >= 18

estudiante = Estudiante('douglas', 21)

if estudiante.es_mayor_de_edad():
  print(f'{estudiante.nombre} es mayor de edad')
else:
  print(f'{estudiante.nombre} es menor de edad')