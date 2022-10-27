# Casas

class Casa:
  def __init__(self):
    pass

  def set_id(self, _id):
    self.id = _id

  def get_id(self):
    return self.id

  def set_direccion(self, direccion):
    self.dir = direccion

  def get_direccion(self):
    return self.dir

  def set_cuartos(self, cuartos):
    self.cuartos = cuartos

  def get_cuartos(self):
    return self.cuartos

  def set_tamanyo(self, tamanyo):
    self.tamanyo = tamanyo

  def get_tamanyo(self):
    return self.tamanyo

  def set_precio_venta(self, precio_venta):
    self.precio_venta = precio_venta

  def get_precio_venta(self):
    return self.precio_venta

  def set_precio_compra(self, precio_compra):
    self.precio_compra = precio_compra

  def get_precio_compra(self):
    return self.precio_compra

  def __str__(self):
    msg = ''
    msg += f'  id: {self.get_id()}\n'

    msg += f'  direccion: {self.get_direccion()}\n'
    msg += f'  tamanyo: {self.get_tamanyo()}\n'
    msg += f'  numero de cuartso: {self.get_cuartos()}\n' 
    msg += f'  precio de venta: {self.get_precio_venta()}\n'
    msg += f'  precio de compra: {self.get_precio_compra()}\n'

    return msg

datos = [
  {
    'id': 90123984,
    'dir': 'delicias 1',
    'cuartos': 2,
    'tamanyo': 45,

    'precio_venta': '10$',
    'precio_compra': '40$',
  },
  {
    'id': 134897323,
    'dir': 'delicias 2',
    'cuartos': 4,
    'tamanyo': 50,

    'precio_venta': '10$',
    'precio_compra': '40$',
  },
  {
    'id': 1983409324,
    'dir': 'delicias 5',
    'cuartos': 3,
    'tamanyo': 60,

    'precio_venta': '10$',
    'precio_compra': '40$',
  }
]

casas = []

for c in datos:
  casa = Casa()

  casa.set_id(c['id'])
  casa.set_direccion(c['dir'])
  casa.set_tamanyo(c['tamanyo'])
  casa.set_cuartos(c['cuartos'])

  casa.set_precio_venta(c['precio_venta'])
  casa.set_precio_compra(c['precio_compra'])

  casas.append(casa)

print('Casas en venta: \n')
for casa in casas:
  print(casa)


  