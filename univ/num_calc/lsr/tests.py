import util
from algorithms import *

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

def test(m):
	m = util.convert_to_fractions(m)
	m, err = gauss(m)

	if err:
		print(err)
		util.print_matrix(m)
		return 0

	print('Resultado: Sistema determinado, compatible.')
	util.print_matrix(m)

def testgj(m):

	m = util.convert_to_fractions(m)
	m, err = gauss_jordan(m)

	if err:
		print(err)
		util.print_matrix(m)
		return 0

	print('Resultado: Sistema determinado, compatible.')
	util.print_matrix(m)

if __name__ == '__main__':
	print('gauss')
	test(test1)
	test(test2)
	test(test3)
	test(test4)

	print('gauss jordan')
	testgj(test1)
	testgj(test2)
	testgj(test3)
	testgj(test4)