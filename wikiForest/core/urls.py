from django.urls import path
from .views import inicio, iniciar_sesion

urlpatterns = [
    path('', inicio, name='inicio'), #entre las comillas debe quedar vacio para que sea el primero en ser accedido, decia inicio antes
    path('iniciar_sesion', iniciar_sesion, name='iniciar_sesion'),
]
