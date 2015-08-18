class Estrella():
	def __init__(self, RA, DEC, Tipo):
		self.observaciones = []
		self.RA = RA
		self.DEC = DEC	
		self.tipo = Tipo

	def agregarObservacion(self,observacion):
		self.observaciones.append(observacion)

	def calcularpromedio(self):
		suma = 0
		for observacion in self.observaciones:
			suma += observacion.magnitud
		promedio = suma/len(self.observaciones)
		return  promedio

	def calcularvarianza(self,promedio):
		suma = 0
		for observacion in self.observaciones:
			suma += (observacion.magnitud - promedio)**2
		varianza = suma/len(self.observaciones)
		return varianza

class Observacion():
	def __init__(self,tiempo,magnitud,error):
		self.tiempo= tiempo
		self.magnitud = magnitud
		self.error = error

class Cielo():
	def __init__(self):
		self.fields = []

	def agregarfield(self,field):
		self.fields.append(field)

class Field():
	def __init__(self):
		self.estrellas = []

	def agregarEstrella(self,estrella):
		self.estrellas.append(estrella)



observacion1 = Observacion(8,3,15)
observacion2 = Observacion(5,8,19)

estrella1 = Estrella(5,7,'Mira')
estrella2 = Estrella(6,6,'Mira')
estrella3 = Estrella(7,5,'Mira')
estrella4 = Estrella(8,4,'Mira')
estrella5 = Estrella(9,3,'Mira')
estrella6 = Estrella(10,2,'Mira')

field1 = Field()
field2 = Field()

field1.agregarEstrella(estrella1)
field1.agregarEstrella(estrella2)
field1.agregarEstrella(estrella3)

field2.agregarEstrella(estrella4)
field2.agregarEstrella(estrella5)
field2.agregarEstrella(estrella6)

estrella1.agregarObservacion(observacion1)
estrella1.agregarObservacion(observacion2)

cielo1 = Cielo()

cielo1.agregarfield(field1)
cielo1.agregarfield(field2)

print(estrella1.calcularpromedio())

print(estrella1.calcularvarianza(estrella1.calcularpromedio()))


for field in cielo1.fields:
	for estrella in field.estrellas:
		print(estrella.tipo)







