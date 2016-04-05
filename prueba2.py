import math 
t = "%(nombre)s sabe %(idiomas)i idiomas"

v = [{'nombre':'Naomi', 'idiomas':5},
    {'nombre':'Jaime', 'idiomas':3}]
print "*************** DICCIONARIO COMPLETO ***************\n"
for persona in v:
    print t % persona 


print "\n*************** CAMPO A BUSCAR DEL DICCIONARIO ***************\n"

def buscar (nombre):
		if persona['nombre'] == nombre:
			print t % persona
		else:
			print "El nombre no esta en el diccionario"

buscar('Jaime')