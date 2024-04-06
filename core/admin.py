from django.contrib import admin

# Register your models here.
from .models import Tabla_Rol, Tabla_Usuario

admin.site.register(Tabla_Usuario)
admin.site.register(Tabla_Rol)