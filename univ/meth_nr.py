import math

def meth_nr(fn, Dfn, x, t=10, fn_err=None):
	if not fn_err:
		fn_err = lambda x, y: math.fabs(((x - y) / x) * 100)

	err = 100
	results = []
	results.append({'x': x, 'err': None})

	i = 0
	while err > t:
		print(f'\n--- iteration #{i}')
		next_x = x - (fn(x)/Dfn(x))

		print(f'f(x) = f({x}) = f({fn(x)})')
		print(f'Df(x) = Df({x}) = Df({Dfn(x)})')
		print(f'x{i + 1} = {next_x}')

		if i > 0:
			err = fn_err(next_x, x)

		r = {'x':x, 'err': err}
		x = next_x
		results.append(r)
		i += 1

	print(f'\n--- results ---')
	for i, r in enumerate(results):
		print(f'{i:>2}. {r}')

	print()
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