import math

fi = 1.618033988
e = 0.3
a = 0
b = 20

# ------------    

def run_golder_search(a, b):
    a1 = a*(1 - fi) + b * fi
    a2 = a * fi + b*(1 - fi)

    def f(x):
        return 5*math.pi*x - x**2

    fa1 = f(a1)
    fa2 = f(a2)

    if fa1 > fa2:
        return [a1, b, a1, a2, fa1, fa2]
    else:
        return [a, a2, a1, a2, fa1, fa2]

for i in range(15):
    a, b, a1, a2, fa1, fa2 = run_golder_search(a, b)
    print(f'iteración #{i}')
    print(f' a={a};\n b={b};\n a1={a1};\n a2={a2}')   
    print(f'f({a1})={fa1}')
    print(f'f({a2})={fa2}')
    print()

    if math.fabs(a1 - a2) < e: break
