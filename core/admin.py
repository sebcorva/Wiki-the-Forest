from django.contrib import admin
from core.models import Usuario

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['correo', 'clave']

admin.site.register(Usuario, UsuarioAdmin)