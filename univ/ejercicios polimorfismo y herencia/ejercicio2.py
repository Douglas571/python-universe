# Ejercicio #2 
# Douglas Socorro 29.748.656

class Persona:
    def __init__(self, nombre, apellido, edad, cargo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cargo = cargo
        self.telefono = telefono
    
    def __str__(self):

        msg = "Nombre: " + self.nombre + '\n'
        msg += "Apellido: " + self.apellido + '\n'
        msg += "Edad: " + str(self.edad) + '\n'
        msg += "Cargo: " + self.cargo + '\n'
        msg += "Telefono: " + self.telefono + '\n'

        return msg

class Jugador(Persona):
    def __init__(self, nombre, apellido, edad, cargo, telefono, posicion):
        super().__init__(nombre, apellido, edad, cargo, telefono)
        self.posicion = posicion
    
    def __str__(self):
        msg = '--- Jugador ---' + '\n'
        msg += super().__str__()
        msg += "Posicion: " + self.posicion + '\n'

        return msg
        
class Entrenador(Persona):
    def __init__(self, nombre, apellido, edad, cargo, telefono, posicion):
        super().__init__(nombre, apellido, edad, cargo, telefono)
        self.posicion = posicion

    def set_entrenamiento(self, tipo, horario):
        self.tipo = tipo
        self.horario = horario
    
    def __str__(self):
        msg =  '--- Entrenador ---' + '\n'
        msg += super().__str__()

        if (self.tipo and self.horario):
            msg += "Entrenamiento: " + self.tipo + ' - ' + self.horario + '\n'

        return msg
        
class Asistente(Persona):
    def __init__(self, nombre, apellido, edad, cargo, telefono, funcion='n/a'):
        super().__init__(nombre, apellido, edad, cargo, telefono)           
        self.funcion = funcion           

    def set_funcion(self, funcion):
        self.funcion = funcion
    
    def __str__(self):
        msg =  '--- Asistente ---' + '\n'
        msg += super().__str__()
        msg += "Funcion: " + self.funcion + '\n'

        return msg
        
jugadorA = Jugador("Mandinga", "Pirona", 20, "Jugador", "412434134", "ni idea")
jugadorB = Jugador("Paquitos", "Maguire ", 10, "Jugador", "343423423", "null")

entrenador = Entrenador("Ashley", "Frangipane", 26, "Entrenadora", "unknow", "Ladilladora")    
entrenador.set_entrenamiento('Correr por la playa', 'de 7 a 8')

asistente = Asistente("Harry", "Styles", 27, "Asistente", "unknow")
asistente.set_funcion('Animar a la gente')

print(jugadorA)
print(jugadorB)
print(entrenador)
print(asistente)