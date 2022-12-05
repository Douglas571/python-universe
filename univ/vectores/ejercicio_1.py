# crea un programa que calcule el producto escalar de dos vectores
n = int(input('numero de elementos: '))
v = []
w = []
pescalar = 0

for i in range(n):
    vi = float(input('introduce elemento de v: '))
    wi = float(input('introduce elemento de w: '))
    v = v + [vi]
    w = w + [wi]
    pescalar = pescalar + v[i] * w[i]

print('vector v= ', v)
print('vector w= ', w)
print('producto escalar= ', pescalar)