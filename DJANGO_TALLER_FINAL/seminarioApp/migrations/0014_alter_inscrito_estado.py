# Generated by Django 4.1.3 on 2022-12-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminarioApp', '0013_alter_inscrito_estado_alter_inscrito_institucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscrito',
            name='estado',
            field=models.IntegerField(choices=[['Reservado', 0], [1, 'Completada'], [2, 'Anulada'], [3, 'No asisten']]),
        ),
    ]
