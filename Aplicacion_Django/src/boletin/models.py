from django.db import models

# Aqui se crean los modelos
#La clase Registrado en models hereda de clase Model

#Registrado es una Tabla de nuestra db
class Registrado(models.Model):
	#Aqui definimos campos o atributos
	nombre = models.CharField(max_length=120, blank=True, null=True)#models y tipo de dato
	email = models.EmailField()
	codigo_postal = models.IntegerField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)
	media = models.FileField(upload_to='myfolder/', blank=True, null=True) #barra / debe ir despues del nombre de carpeta

	#No olvide definir el Unicode, este es para python 3, el de python 2.x es __unicode__
	def __str__(self):
		return self.email
