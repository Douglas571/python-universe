from fractions import Fraction
import util
import algorithms as alg

def is_correct_m(m):
	util.print_matrix(m)
	res = input('\n¿Esta es la matriz? (s/n): ')
	return (res.lower() == 's')

def get_number_of_rows_and_cols():
	print('\nEn la matriz ampliada...')
	rows = int(input('¿Cuántas filas hay? '))
	cols = int(input('¿Cuántas columnas hay? '))

	return rows, cols

def get_amplified_matrix(n_rows, n_cols):
	m = []
	print('\nEscrb. los elementos en cada fila (ej: 1/2, 2, 0, 3.7)')
	for i in range(n_rows):
		row = []

		elms = input(f'fila #{(i + 1)}: ').strip().split(',')
		row = ([Fraction(x) for x in elms])

		m.append(row)

	return m

def main():
	print('--- Métodos de eliminación Gauss/Gauss-Jordan ---')

	m = []
	done = False
	while not done:
		n_rows, n_cols = get_number_of_rows_and_cols()
		m = get_amplified_matrix(n_rows, n_cols)
		done = is_correct_m(m)

	m2 = util.copy(m)

	m, err = alg.gauss(m)
	m2, err = alg.gauss_jordan(m2)

	if err:
		print(err)
		util.print_matrix(m)
		return 0

	print('\n---- RESULTADOS -----')
	print('Gauss:')
	util.print_matrix(m)

	print('\nGauss Jordan:')
	util.print_matrix(m2)

if __name__ == '__main__':
	main()