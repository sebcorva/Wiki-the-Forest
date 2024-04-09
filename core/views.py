from django.shortcuts import render
from django.contrib.auth import logout
from core.models import Usuario
from core.forms import IniciarForm, RegistroForm

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)

def cuenta(request):
    context = {}
    usuarios = Usuario.objects.all()
    context['usuarios'] = usuarios
    return render(request, 'cuenta.html', context)

def registro(request):
    context = {}
    formRegistro = RegistroForm()
    context['formRegistro'] = formRegistro
    if request.method == 'POST':
        if 'guardar' in request.POST:
            formRegistro = RegistroForm(request.POST)
            formRegistro.save()
    return render(request, 'registro.html', context)