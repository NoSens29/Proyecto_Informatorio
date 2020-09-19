# Generated by Django 2.1.5 on 2020-09-07 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='id_solicitante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actividadesSol', to='voluntariado.Persona'),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='id_voluntario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actividadesVol', to='voluntariado.Persona'),
        ),
    ]
