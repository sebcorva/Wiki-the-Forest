from django import forms
from core.models import Usuario

class IniciarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['correo', 'clave']

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'clave']