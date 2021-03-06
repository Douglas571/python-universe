"""
	Main execution file, 
	for console input and output
	
	by Douglas Socorro 29.748.656
	douglassocorro1@gmai.com
"""

from fractions import Fraction
import util
import algorithms as alg

def m_is_correct(m):
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

		if len(row) > n_cols:
			err = f'Error: hay elementos demas en la fila {(i+1)}'
			return m, err

		if len(row) < n_rows:
			err = f'Error: faltan elementos en la fila {(i+1)}'
			return m, err

		m.append(row)

	return m, None

def main():
	print('--- Métodos de eliminación Gauss/Gauss-Jordan ---')

	m = []

	while True:
		n_rows, n_cols = get_number_of_rows_and_cols()
		m, err = get_amplified_matrix(n_rows, n_cols)

		if err:
			print(err)
			return 0

		if m_is_correct(m): break

	m2 = util.copy(m)

	m, err = alg.gauss(m)
	m2, err = alg.gauss_jordan(m2)

	if err:
		print(err)
		print('Gauss:')
		util.print_matrix(m)
		print('\nGauss Jordan:')
		util.print_matrix(m2)
		return 0

	print('\n---- RESULTADOS -----')
	print('Gauss:')
	util.print_matrix(m)

	print('\nGauss Jordan:')
	util.print_matrix(m2)

if __name__ == '__main__':
	main()