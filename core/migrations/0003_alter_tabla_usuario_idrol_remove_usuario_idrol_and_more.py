# Generated by Django 5.0.3 on 2024-04-06 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tabla_rol_tabla_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabla_usuario',
            name='idRol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tabla_rol'),
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='idRol',
        ),
        migrations.RenameField(
            model_name='tabla_usuario',
            old_name='Clave',
            new_name='clave',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
