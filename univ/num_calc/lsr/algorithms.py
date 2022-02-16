"""
	Algorithms of Gauss and Gauss-Jordan
"""

from fractions import Fraction as frac
import util

def gauss(m):
	for i in range(len(m)):
		m, err = util.zeros_down(m, i)

		if err: return m, err
		
		m = util.clear_colum(m, i, simple=True)

	return m, None

def gauss_jordan(m):
	for i in range(len(m)):
		m, err = util.zeros_down(m, i)

		if err: return m, err

		k = 1/m[i][i]
		m[i] = util.scalar_product(m[i], k)
		
		m = util.clear_colum(m, i)

	return m, None