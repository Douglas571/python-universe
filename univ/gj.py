"""
	Desarrollar un programa que resuelva ecuaciones
	lineales mediante el metodo de gaus jordan.
"""

import math

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

def gauss_jordan1(matriz):
	n_filas = len(matriz)
	n_colms = len(matriz[0])

	coeficiente = matriz[0][0]

	def mutiplicar(n):
		return n * coeficiente

	print("dividir 1ra fila por 1/5")
	matriz[0] = [ n / coeficiente for n in matriz[0]]
	print_matriz(matriz)

	print('convertir a00 en 1')
	inferior = matriz[1][0]
	matriz[1] = [n / math.fabs(inferior) for n in matriz[1]]
	print_matriz(matriz)

	print('convertir inferiores en 0')
	inferior = matriz[1][0]
	if (inferior + matriz[0][0]) == 0:
		for c in range(0, n_colms):
			matriz[1][c] += matriz[0][c]
	print_matriz(matriz)

	#---------- 2da fila ----------#
	print('convertir a11 en 1')
	obj = matriz[1][1]
	matriz[1] = [n * (1 / obj) for n in matriz[1]]
	print_matriz(matriz)

	print('convertir a01 en 0')
	obj = matriz[0][1]
	for c in range(0, n_colms):
		matriz[0][c] += matriz[1][c] * -obj
	print_matriz(matriz)

	return matriz

def multiplicar_por_escalar(fila, k):
	return [n * k for n in fila]

def sumar_filas(A, B):
	return [a + b for a, b in zip(A, B)]

def gauss_jordan3x3(matriz):
	n_filas = len(matriz)
	n_colms = len(matriz[0])

	matriz = convert_to_fraction(matriz)

	print_matriz(matriz)
 #------------
	

	for f in range(0, n_colms - 1):
		k = 1/matriz[f][f]
		matriz[f] = multiplicar_por_escalar(matriz[f], k)
		print_matriz(matriz)

		for fc in range(0, n_filas):
		 	if f == fc: continue
		 	a = matriz[f][f]
		 	b = matriz[fc][f]
		 	x = -b/a

		 	print(f'fila {fc}')
		 	aplanadora = multiplicar_por_escalar(matriz[f], x)
		 	print(f'x={x};')
		 	matriz[fc] = sumar_filas(matriz[fc], aplanadora)

	print('resultado')
	print_matriz(matriz)

	return matriz

from fractions import Fraction

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