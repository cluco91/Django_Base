#Model Forms
from django import forms
from .models import Registrado

class RegistradoForm(forms.ModelForm):
	class Meta:
		model = Registrado
		#Campos que queremos ver en nuestro formulario
		fields = ["email", "nombre", "media"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		#validacion personalizada para el campo email
		#if not "edu" in email:
		#	raise forms.ValidationError("Por favor utilice email con la extension .edu")
		email_base, proveedor = email.split("@")
		dominio, extension = proveedor.split(".")
		if not extension == "edu":
			raise forms.ValidationError("Por favor utilice un email con la extension .edu")
		return email


#Django Forms
#from django import forms

# class RegForm(forms.Form):
# 	nombre_form = forms.CharField(max_length=100)
# 	edad = forms.IntegerField()