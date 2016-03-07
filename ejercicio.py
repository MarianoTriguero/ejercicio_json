# -*- coding: utf-8 -*-

import json
from pprint import pprint

f=open("CentrosSanitarios.json","r")
doc = f.readlines()
acum = 1

#Haz una lista con los nombres y las localidades de los respectivos centros de salud de Navarra
for line in doc[1:]:
	lineajson = json.loads(line)
	nombre = lineajson["NOMBRE"]
	nombre = nombre.encode('UTF-8')
	localidad = lineajson["LOCALIDAD"]
	localidad = localidad.encode('UTF-8')
	print "----------------\nCentro Nº" + str(acum)
	print "Nombre del centro de salud: " + nombre
	print "Localidad: " + localidad
	acum = acum + 1

#Muestra cuantos centros de salud hay por categorias
print "\nCentros de salud por categorias"
tipos = []
for line in doc[1:]:
	lineajson = json.loads(line)
	tipo = lineajson["TIPO"]
	if tipo not in tipos:
		tipos.append(tipo)

for tipo in tipos:
	acum = 0
	for line in doc[1:]:
		lineajson = json.loads(line)
		if tipo == lineajson["TIPO"]:
			acum = acum + 1
	print "Hay " + str(acum) + " centros del tipo " + tipo

#Muestra los centros de salud cuyo nombre contenga un numero determinado de palabras y empiecen por una cadena determinada
num = int(raw_input("¿Cuantas palabras contiene el nombre del centro?: "))
cadena = raw_input("Introduzca una cadena por la que comience el nombre: ")
for line in doc[1:]:
	lineajson = json.loads(line)
	if lineajson["NOMBRE"].startswith(cadena):
		nombrepartido = lineajson["NOMBRE"].split(" ")
		if len(nombrepartido) == num:
			print "El centro " + lineajson["NOMBRE"] " coincide con los criterios de busqueda."