import math

def meth_nr(fn, Dfn, x, t=10, fn_err=None, v=False):
	if not fn_err:
		fn_err = lambda x, y: math.fabs(((x - y) / x) * 100)

	err = 100
	results = []

	while err > t:
		next_x = x - (fn(x)/Dfn(x))

		if len(results) > 0:
			err = fn_err(next_x, x)

		r = {'x':x, 'next_x': next_x, 'err': err}
		x = next_x
		results.append(r)

	if v:
		print(f'\n--- N-R Results ---')
		for i, r in enumerate(results):
			print(f'{(i + 1):>2}. {r}')

	return next_x, err

def main():
	x = 4
	fn = lambda x: x**3 - 6*x**2 + 11*x - 8
	Dfn = lambda x: 3*x**2 - 12*x + 11
	t = 0.0001

	aprx, err = meth_nr(fn, Dfn, x, t)
	print(f'aprx={aprx}, err={err}')

if __name__ == '__main__':
	main()