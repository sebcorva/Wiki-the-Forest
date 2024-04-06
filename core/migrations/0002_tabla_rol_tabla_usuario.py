# Generated by Django 5.0.3 on 2024-04-06 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabla_Rol',
            fields=[
                ('idRol', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion rol')),
            ],
        ),
        migrations.CreateModel(
            name='Tabla_Usuario',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('Clave', models.CharField(max_length=50, verbose_name='Clave')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo')),
                ('idRol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rol')),
            ],
        ),
    ]