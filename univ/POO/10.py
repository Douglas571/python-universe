# 

class Persona:
  def __init__(self, datos):
    self._nombre = datos['nombre']
    self._apellido = datos['apellido']
    self._cedula = datos['cedula']
    self._direccion = datos['direccion']
    self._telefono = datos['telefono']

  def __str__(self):
    msg = f'nombre: {self._nombre}\n'
    msg += f'apellido: {self._apellido}\n'
    msg += f'cedula: {self._cedula}\n'
    msg += f'direccion: {self._direccion}\n'
    msg += f'telefono: {self._telefono}\n'

    return msg

class App:
  def __init__(self):
    self.personas = []
    
  def regist_persona(self):
    print('[>] introdusca una nueva persona')

    datos = {}
    datos['nombre'] = input('[?] nombre: ')
    datos['apellido'] = input('[?] apellido: ')
    datos['cedula'] = input('[?] cedula: ')
    datos['direccion'] = input('[?] direccion: ')
    datos['telefono'] = input('[?] telefono: ')

    persona = Persona(datos)

    self.personas.append(persona)
    print('[!] registro exitoso!\n')

    print('[>] Los datos de la persona son:')
    print(persona)

  def run(self):
    self.regist_persona()

app = App()
app.run()