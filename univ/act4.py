from bisection import bisection
from regula_falsi import regula_falsi
from meth_nr import meth_nr

def main():
	print('--- Métodos de busqueda de raices ---')

	a = 0
	b = 1
	fn = lambda x: 6*x**3 - 5*x**2 + 7*x - 2
	t = 0.1

	Dfn = lambda x: 18*x**2 - 10*x + 7
	aprx, err = meth_nr(fn, Dfn, b, t)
	print(f'      N-R: aprx={aprx}, err={err:.9f}')

	aprx, err = bisection(fn, a, b, t, v=True)
	print(f' bisectin: aprx={aprx}, err={err}')

	aprx, err = regula_falsi(fn, a, b, t)
	print(f'reg-falsi: aprx={aprx}, err={err}')

if __name__ == '__main__':
	main()