class Medico:
    def __init__(self, codigo, nombre, especialidad, horario):
        self.codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad
        self.horario = horario

    def imprimir(self):
        print 'Los datos del medico son:'
        print 'Codigo: ', self.codigo
        print 'Nombre: ', self.nombre
        print 'Especialidad: ', self.especialidad
        print 'Horario: ', self.horario

class Paciente:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def imprimir(self):
        print 'Los datos del paciente son:'
        print 'Codigo: ', self.codigo
        print 'Nombre: ', self.nombre

class Cita:
    def __init__(self, codigo, medico, paciente, consultorio):
        self.codigo = codigo
        self.medico = medico
        self.paciente = paciente
        self.consultorio = consultorio

    def imprimir(self):
        print 'Los datos de la cita son:'
        print 'Codigo: ', self.codigo
        print 'Consultorio: ', self.consultorio
        self.medico.imprimir()
        self.paciente.imprimir()
        print ''

med1 = Medico('001','Juan Gutierrez','Oftalmologia','07-12')
med2 = Medico('002','Cesar Jimenez','Medicina Interna','13-18')

pac1 = Paciente('001','Jorge Benitez')
pac2 = Paciente('002','Luis Fernandez')

cita1 = Cita('001',med1,pac2,302)
cita2 = Cita('002',med2,pac1,305)

cita1.imprimir()
cita2.imprimir()

