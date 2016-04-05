class Persona():

    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def __str__(self):
        return "nombre: "+self.nombre+" "+self.apellidos + ", "+str(self.edad)

    @property
    def mayor_edad(self):
        return self.edad >= 18
            
class Alumno(Persona):

    def __init__(self, nombre, apellidos, edad, asignatura):
        super().__init__(nombre, apellidos, edad)
        self.asignatura = asignatura

    def __str__(self):
        return super().__str__() + " asignatura que estudia: "+self.asignatura

def agregar(numero, bbdd=[]):
    for i in range(numero):
        nombre = str(input("Introduce un nombre: "))
        apellidos = str(input("Introduce los apellidos: "))
        edad = int(input("Introduce la edad: "))
        asignatura = str(input("Introduce asignatura: "))
        bbdd.append(Alumno(nombre, apellidos, edad, asignatura))

    return bbdd
def mostrar_adultos(bbdd):
    for o in bbdd:
        if o.mayor_edad:
            print(o)


def mostrar(bbdd):
    for o in bbdd:
        print(o)

bbdd = [
        Alumno('Angela', 'Manero', 23, "PHP"), 
        Alumno('Jaime', 'de Corti', 19, "JAVA"), 
        Alumno('Ayoub', 'Laarourssi', 17, "JSP"),
        Alumno('Naomi', 'Porto', 14, "JAVASCRIPT")
]

numero = int(input("Introduce el numero de alumnos que va a añadir: "))
bbdd = agregar(numero,bbdd)
print("*************** Lista entera ***************")
mostrar(bbdd)
print("*************** Mayores de edad ***************")
mostrar_adultos(bbdd)