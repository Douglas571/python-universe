import math

def get_aprox(Xa, Xb):
	return (Xa + Xb) / 2

def calc_new_range(fn, Xa, Xb, aprox):
	Ya = fn(Xa)
	Y_aprox = fn(aprox)

	if Ya * Y_aprox > 0:
		return aprox, Xb

	if Ya * Y_aprox < 0:
		return Xa, aprox

	return Xa, Xb

def bisection(fn, Xa, Xb, t=10):
	aprx = None
	err = 100
	calc_error = lambda x, y : math.fabs((x - y) / x ) * 100
	results = []

	last_aprx = None
	while err > t:
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