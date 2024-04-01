from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def iniciar_sesion(request):
    return render(request, 'core/iniciar_sesion.html')