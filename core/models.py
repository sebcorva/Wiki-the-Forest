from django.db import models


class Tabla_Rol(models.Model):
    idRol = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, verbose_name="Descripcion rol")

class Tabla_Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    clave = models.CharField(max_length=50, verbose_name="Clave")
    correo = models.CharField(max_length=50, verbose_name="Correo")
    idRol = models.ForeignKey(Tabla_Rol, on_delete=models.CASCADE) 