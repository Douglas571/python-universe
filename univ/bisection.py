import math

def get_aprox(Xa, Xb):
	m = (Xa + Xb) / 2
	print(f'\nm = {Xa} + {Xb} / 2')
	print(f'm = {m}')
	return m

def calc_new_range(fn, Xa, Xb, aprox):
	Ya = fn(Xa)
	Y_aprox = fn(aprox)

	print(f'\n --- calc_new_range ---')
	print(f'f(a) = f({Xa}) = {fn(Xa)}')
	print(f'f(b) = f({Xb}) = {fn(Xb)}')
	print(f'f(m) = f({aprox}) = {fn(aprox)}')

	p = Ya * Y_aprox
	print(f'\nf(a).f(m) = f({fn(Xa)}).f({fn(aprox)})')
	print(f'\nf(a).f(m) = {p} < 0: {p < 0}')

	if Ya * Y_aprox > 0:
		return aprox, Xb

	if Ya * Y_aprox < 0:
		return Xa, aprox

	return Xa, Xb

def bisection(fn, Xa, Xb, t=10, v=False):
	aprx = None
	err = 100
	calc_error = lambda x, y : math.fabs((x - y) / x ) * 100
	results = []

	last_aprx = None
	i = 0
	while err > t:
		i += 1
		print(f'\n........ {i}th Iteración .....')
		aprx = get_aprox(Xa, Xb)
		Xa, Xb = calc_new_range(fn, Xa, Xb, aprx)

		if last_aprx:
			err = calc_error(aprx, last_aprx)

		last_aprx = aprx

		res = { 
			'Xa': Xa,
			'Xb': Xb, 
			'aprox': aprx, 
			'error': err
		}

		results.append(res)
		

	if v:
		for i, res in enumerate(results):
			print(f'{(i+1):>2}. {res}')

	return aprx, err


def main():
	a = 0
	b = 1
	fn = lambda x : 6*x**3 - 5*x**2 + 7*x - 2
	t = 10

	aprx, err = bisection(fn, a, b, t)
	print(f'aprx={aprx}, err={err}')

if __name__ == '__main__':
	main()