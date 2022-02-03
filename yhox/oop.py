class Ave:
	def volar(self):
		return "no todas las aves pueden volar."

class Pinguino(Ave):
	def volar(self):
		return "no puedo volar, soy un Pinguino"

class Aguila(Ave):
	def volar(self):
		return "a volar!! soy un aguila"	

class Gallina(Ave):
	def volar(self):
		return "medio vuelo, dame gusanos"	

aves = [Pinguino(), Aguila(), Gallina()]
for ave in aves:
	print(ave.volar)

