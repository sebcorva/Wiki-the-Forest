from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)

    def __str__(self):
        return self.correo