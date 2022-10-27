# motos

datos = [
  {
    'id': 1,
    'marca': 'motorola',
    'precio': 1000
  },
  {
    'id': 2,
    'marca': 'motomami',
    'precio': 2400
  },
  {
    'id': 3,
    'marca': 'blablacar',
    'precio': 100
  }
]

class Moto:
  def __init__(self, datos):
    self.set_id(datos['id'])
    self.set_marca(datos['marca'])
    self.set_precio(datos['precio'])

  def set_id(self, _id):
    self.id = _id

  def get_id(self):
    return self.id

  def set_marca(self, marca):
    self.marca = marca

  def get_marca(self):
    return self.marca

  def set_precio(self, precio):
    self.precio = precio

  def get_precio(self):
    return self.precio

  def __str__(self):
    msg = ''
    msg += f'  id: {self.get_id()}\n'
    msg += f'  marca: {self.get_marca()}\n'
    msg += f'  precio: {self.get_precio()}$\n'


    return msg

class TiendaMotos:
  def __init__(self):
    self.motos = []

    self.nombre = 'mimoto.com'
    self.tipo_de_motos = 'de juguete'

  def set_nombre(self, n):
    self.nombre = n

  def get_n(self):
    return self.nombre

  def set_tipo_de_motos(self, t):
    self.tipo_de_motos = t

  def get_tipo_de_motos(self):
    return self.tipo_de_motos

  def run(self):
    for d in datos:
      self.motos.append(Moto(d))

    print('Motos en venta:\n')
    for moto in self.motos:
      print(moto)

app = TiendaMotos()
app.run()