# Program to automate my homework of the subject
# "numerical analysis", error analysis.

import sys
import math

def calc_tolerance(significant_numbs):
	return 0.5 * math.pow(10, 2 - significant_numbs)

def get_aprox(x):
	return 1 - x

def main():
	t = calc_tolerance(5)

	vv = math.exp(float(sys.argv[1]))
	x = float(sys.argv[2])

	aprox_ant = 0
	aprox = get_aprox(x) 
	ev = vv - aprox
	er = ev / vv

	print(f'vv: {vv};')
	print(f'x: {x};')
	print(f'aprox: {aprox};')
	print(f'ev: {ev:.10f}')
	print(f'er: {er:.10f} => {er * 100:.10f}%')

	if len(sys.argv) > 3:
		aprox_ant = float(sys.argv[3])
		ea = math.fabs((aprox - aprox_ant) / aprox)
		print(f'ea: {ea:.10f} => {(ea * 100):.10f}%')
		print('')

		print(f'tolerancia: {t}%')
		print(f'ea < e: {((ea * 100) < t)}')

def main_2():
	register = list()

	t = calc_tolerance(int(sys.argv[1]))
	vv = math.exp(float(sys.argv[2]))

	objective = 1 - vv

	last_ea_perc = 1000

	count = 2
	x = float(str(get_aprox(vv))[0:count])	
	while last_ea_perc >= t:
		aprox = get_aprox(x) 
		ev = vv - aprox
		er = ev / vv

		aprox_ant = 0
		if len(register) > 0:
			aprox_ant = register[-1]['aprox']
		
		ea = math.fabs(aprox - aprox_ant) / aprox
		last_ea_perc = ea * 100

		reg = {}
		reg['x'] = x
		reg['aprox'] = aprox
		reg['ev'] = ev
		reg['er'] = er
		reg['ea'] = ea

		register.append(reg)
		count += 1
		x = float(str(get_aprox(vv))[0:count])

	print(f'tolerancia: {t}%')
	print()

	print(f'itr x          aprox      ER           EA         ')
	for itr in range(0, len(register)):
		reg = register[itr]
		x = reg['x']
		aprox = round(reg['aprox'], 10)
		ER = reg['er']
		EA = reg['ea']

		ER = f'{(ER * 100):.5f}'
		EA = f'{(EA * 100):.5f}'

		print(f'{(itr + 1): <3} {x: <10} {aprox: <10} {ER: >10}% {EA: >10}%')

	print('')
	for itr in range(0, len(register)):

		reg = register[itr]
		x = reg['x']
		aprox = round(reg['aprox'], 10)
		EV = reg['ev']
		ER = reg['er']
		EA = reg['ea']		

		ER_perc = f'{(ER * 100):.5f}'
		EA_perc = f'{(EA * 100):.5f}'

		print(f'Iteración: {itr + 1}')
		print(f'vv: {vv};')
		print(f'x: {x};')
		print(f'aprox: {aprox};')
		print(f'ev: {EV:0.10f}')
		print(f'er: {ER:0.10f} => {ER_perc}%')

		print(f'ea: {EA:0.10f} => {EA_perc}%')
		print('')



if __name__ == '__main__':
	main_2()