#Programa que utiliza el método de la sección dorada para optimizar una función

#Importar librerías
import math

#Definir funcion
def f(x):
    return 2*math.sin(x)-((x)**2/10)

#Definir intervalo de búsqueda
i1 = 0
i2 = 4

#Definir número de iteraciones
n = 100

#Definir tolerancia
tol = 0.1

#Definir ciclo de iteraciones
for i in range(n):
    a = 0.618(i1 - i2)
    b = 0.618**2(i1 - i2)
    
    x1 = i1 + a
    x2 = i1 + b
    f1 = f(x1)
    f2 = f(x2)

    if f1 < f2:
        i1 = i1
        i2 = x1
    else:
        i1 = x2
        i2 = i2
    if abs(i2 - i1) < tol: break
    print(i, i1, i2)