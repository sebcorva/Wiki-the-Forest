from django.urls import path
from .views import inicio, iniciar_sesion

urlpatterns = [
    path('inicio', inicio, name='inicio'),
    path('iniciar_sesion', iniciar_sesion, name='iniciar_sesion'),
]
