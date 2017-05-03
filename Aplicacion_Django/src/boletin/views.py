from django.shortcuts import render
from .forms import RegistradoForm
from .models import Registrado
#from .forms import RegistradoForm

# Crea tus vistas aqui.

#Pagina Principal

#inicio.html es el template, y {} representa un diccionario vacio
#un diccionario sirve para pasar variables al url en cuestion

def inicio(request):
	titulo = "Bienvenidos"
	form = RegistradoForm(request.POST or None, request.FILES or None)
	#request.FILES or None, es para requerir archivos

	#Variable para Queryset
	queryset = Registrado.objects.all() #Lista de todas las instancias de nuestra clase modelo

	for obj in queryset:
		print(obj.nombre)
		print(obj.email)
		print(obj.id)#numero de identificacion de cada objeto, el id es automatico
		#Y podemos modificarlo si queremos 

	context = {
		"titulo":titulo,
		"form":form,
		"queryset":queryset
	}

	#Si el formulario a enviar es valido
	if form.is_valid():
		instance = form.save(commit=False)
		#Si es true, se guarda de inmediato a la base de datos
		#Aun no se guarda
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		form.save() 
		#Ahora se guarda

		#Segundo diccionario de contexto para cuando se guardan los datos a la db
		context = {
			"titulo": "Gracias %s, ya se ha registrado." %(nombre)
		}
		if not nombre:
			context = {
				"titulo": "Gracias %s, ya se ha registrado." %(email) 
			}

		# print (instance)
		# print (instance.timestamp)

	#Si no lleva (request.POST) no se validará

	# if request.user.is_authenticated():
	# 	titulo = "Hola, %s!" %(request.user) 
		#%s es un string substitution

	# #En el contexto yo coloco lo que voy a pasar al template
	# context = {
	# 	"titulo_template":titulo,
	# 	"form":form
	# }

	"""
	#Este form es para asociar el formulario a esta vista
	form = RegForm(request.POST or None)
	#El request.POST, es para validar la informacion del formulario
	#Con None evitamos duplicacion de mensajes
	
	#Diccionario de contexto
	context = {
		"form": form
	}


	#Validacion
	if form.is_valid():
		#form_dicc = form.cleaned_data
		#print(form_dicc.get("nombre"))#Si quieron que en el cmd me muestre solo nombre enviado
		#print (form.cleaned_data)
		form_data = form.cleaned_data
		abc = form_data.get("nombre_form")
		#Lo capturo del formulario
		obj = Registrado.objects.create(nombre=abc)
		#create es para crear y guardar en la base de datos

		#Estas 3 lineas de codigo tambien pueden guardar los datos en la db
		#obj2 = Registrado()
		#obj2.nombre = abc
		#obj2.save()
	"""

	return render(request, "inicio.html", context)
	#return render(request, "inicio.html", {})


#Nueva Vista => Sobre

def sobre(request):
	titulo = "Sobre Nosotros"

	context = {
		"titulo":titulo,
	}

	return render(request, "sobre.html", context)

