import math

def meth_nr(fn, Dfn, x, t=10, v=False, fn_err=None):
	if not fn_err:
		fn_err = lambda x, y: math.fabs(((x - y) / x) * 100)

	err = 100
	results = []
	X = [x]

	i = 0
	while err > t:
		new_x = X[i] - (fn(X[i])/Dfn(X[i]))
		X.append(new_x)


		if len(results) > 1:
			err = fn_err(X[i+1], X[i])

		r = {'x': X[i], 'next_x': X[i+1], 'err': err}
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