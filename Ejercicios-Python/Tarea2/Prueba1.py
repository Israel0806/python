class Alumno:
    def __init__(self,codigo,nombre,email,semestre):
        self.codigo=codigo
        self.nombre=nombre
        self.email=email
        self.semestre=semestre


class Profesor:
    def __init__(self,codigo,nombre,email,categoria):
        self.codigo=codigo
        self.nombre=nombre
        self.email=email
        self.categoria=categoria

class Escuela(Alumno,Profesor):
    def __init__(self,nombre):
        self.nombre=nombre
        self.numProfe=0
        self.numAlum=0
        self.profesores=[]
        self.alumnos=[]

    def agregarProf(self,prof):
        self.profesores.append(prof)
        self.numProfe+=1

    def agregarAlum(self,alum):
        self.alumnos.append(alum)
        self.numAlumn+=1
        
class Facultad:
    def __init__(self,nombre):
        self.nombre=nombre
        self.numEscu=0
        self.escuelas=[]

    def agregarEscu(self,escu):
        self.escuelas.append(escu)
        self.numEscu+=1
        
class Universidad:
    def __init__(self,nombre):
        self.nombre=nombre
        self.numFacul=0
        self.facultades=[]

    def agregarFacul(self,facul):
        self.facultades.append(facul)
        self.numFacul+=1
        
alumno1=Alumno
