from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')