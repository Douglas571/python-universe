# Sumatoria de numeros primos

class SumadorDePrimos:
  def __init__(self, FROM, TO):
    self._from = FROM
    self._to = TO  
    self._primos = []
    self._sumatoria = 0

    self._optener_primos()
    self._optener_sumatoria()

  def print(self):
    print(f'Los numeros primos son: {self._primos}')
    print(f'La sumatoria es: {self._sumatoria}')

  def _optener_primos(self):
    for n in range(0, self._to + 1):
      if self._es_primo(n):
        self._primos.append(n)

  def _es_primo(self, numero):
    for n in range(numero - 1, 1, -1):

      #print(f'{numero}/{n} = {numero%n}')
      
      if numero % n == 0:
        return False

    return True

  def _optener_sumatoria(self):
    c = 0
    for n in self._primos:
      c += n

    self._sumatoria = c

contador = SumadorDePrimos(0, 200)
contador.print()