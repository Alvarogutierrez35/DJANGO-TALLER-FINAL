# Generated by Django 4.1.3 on 2022-12-17 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seminarioApp', '0005_alter_institucion_institucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscrito',
            name='institucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminarioApp.institucion'),
        ),
    ]
