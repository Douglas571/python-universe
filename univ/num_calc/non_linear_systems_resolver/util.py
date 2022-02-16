from fractions import Fraction

def print_matrix(m):
	for i in range(len(m)):
		for j in range(len(m[0])):
			el = str(m[i][j])
			if j == 0:
				print(f'  ({el:>7}', end='')
				continue
			
			if j == (len(m[0]) - 1):
				print(f' | {el:>6} )')
				continue

			print(f'{el:>7}', end='')

def suma(fila_a, fila_b):
	return [a + b for a, b in zip(fila_a, fila_b)]

def producto_escalar(fila, k):
	return [x * k for x in fila]

def intercambiar(m, a, b):
	temp = m[a]
	m[a] = m[b]
	m[b] = temp
	return m

def zeros_down(m, i):
	j = i + 1
	n_rows = len(m)
	while(m[i][i] == 0 and j < n_rows):
		#print(f'm{m}')
		#print(f'i{i}')
		#print(f'j{j}')

		m = intercambiar(m, i, j)
		j += 1

	if(m[i][i] == 0):
		total = 0
		for j in range(len(m[i])):
			total += m[i][j]

		err = "Error: El sistema es indeterminado, no hay solución."
		if total == 0:
			err = "Error: El sistema es indeterminado, tiene infinitas soluciones."
		
		return m, err

	return m, None

def clear(m, i, simple=False):
	#print('cleaning')
	start = 0
	end = len(m)

	if simple: start = i

	for j in range(start, end):
		#si j == i: saltar
		if j == i: continue

		a = m[i][i]
		b = m[j][i]
		c = -(b/a)

		#print(f'a = {a}; b = {b}; c = {c}')

		aplanador = producto_escalar(m[i], c)
		m[j] = suma(m[j], aplanador)
		#print_matrix(m)

	return m

def convert_to_fractions(m):
	for i in range(len(m)):
		m[i] = [Fraction(x).limit_denominator(100) for x in m[i]]

	return m

def copy(m):
	new_m = []
	for i in range(len(m)):
		row = []
		for j in range(len(m[i])):
			row.append(m[i][j])
		new_m.append(row)

	return new_m