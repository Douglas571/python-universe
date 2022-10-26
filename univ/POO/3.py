# Programa que calcula los numeros impares y su sumatoria
# del 1 - 20

class Sumador:
  def __init__(self):
    self._from_n = 1
    self._to = 10

    self._obtener_impares()
    print(self._impares)

  def _obtener_impares(self):
    self._impares = []
    for n in range(self._from_n, self._to):
      if not (n%2 == 0):
        self._impares.append(n)

  def imprimir_numeros_impares(self):
    print('los numeros impares son:' , end=" ")
    for n in self._impares:
      print(n, end=" ")
    print('\n')

  def imprimir_sumatoria(self):
    c = 0
    for n in self._impares:
      c += n

    print(f'la sumatoria es: {c}')

sumador = Sumador()
sumador.imprimir_sumatoria()
sumador.imprimir_numeros_impares()