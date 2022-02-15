import math

def meth_nr(fn, Dfn, x, t=10, fn_err=None, v=False):
	print(f'\n.... Method of newton raphson ....')
	if not fn_err:
		fn_err = lambda x, y: math.fabs(((x - y) / x) * 100)

	err = 100
	results = []
	X = [x]

	i = 0
	while err > t:
		print(f'\n--- {i + 1}th Iteration ---')

		print(f'\nf(x) = f({X[i]}) = {fn(X[i])}')
		print(f'Df(x) = Df({X[i]}) = {Dfn(X[i])}')

		new_x = X[i] - (fn(X[i])/Dfn(X[i]))
		print(f'X{(i + 1)}={new_x}')
		X.append(new_x)


		if len(results) > 1:
			err = fn_err(X[i+1], X[i])

		r = {'x': X[i], 'next_x': X[i+1], 'err': err}
		#x = next_x
		results.append(r)
		i += 1

	if v:
		print(f'\n--- N-R Results ---')
		for i, r in enumerate(results):
			print(f'{(i):>2}. {r}')

	return new_x, err

def main():
	x = 4
	fn = lambda x: x**3 - 6*x**2 + 11*x - 8
	Dfn = lambda x: 3*x**2 - 12*x + 11
	t = 0.0001

	aprx, err = meth_nr(fn, Dfn, x, t)
	print(f'aprx={aprx}, err={err}')

if __name__ == '__main__':
	main()