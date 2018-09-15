import math

def have_equal_sign(a, b):
	return a > 0 and b > 0

def calc_new_range(fn, a, b):
	print('\n---- calc_new_range ----')
	Ya = fn(a)
	Yb = fn(b)

	c = b - ((Yb*(a - b))/(Ya - Yb))
	Yc = fn(c)

	p = Ya * Yc

	print(f'f(a) = f({a}) = {Ya}')
	print(f'f(b) = f({b}) = {Yb}')
	print(f'f(c) = f({c}) = {Yc}')
	print(f'p = {p}')

	if p > 0:
		return c, b, c

	return a, c, c

def regula_falsi(fn, a, b, t=10, fn_err=None):
	print('\n........start regula falsi......')

	if not fn_err:
		fn_err = lambda x, y : math.fabs((x - y) / x ) * 100

	c = None
	err = 100
	last_aprx = None

	results = []

	print(f'a={a}, b={b}, c={c}, err={err}')
	while err > t:
		a, b, c = calc_new_range(fn, a, b)

		if last_aprx:
			print(f'\n--- calc error ---')
			err = fn_err(c, last_aprx)
			print(f'l_aprx={last_aprx}, c={c}')
			print(f'err={err}')

		last_aprx = c
		print('\n--- iter results ---')

		res = { 'a': a, 'b': b, 'c': c, 'err': err }
		print(f'res={res}')
		results.append(res)

	print()
	for i, res in enumerate(results):
		print(f'{i}. {res}')

	return c, err

def main():
	a = 6
	b = 7
	fn = lambda x : -0.5*x**2 + 2.5*x + 4.5
	t = 10

	aprx, err = regula_falsi(fn, a, b, t)
	print(f'aprx={aprx}, err={err}')

if __name__ == '__main__':
	main()