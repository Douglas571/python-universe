import math

def calc_new_range(fn, a, b):
	Ya = fn(a)
	Yb = fn(b)

	#print(f'\n*** calculating new range ***')
	#print(f'f(a) = f({a}) = {Ya}')
	#print(f'f(b) = f({b}) = {Yb}')

	c = b - ((Yb*(a - b))/(Ya - Yb))
	Yc = fn(c)
	#print(f'\nc = b - ((f(b)*(a - b))/(f(a) - f(b))')
	#print(f'c = {b} - ({Yb}*({a} - {b}))/({Ya} - {Yb})')
	#print(f'c = {c}')
	#print(f'f(c) = f({c}) = {Yc}')
	#print(f'f(c) = {Yc}')

	p = Ya * Yc

	#print(f'\n___comprobando intervalo___')
	#print(f'f(a).f(c) = f({a}).f({c})')
	#print(f'f(a).f(c) = {Ya}.f({Yc}) = {p}')
	if p > 0:
		#print(f'{p} > 0: [c, b]: [{c}, {b}]')
		return c, b, c

	#print(f'{p} < 0: [a, c]: [{a}, {c}]')
	return a, c, c

def regula_falsi(fn, a, b, t=10, fn_err=None, v=False):
	if not fn_err:
		fn_err = lambda x, y : math.fabs((x - y) / x ) * 100

	c = None
	err = 100
	last_aprx = None

	results = []

	#i = 0
	#print('\n...... Regula Falsi .......')
	while err > t:
		#i += 1
		#print(f'\n---- {i}th Iteration ----')
		a, b, c = calc_new_range(fn, a, b)

		if last_aprx:
			err = fn_err(c, last_aprx)

		last_aprx = c

		res = { 'a': a, 'b': b, 'c': c, 'err': err }
		results.append(res)

	if v:
		print(f'\n--- Regula Falsi Results ---')
		for i, res in enumerate(results):
			print(f'{(i+1):>2}. {res}')

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