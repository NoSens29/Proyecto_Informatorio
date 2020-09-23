from django.db import models

from django import forms

from django.contrib.auth.models import User
# Create your models here.


class Persona(models.Model):
	id = models.IntegerField(primary_key = True, editable=False)
	dni = models.IntegerField()
	nombre = models.CharField(max_length=60)
	apellido = models.CharField(max_length=60)
	telefono = models.CharField(max_length=20)
	mail = models.EmailField()
	direccion = models.CharField(max_length=100)
	administrador = models.BooleanField()
	voluntario = models.BooleanField(null=True, blank=True)
	solicitante = models.BooleanField(null=True, blank=True)
	contrasenia = models.CharField(max_length=60, default="usuario")
	usuario = models.CharField(max_length=20)

	def __str__(self):
		return (self.nombre + ', '+self.apellido)


class Actividad(models.Model):
	id = models.IntegerField(primary_key=True, editable=False)
	nombre = models.CharField(max_length=60)
	fecha = models.DateField()
	realizada = models.BooleanField()
	id_solicitante = models.ForeignKey('Person', on_delete = models.SET_NULL, null=True, blank=True, related_name = 'actividadesSol')
	id_voluntario = models.ForeignKey('Person', on_delete = models.SET_NULL, null=True, blank=True, related_name = 'actividadesVol')
	
	def __str__(self):
		return (self.nombre + ' Fecha: '+str(self.fecha))


class Person(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	dni = models.IntegerField()
	telefono = models.CharField(max_length=20, null=True, blank=True)
	direccion = models.CharField(max_length=100, null=True, blank=True)
	administrador = models.BooleanField(null=True, blank=True, default=False)
	voluntario = models.BooleanField(null=True, blank=True)
	solicitante = models.BooleanField(null=True, blank=True)

	def __str__(self):

		return (self.user.username + ' solicitante: '+str(self.solicitante) + ', voluntario: '+str(self.voluntario))


class Contacto(models.Model):
	id = models.IntegerField(primary_key= True, editable= False)
	tu_nombre = models.CharField(max_length=60)
	tu_direccion_de_correo = models.EmailField()
	tu_mensaje = models.TextField(max_length=200)

    
	def __str__(self):
		
		return (self.tu_nombre) 