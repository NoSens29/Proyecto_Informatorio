# Generated by Django 3.1.1 on 2020-09-23 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('tu_nombre', models.CharField(max_length=60)),
                ('tu_direccion_de_correo', models.EmailField(max_length=254)),
                ('tu_mensaje', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('dni', models.IntegerField()),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=100)),
                ('administrador', models.BooleanField()),
                ('voluntario', models.BooleanField(blank=True, null=True)),
                ('solicitante', models.BooleanField(blank=True, null=True)),
                ('contrasenia', models.CharField(default='usuario', max_length=60)),
                ('usuario', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('administrador', models.BooleanField(blank=True, default=False, null=True)),
                ('voluntario', models.BooleanField(blank=True, null=True)),
                ('solicitante', models.BooleanField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('fecha', models.DateField()),
                ('realizada', models.BooleanField()),
                ('id_solicitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actividadesSol', to='voluntariado.person')),
                ('id_voluntario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actividadesVol', to='voluntariado.person')),
            ],
        ),
    ]
