import gj

def comprobation_test():
	print(f'verificando: es_escalonada_reducida()')
	m = [
			[1, 0, -1],
			[0, 1, 4]
		]

	res = gj.es_escalonada_reducida(m)
	gj.print_matriz(m)
	print(f'es escalonada reducida: {res} (true)')

def gauss_jordan1():
	print(f'VERIFICATION: caso1()')
	mt = [
		[ 5, 2,  3],
		[-3, 3, 15]
	]
	gj.print_matriz(mt)
	res = gj.gauss_jordan(mt)

	#print('resultado:')
	#gj.print_matriz(res)
	print('    -----')	
	print('solution is:')
	gj.print_matriz([
			[1, 0, -1],
			[0, 1, 4]
		])

	print('....................')

def gauss_jordan2():
	print(f'VERIFICATION: caso2()')
	mt = [
		[ 5, 2,  0, 2],
		[ 2, 1, -1, 0],
		[ 2, 3, -1, 3]
	]
	gj.print_matriz(mt)

	res = gj.gauss_jordan(mt)
	print('     ------')
	print('solution is:')
	gj.print_matriz([
			[1, 0, 0, -0.2],
			[0, 1, 0, 1.5],
			[0, 0, 1, 1.1]
		])

def gauss_jordan3():
	print(f'VERIFICATION: caso3()')
	mt = [
		[  1.0,  2.0, -3.0, -1.0,  0.0],
		[  0.0, -3.0,  2.0,  6.0, -8.0],
		[ -3.0, -1.0,  3.0,  1.0,  0.0],
		[  2.0,  3.0,  2.0, -1.0, -8.0]
	]
	gj.print_matriz(mt)

	res = gj.gauss_jordan(mt)
	print('     ------')
	print('solution is:')
	gj.print_matriz([
			[1, 0, 0, 0, -1],
			[0, 1, 0, 0, -2],
			[0, 0, 1, 0, -1],
			[0, 0, 0, 1, -2]
		])

def gauss_jordan4():
	print(f'VERIFICATION: caso4()')
	mt = [
		[3, -1, 7, 1],
		[6, 0, 1, 2]
	]
	gj.print_matriz(mt)

	res = gj.gauss_jordan(mt)
	print('     ------')
	print('solution is:')
	gj.print_matriz([
			[1, 0, '1/6', '1/3'],
			[0, 1, '-13/2', 0]
		])
def main():
	comprobation_test()
	gauss_jordan1()
	gauss_jordan2()
	gauss_jordan3()
	gauss_jordan4()

if __name__ == '__main__':
	main()