import sys

from modelos.alumno import Alumno
from modelos.persona import Persona


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

try:
    numero = int(input("Introduce el numero de alumnos que va a añadir: "))
except Exception:
    print("Introduce un numero")
    sys.exit()

bbdd = agregar(numero,bbdd)
print("*************** Lista entera ***************")
mostrar(bbdd)
print("*************** Mayores de edad ***************")
mostrar_adultos(bbdd)