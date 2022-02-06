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
			end_c = ''
			if (num_de_colms - c) == 2:
				end_c = ' | '

			print(f'{matriz[f][c]:6}', end=end_c)
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

def gauss_jordan3x3(matriz):
	n_filas = len(matriz)
	n_colms = len(matriz[0])

 #------------
	for f in range(0, 2):
		obj = matriz[f][f]
		matriz[f] = [n / obj for n in matriz[f]]

		print_matriz(matriz)

		for fc in range(0, n_filas):
			if f == fc: 
				continue
			print(f'convertir a{fc},{f} en 1')
			n_aplanar= matriz[fc][f]
			matriz[fc] = [n * (1 / n_aplanar) for n in matriz[fc]]
			print_matriz(matriz)
		
			x = matriz[f][f]
			y = matriz[fc][f]
			#print(f'x={x}; y={y}')
			z = -y/x
			#print(f'z={z}')
			print(f'convertir fila {fc} en 0, sumar {z}')
			for c in range(0, n_colms):
				matriz[fc][c] += z

	print('resultado')
	print_matriz(matriz)

	return matriz
if __name__ == '__main__':
	main()

def main():
	pass