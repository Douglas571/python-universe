# Ejercicio #1 
# Douglas Socorro 29.748.656

class Vehiculo:
    def __init__(self, modelo, precio, color, descripcion):
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.descripcion = descripcion

    def __str__(self):
        msg = "Modelo: " + self.modelo + "\n"
        msg += "Precio: " + self.precio + "$" + "\n"
        msg += "Color: " + self.color + "\n"
        msg += "Descripción: " + self.descripcion + "\n"
        return msg


class Auto(Vehiculo):
    def __init__(self, modelo, precio, color, descripcion, puertas):
        super().__init__(modelo, precio, color, descripcion)
        self.puertas = puertas

    def __str__(self):
        msg = '\n Auto' + "\n"
        msg += super().__str__()
        msg += "Puertas: " + self.puertas + "\n"

        return msg      

class Moto(Vehiculo):
    def __init__(self, modelo, precio, color, descripcion, tipo):
        super().__init__(modelo, precio, color, descripcion)
        self.tipo = tipo

    def __str__(self):
        msg = '\n Moto' + "\n"
        msg += super().__str__()
        msg += "Tipo: " + self.tipo + "\n"

        return msg

print('\n-------- Auto ----------')

modelo_auto = input("Modelo del auto: ") or 'n/a'
precio_auto = input("Precio del auto: ") or 'n/a'
color_auto = input("Color del auto: ") or 'n/a'
descripcion_auto = input("Descripción del auto: ") or 'n/a'
num_puertas = input("Número de puertas: ") or 'n/a'

print('\n-------- Moto ----------')

modelo_moto = input("Modelo de la moto: ") or 'n/a'
precio_moto = input("Precio de la moto: ") or 'n/a'
color_moto = input("Color de la moto: ") or 'n/a'
descripcion_moto = input("Descripción de la moto: ") or 'n/a'
tipo_moto = input("Cilindrada de la moto: ") or 'n/a'

auto = Auto(modelo_auto, precio_auto, color_auto, descripcion_auto, num_puertas)
moto = Moto(modelo_moto, precio_moto, color_moto, descripcion_moto, tipo_moto)

print(auto)
print(moto)