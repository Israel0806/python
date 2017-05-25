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
        print ''

num = input('Ingrese la cantidad de medicos: ')
medicos = []

for i in range(0,num):
    print 'Ingrese datos del medico: ', i+1
    cod = raw_input('Ingrese Codigo: ')
    nom = raw_input('Ingrese Nombre: ')
    esp = raw_input('Ingrese Especialidad: ')
    hor = raw_input('Ingrese Horario: ')
    med = Medico(cod,nom,esp,hor)
    medicos.append(med)

print ''
print 'El listado de medicos ingresados es: '
print ''
for medi in medicos:
    medi.imprimir()
