# Programa para sumar numeros cuadrados
import math

class SumadorDeCuadrados:
  def __init__(self, FROM, TO):
    self._from = FROM
    self._to = TO

    self._sumar_cuadrados()

  def _sumar_cuadrados(self):
    c = 0
    for n in range(self._from, self._to + 1):
      p = math.pow(n, 2)
      #print(f'the power of {n} is {p}')
      c += p

    self._sumatoria = c

  def print(self):
    print(f'La sumatoria de cuadrados desde {self._from} hasta {self._to} es {self._sumatoria}')

def main():
  sumador = SumadorDeCuadrados(0, 10)
  sumador.print()

if __name__ == '__main__':
  main()