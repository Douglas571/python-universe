# Ejercicio #3 
# Douglas Socorro 29.748.656

import math

class FiguraGeometrica:
	def __init__(self):
		self.nombre = 'unknow'

	def area(self):
		pass

	def __str__(self):
		msg = 'Nombre: ' + self.nombre + '\n'
		
		#msg += self.medidas()

		msg += 'Area: ' + str(self.area()) + ' unidades\n'

		return msg


class Triangulo(FiguraGeometrica):
	def __init__(self, base, altura):
		super().__init__()
		self.nombre = 'Triangulo'
		self.base = base
		self.altura = altura

	def area(self):
		return (self.base * self.altura) / 2

class Circulo(FiguraGeometrica):
	def __init__(self, radio):
		super().__init__()
		self.nombre = 'Circulo'
		self.radio = radio

	def area(self):
		return math.pi * (self.radio**2)

class Cuadrado(FiguraGeometrica):
	def __init__(self, medida_de_un_lado):
		super().__init__()
		self.nombre = 'Cuadrado'
		self.medida_de_un_lado = medida_de_un_lado

	def area(self):
		return self.medida_de_un_lado**2

class Rombo(FiguraGeometrica):
	def __init__(self, diagonal_mayor, diagonal_menor):
		super().__init__()
		self.nombre = 'Rombo'
		self.diagonal_mayor = diagonal_mayor
		self.diagonal_menor = diagonal_menor

	def area(self):
		return (self.diagonal_mayor * self.diagonal_menor) / 2

class Trapecio(FiguraGeometrica):
	def __init__(self, base_mayor, base_menor, altura):
		super().__init__()
		self.nombre = 'Trapecio'
		self.base_mayor = base_mayor
		self.base_menor = base_menor
		self.altura = altura

	def area(self):
		return ((self.base_mayor + self.base_menor) * self.altura) / 2

triangulo = Triangulo(1, 1)
circulo = Circulo(2)
rombo = Rombo(30, 16)
trapecio = Trapecio(10, 4, 4)


continuar = True

while continuar:
	op = int(input("Ingrese el número de la figura a calcular:\n"
        "1. Triángulo\n"
        "2. Círculo\n"
        "3. Cuadrado\n"
        "4. Rombo\n"
        "5. Trapecio\n"
        "6. Salir\n\n"
        "[?]  "))

	match(op):
		case 1:
			a = float(input("Base del triángulo: "))
			b = float(input("Altura del triángulo: "))
			triangulo = Triangulo(a, b)
			print(triangulo)

		case 2:
			r = float(input("Radio del círculo: "))
			circulo = Circulo(r)
			print(circulo)

		case 3:
			l = float(input("Medida de un lado del cuadrado: "))
			cuadrado = Cuadrado(l)
			print(cuadrado)

		case 4:
			diagonal_mayor = float(input("Diagonal mayor del rombo: "))
			diagonal_menor = float(input("Diagonal menor del rombo: "))
			rombo = Rombo(diagonal_mayor, diagonal_menor)
			print(rombo)

		case 5:
			base_mayor = float(input("Base mayor del trapecio: "))
			base_menor = float(input("Base menor del trapecio "))
			altura = float(input("Altura del trapecio: "))
			trapecio = Trapecio(base_mayor, base_menor, altura)
			print(trapecio)

		case 6:
			continuar = False
			print('good bye...')