import math

fi = 1.618033988
e = 0.5
a = 0
b = 20

# ------------

a1 = a*(1 - fi) + b * fi
a2 = a * fi + b*(1 - fi)

def f(x):
    return 5*math.pi*x - x**2

fa1 = f(a1)
fa2 = f(a2)

if fa1 > fa2:
    a = a1
else:
    b = a2

print(f'a={a}; b={b}; a1={a1}; a2={a2}')