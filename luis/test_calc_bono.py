import unittest

from calc_bono import calcular_bono

class TestCalcularBono(unittest.TestCase):
	def test_calcular_bono(self):
		res = calcular_bono(500000)
		self.assertEqual(res, 0.05)

		res = calcular_bono(1500000)
		self.assertEqual(res, 0.08)

		res = calcular_bono(3000000)
		self.assertEqual(res, 0.12)

		res = calcular_bono(4500000)
		self.assertEqual(res, 0.15)

if __name__ == '__main__':
	unittest.main()