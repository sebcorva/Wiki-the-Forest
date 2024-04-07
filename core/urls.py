from django.urls import path
from .views import inicio, iniciar_sesion, cuenta, registro

urlpatterns = [
    path('inicio', inicio, name='inicio'), 
    path('', iniciar_sesion, name='iniciar_sesion'), #entre las comillas debe quedar vacio para que sea el primero en ser accedido
    path('cuenta', cuenta, name='cuenta'),
    path('registro', registro, name='registro'),
]
