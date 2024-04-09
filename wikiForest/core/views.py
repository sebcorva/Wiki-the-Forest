from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)