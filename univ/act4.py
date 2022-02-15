from bisection import bisection
from regula_falsi import regula_falsi
from meth_nr import meth_nr

def main():
	print('--- Métodos de busqueda de raices ---')
	v = False#True

	a = 2
	b = 3
	fn = lambda x : x**3 - 3 * x**2 + 1.6
	t = 0.00001

	Dfn = lambda x: 18*x**2 - 10*x + 7
	aprx, err = meth_nr(fn, Dfn, b, t, v)
	print(f'      N-R: aprx={aprx}, err={err:.9f}')

	aprx, err = bisection(fn, a, b, t, v)
	print(f' bisectin: aprx={aprx}, err={err}')

	aprx, err = regula_falsi(fn, a, b, t, v)
	print(f'reg-falsi: aprx={aprx}, err={err}')

if __name__ == '__main__':
	main()