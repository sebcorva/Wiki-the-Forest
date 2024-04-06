from django.forms import ModelForm
from .models import Tabla_Usuario

class UserForm(ModelForm):
    class Meta:
        model = Tabla_Usuario
        fields = ['idUsuario','nombre', 'apellido', 'clave', 'correo', 'idRol']