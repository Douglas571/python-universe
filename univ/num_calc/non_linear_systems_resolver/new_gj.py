import gj

def intercambiar(m, a, b):
	print(f'm{m}')
	print(f'a{a}')
	print(f'b{b}')
	temp = m[a]
	m[a] = m[b]
	m[b] = temp
	return m


def suma(fila_a, fila_b):
	return [a + b for a, b in zip(fila_a, fila_b)]

def producto_escalar(fila, k):
	print(k)
	print(fila)
	return [x * k for x in fila]

def ceros_abajo(m, i, n_filas):
	end = False
	j = i + 1
	while(m[i][i] == 0 and j < n_filas):
		print(f'm{m}')
		print(f'i{i}')
		print(f'j{j}')

		m = intercambiar(m, i, j)
		j += 1

	if(m[i][i] == 0):
		end = True

	return m, end


def gauss_jordan(m):
	n_incog = len(m[0]) - 1
	n_filas = len(m)

	print(f'incog. {n_incog}; ecuaciones {n_filas}')

	for i in range(n_incog):
		print(i)
		gj.print_matriz(m)
		if m[i][i] == 0:
			m, end = ceros_abajo(m, i, n_filas)
			if end: break
		
		k = 1/m[i][i]
		m[i] = producto_escalar(m[i], k)
		
		for j in range(n_incog):
			if i == j: continue
			k = -m[j][i]/m[i][i]
			#print(f'k {k}')
			aplanador = producto_escalar(m[i], k)
			#print(f'j={m[j][0]} + ap={str(aplanador[0])}')
			#print(m[j][0] + aplanador[0])
			m[j] = suma(m[j], aplanador)

		
	return m

def main():
	m = [
		[1, 1, 1, 9],
		[2, -3, 4, 13],
		[3, 4, 5, 40],
	]
	m = gj.convert_to_fraction(m)
	new_m = gauss_jordan(m)
	
	gj.print_matriz(m)

if __name__ == '__main__':
	main()
