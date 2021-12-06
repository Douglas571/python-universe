import sys

def calcular_bono2(num_de_ventas):
	bono = 0

	if num_de_ventas in range(500000, 1500000):
		bono = 0.05

	if num_de_ventas in range(1500000, 3000000):
		bono = 0.08

	if num_de_ventas in range(3000000, 4500000):
		bono = 0.12

	if num_de_ventas in range(4500000, 6000000):
		bono = 0.15

	return bono

def calcular_bono(num_de_ventas):
	bono = 0

	if (num_de_ventas >= 500000) and (num_de_ventas < 1500000):
		bono = 0.05

	if (num_de_ventas >= 1500000) and (num_de_ventas < 3000000):
		bono = 0.08

	if (num_de_ventas >= 3000000) and (num_de_ventas < 4500000):
		bono = 0.12

	if (num_de_ventas >= 4500000) and (num_de_ventas < 6000000):
		bono = 0.15

	return bono

def main():
	entrada = ''
	num_de_ventas = 0

	try:
		if len(sys.argv) > 1:
			entrada = sys.argv[1]
			num_de_ventas = int(entrada)

		else:
			entrada = input('[?] Numero de ventas: ')
			num_de_ventas = int(entrada)

		bono = calcular_bono(num_de_ventas)
		print(f'El bono es de: {bono * 100}%')

		if bono == 0:
			print('El mínimo de ventas es: 500000')

	except ValueError:
		print(f'Error: "{entrada}" no es un numero entero.')

if __name__ == '__main__':
	main()