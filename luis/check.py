def main():
	entr = ''
	num1 = 0
	num2 = 0
	num3 = 0
	res_suma = 0
	res_bool = ''

	print('[>] Este, es un programa que recibe 3 enteros, suma los 2 primeros y verifica si da igual al 3ro.')
	print()

	try:
		entr = input('[?] Numero 1: ')
		num1 = int(entr)

		entr = input('[?] Numero 2: ')
		num2 = int(entr)

		entr = input('[?] Numero 3: ')
		num3 = int(entr)

		res_suma = num1 + num2


		if res_suma == num3:
			res_bool = 'igual a'

		else:
			res_bool = f'{res_suma}, distinto de'

		# imprimir: el resultado de sumar: 1 + 2 es igual a 3

		print()
		print(f'[>] El resultado de sumar: {num1} + {num2} es {res_bool} {num3}.')

	except ValueError as err:
		print(f'Error: "{entr}" no es un entero.')

if __name__ == '__main__':
	main()