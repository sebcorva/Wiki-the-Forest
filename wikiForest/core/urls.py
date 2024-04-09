from django.urls import path
from .views import inicio, login, logout_view

urlpatterns = [
    path('', inicio, name='inicio'), 
    path('accounts/login', login, name='login'), #entre las comillas debe quedar vacio para que sea el primero en ser accedido
    path('accounts/logout', logout_view, name="logout" ),
]
