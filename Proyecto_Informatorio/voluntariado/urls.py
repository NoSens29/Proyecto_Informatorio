
from django.contrib import admin
from django.urls import path
from voluntariado import views

urlpatterns = [
      path('', views.home, name="Home"),
 #     path('home/', views.home, name="Home"),
<<<<<<< HEAD
      path('registrar_voluntario/', views.registrar_voluntario, name='registrar_voluntario'),
      path('form_persona/', views.registrar_persona, name='form_persona'),
=======
      path('registro/', views.registro),
      path('login/', views.login),
      path('registro/', views.registrar_voluntario, name='registrar_voluntario'),
      path('registro/', views.registrar_solicitante, name='registrar_solicitante')
>>>>>>> master
]
