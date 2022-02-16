from fractions import Fraction as frac

import util

def gauss(m): 
	#util.print_matrix(m)

	#execute gauss elimination
	for i in range(len(m)):
		el = m[i][i]

		m, err = util.zeros_down(m, i)	
		if err: return m, err
		
		m = util.clear(m, i, simple=True)

	return m, None

def gauss_jordan(m):
	#util.print_matrix(m)

	#execute gauss elimination
	for i in range(len(m)):
		el = m[i][i]

		m, err = util.zeros_down(m, i)
		if err: return m, err

		k = 1/m[i][i]
		m[i] = util.scalar_product(m[i], k)
		
		m = util.clear(m, i)

	return m, None

#---------- TESTS -----------#

test1 = [
		[ 0, 3,  1, 0],
		[ 0, 1, 2, 1],
		[ 1, -1, -1, -1]
] # valido

test2 = [
		[1, 2, 2, 2],
		[2, 1, 3, 3],
		[3, 3, 5, 6]
] # no tiene solución

test3 = [
		[1, 1, -1, 0],
		[2, 1, -1, 1],
		[0, -1, 1, 1]
] # infinitas soluciones

test4 = [
		[1, 2, 2, 1],
		[3, 1, 2, 5],
		[4, 3, 3, 8]
] # bien

def test():
	m = test4

	m = util.convert_to_fractions(m)
	m, err = gauss_jordan(m)

	if err:
		print(err)
		print_matrix(m)
		return 0

	print('El resultado es:')
	print_matrix(m)

if __name__ == '__main__':
	test()