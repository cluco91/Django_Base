from django.contrib import admin

from .forms import RegistradoForm
from .models import Registrado

# Registra tus modelos aqui.

class AdminRegistrado(admin.ModelAdmin):
	#Esta es la forma en que se vera nuestro modelo en la interfaz administrativa
	#Lista de Registrados, por el unicode que retorna email, el nombre y el timestamp
	#Puedo agregar más si lo deseo
	list_display = ["__str__", "nombre", "timestamp"]
	form = RegistradoForm
	#class Meta:
	#	model = Registrado


#Por ultimo registro Registrado y AdminRegistrado
admin.site.register(Registrado, AdminRegistrado)