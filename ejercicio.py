# -*- coding: utf-8 -*-

import json

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
num = int(raw_input("\n¿Cuantas palabras contiene el nombre del centro?: "))
cadena = raw_input("Introduzca una cadena por la que comience el nombre: ")
for line in doc[1:]:
	lineajson = json.loads(line)
	if lineajson["NOMBRE"].startswith(cadena):
		nombrepartido = lineajson["NOMBRE"].split(" ")
		if len(nombrepartido) == num:
			print "El centro " + lineajson["NOMBRE"] + " coincide con los criterios de busqueda."

#Introduce un tipo de centro y muestra el porcentaje de cuantos centros hay en las distintas localidades con respecto a las demas
tipo = raw_input("\nIntroduzca un tipo de centro: ")
ciudades = []
acumulador = 0
for line in doc[1:]:
	lineajson = json.loads(line)
	if lineajson["TIPO"] == tipo:
		acumulador = acumulador + 1
		if lineajson["LOCALIDAD"] not in ciudades:
			ciudades.append(lineajson["LOCALIDAD"])

for ciudad in ciudades:
	contador = 0
	for line in doc[1:]:
		lineajson = json.loads(line)
		if lineajson["TIPO"] == tipo and lineajson["LOCALIDAD"] == ciudad:
			contador = contador + 1
	print "La ciudad " + ciudad + " tiene el " + str((float(contador)*100.0)/float(acumulador)) + " por ciento de los centros de este tipo."

#Elige una localidad determinada, despues selecciona el tipo y por ultimo elige uno de los centros mostrados, del cual facilitaremos
#informacion para poder pedir cita o acceder al mismo
localidad = raw_input("Introduzca una localidad determinada: ")
tipos = []
lista = []
for line in doc[1:]:
	lineajson = json.loads(line)
	if lineajson["LOCALIDAD"] == localidad:
		lista.append(lineajson)
		if lineajson["TIPO"] not in tipos:
			tipos.append(lineajson["TIPO"])
acumulador = 0
print "Selecciona uno de los siguientes tipos: "
for tipo in tipos:
	print str(acumulador) + ") " + tipo
	acumulador = acumulador + 1
seleccion = int(raw_input("Introduzca un numero: "))
acumulador = 0
for centro in lista:
	if centro["TIPO"] == tipos[seleccion]:
		print str(acumulador) + ") " + centro["NOMBRE"]
		acumulador = acumulador + 1
seleccion = int(raw_input("Introduzca un numero: "))

print "El centro " + lista[seleccion]["NOMBRE"] + "esta situado en la localidad" + localidad
print "Su telefono es " + str(lista[seleccion]["TELEFONO"]) + " y su direccion es " + lista[seleccion]["DIRECCION"]