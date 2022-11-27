# Ejercicio #3 
# Douglas Socorro 29.748.656

class PersonalUniversitario:
    def __init__(self, ID, nombre, email):
        self.datos = {
            'id': str(ID), 
            'nombre': nombre, 
            'email': email
        }
    
    def __str__(self):
        msg = 'ID: ' + self.datos['id'] + '\n'
        msg += 'Nombre: ' + self.datos['nombre'] + '\n'
        msg += 'E-mail: ' + self.datos['email'] + '\n'
        
        return msg

class Oficina(PersonalUniversitario):
    def __init__(self, ID, nombre, email, puesto):
        super().__init__(ID, nombre, email)
        self.datos['puesto'] = puesto

    def __str__(self):
        msg = 'Personal de oficina' + '\n'
        msg += super().__str__()
        msg += "Puesto: " + self.datos['puesto'] + "\n"

        return msg

class Profesor(PersonalUniversitario):
    def __init__(self, ID, nombre, email, especializacion):
        super().__init__(ID, nombre, email)
        self.datos['especializacion'] = especializacion

    def __str__(self):
        msg = 'Profesor' + '\n'
        msg = super().__str__()
        msg += "Especialidad: " + self.datos['especializacion'] + "\n"

        return msg        

class Alumno(PersonalUniversitario):
    def __init__(self, ID, nombre, email, creditos_aprobados):
        super().__init__(ID, nombre, email)
        self.datos['creditos_aprobados'] = creditos_aprobados

    def __str__(self):
        msg = 'Alumno' + '\n'
        msg += super().__str__()
        msg += "Créditos aprobados: " + self.datos['creditos_aprobados'] + "\n"

        return msg        

oficinista = Oficina(1, 'Angela Castillo', 'angelaCast@gmail.com', 'Decanato')
docente = Profesor(2, 'Jepsenia Avila', 'jepsi@gmail.com', 'Analista')
estudiante = Alumno(3, 'Douglas Socorro', 'douglassocorro1@gmail.com', '90')

print('Acontinuación, se mostrarán los datos del personal univesitario...\n')
print(oficinista)
print(docente)
print(estudiante)