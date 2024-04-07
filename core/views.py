from django.shortcuts import render
from .models import Tabla_Usuario
from .forms import UserForm

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')

def registro(request):
    datos = {
        'form' : UserForm()
    }
    if request.method=='POST':
        formulario =UserForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Usuario creado exitosamente"

    return render(request, 'registro.html', datos)

def cuenta(request):
    usuario = Tabla_Usuario.objects.all()
    datos = {
        'usuario': usuario
    }
    return render(request, 'cuenta.html', datos)
