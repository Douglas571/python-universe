# la resolvente 
import math

class MyOwnMath:
  def resolvente(self, a, b, c):
    if a == 0:
      return None

    x1 = (-b + math.sqrt((math.pow(b, 2) - 4*a*c)))/(2*a)
    x2 = (-b - math.sqrt((math.pow(b, 2) - 4*a*c)))/(2*a)
    return (x1, x2)

m = MyOwnMath()

print(m.resolvente(1, -9, 8))