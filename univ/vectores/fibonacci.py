import math

#TO-DO: develop a function that make fibonacci series

fib = {}

n = 15
for i in range(0, n+1):
    if i == 0 or i == 1: fib[str(i)] = 1
    else : fib[str(i)]=fib[str(i-1)]+fib[str(i-2)]

def f(x):
    return 5*math.pi*x - x**2

def diference(a, b):
    return b - a

def delta(x, y, z):
    #print(f'i_up={y}')
    return x*y/z

def runFib(n, i, a, b):
    L = diference(a, b)
    #print(f'b-a = {L}')

    i_up = n - i - 1
    i_down = n - i + 1

    #IMPORTANTE CAMBIAR en cada iteracion

    D = delta(L, fib[str(i_up)], fib[str(i_down)])


    #print(f'delta = {D}\n')

    xa = a + D
    xb = b - D

    #print(f'Xa = {xa}')
    #print(f'Xb = {xb}\n')

    fxa = f(xa)
    fxb = f(xb)

    #print(f'f(Xa = {xa}) = {f(xa)}')
    #print(f'f(Xb = {xb}) = {f(xb)}\n')

    if fxa > fxb:
        #print('rechazar 2do intervalo')
        #print(f'new b = xb = {xb}')
        return [a, xb, xa, xb, fxa, fxb]
    else:
        #print('rechazar 1er intervalo')
        #print(f'new a = xa = {xa}')
        return [xa, b, xa, xb, fxa, fxb]

n = 7
i = 1
a = 0
b = 20

for i in range(1, n):
    print(f'iteración # {i}')
    print(f'a = {a};\nb = {b};')

    a, b, Xa, Xb, fxa, fxb = runFib(n, i, a, b)

    print(f'Xa = {Xa};\nXb = {Xb};')
    print(f'f({Xa}) = {fxa};')
    print(f'f({Xb}) = {fxb};')
    print()