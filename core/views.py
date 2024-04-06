from django.shortcuts import render
from .models import Tabla_Usuario
from .forms import UserForm

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')

def cuenta(request):
    usuario = Tabla_Usuario.objects.all()
    datos = {
        'usuario': usuario
    }
    return render(request, 'cuenta.html', datos)
