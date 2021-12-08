# entrada: cantidad de ventas4

def main():
	bono = 0.0
	# int de integuer, enteros, numeros: 1, 2, 3, 4, 5
	num_de_ventas = int(input('numero de ventas? '))
	
	# float de flotante, numeros de coma flotante = decimales 0.3, 0.5
	pago = float(input('pago en bs? '))

	print('numero de ventas: ', num_de_ventas)
	print('pago: ', pago)

	# PROCESO
	# bono_en_por = calcular bono porcentaje
	# vendió 500.000, bono es 5%
	if num_de_ventas >= 500000:
		bono = 0.05
    
	# si vendió 1500k, bono es 8%
	if num_de_ventas >= 1500000:
		bono = 0.08

	# si vendió 3000k, bono es 12%
	if num_de_ventas >= 3000000:
		bono = 0.12

	# si vendió 4500k, bono es 15%
	if num_de_ventas >= 4500000:
		bono = 0.15

	# calcular pago en bolivares
	bono_bs = pago * bono
	print('bono en %: ', bono)
	print('bono en bolivares: ', bono_bs)

	# bono en bolivares = pago x bono en porcentaje
	# pago total = pago + bono en bolivares
	pago_total = pago + bono_bs

	# print('mostrar por pantalla')
	print('el pago mas el bono es igual a ', pago_total, "Bs")


"""
 salida: 
 	bono

 	pago en bolivares

 	mostrar por pantalla


"""

main()