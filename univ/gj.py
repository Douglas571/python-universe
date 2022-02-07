"""
	Desarrollar un programa que resuelva ecuaciones
	lineales mediante el metodo de gaus jordan.
"""

import math
from fractions import Fraction

def print_matriz(matriz):
	num_de_filas = len(matriz)
	num_de_colms = len(matriz[0])

	for f in range(0, num_de_filas):
		for c in range(0, num_de_colms):
			end_c = ', '
			if (num_de_colms - c) == 2:
				end_c = ' | '

			print(f'{matriz[f][c]}', end=end_c)
		print()
	print()

def es_escalonada_reducida(matriz):
	pass

def gauss(matriz):
	pass

# convertir el renglon que me intereza en 1
# sumar a los arreglos de arriba y abajo, -1 * obj

def multiplicar_por_escalar(fila, k):
	return [n * k for n in fila]

def sumar_filas(A, B):
	return [a + b for a, b in zip(A, B)]

def gauss_jordan(matriz):
	n_filas = len(matriz)
	n_colms = len(matriz[0])

	matriz = convert_to_fraction(matriz)

	#print_matriz(matriz)
 	#------------

	lim = n_colms
	if (n_colms > n_filas):
 		lim = n_filas

	for f in range(0, lim):
		#print(f)
		#print(matriz[f])
		k = 1/matriz[f][f]
		matriz[f] = multiplicar_por_escalar(matriz[f], k)
		#print_matriz(matriz)

		for fc in range(0, n_filas):
		 	if f == fc: continue
		 	a = matriz[f][f]
		 	b = matriz[fc][f]
		 	k = -b/a

		 	#print(f'fila {fc}')
		 	aplanadora = multiplicar_por_escalar(matriz[f], k)
		 	#print(f'x={x};')
		 	matriz[fc] = sumar_filas(matriz[fc], aplanadora)

	print('resultado')
	print_matriz(matriz)

	return matriz

def convert_to_fraction(matriz):
	for f in range(0, len(matriz)):
		matriz[f] = [Fraction(x).limit_denominator(1000) for x in matriz[f]]

	return matriz

def main():
	matriz = [
		['3/5', 1.1],
		['0.333', 4]
	]
	matriz = convert_to_fraction(matriz)
	#print(matriz)
	print_matriz(matriz)

if __name__ == '__main__':
	main()