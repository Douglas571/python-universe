# Programa para comparar 3 numeros

class Comparador:
  def __init__(self, *numbers):
    if len(numbers) > 3:
      print('ERROR: Solo 3 numeros')
      exit(0)

    self.a = numbers[0]
    self.b = numbers[1]
    self.c = numbers[2]

  def run(self):
    if self.a > self.b:
      if self.a > self.c:
        return ('a', self.a)

      else:
        return ('c', self.c)

    else:
      if self.b > self.c:
        return ('b', self.b)
        

      else:
        return ('c', self.c)
        


c = Comparador(2, 3, 4)
result = c.run()

print(f'el numero mayor es {result[0]} = {result[1]}')

