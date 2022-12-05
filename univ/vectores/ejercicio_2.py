# Crea un array o arreglo unidimensional donde le indiques 
# el tamaño por teclado y crear una función que rellene el 
# array o arreglo con los múltiplos de un número pedido por 
# teclado. Por ejemplo, si defino un array de tamaño 5 y elijo 
# un 3 en la función, el array contendrá 3, 6, 9, 12, 15. 
# Muestralos por pantalla usando otra función distinta.

def print_multiplos(m):
    print(m)

n = int(input(u"Ingrese el tamaño del arreglo: "))
m = int(input(u"Ingrese el número de múltiplos: "))

A = []

for i in range (1,n + 1):
    A.append(i * m)

print_multiplos(A)