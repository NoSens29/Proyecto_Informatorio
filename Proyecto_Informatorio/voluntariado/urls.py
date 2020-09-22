from django.contrib import admin
from django.urls import path, include
from voluntariado import views

urlpatterns = [
      path('', views.home ),

      path('Home', views.home, name = "Home"),

 #     path('login/', views.login, name ="login"),

 #     path('form_persona/', views.registrar_persona, name='form_persona'),

 #     path('registro/', views.registro, name ="registro"),     

 #     path('registrar_voluntario/', views.registrar_voluntario, name="registrar_voluntario"),
      
 #     path('registrar_solicitante/', views.registrar_solicitante, name ="solicitante"),

      path('Historiadefavores/', views.Historiadefavores, name="Historial"),  

      path('contacto/', views.contacto, name="Contacto"),  

      path('donaciones/', views.donaciones, name="donaciones"),

 #     path('registro_miusuario/', views.registro_miusuario, name="registro_miusuario"),

      path('login2/', views.login2, name="login2"),

      path('registro_actividad/', views.registro_actividad, name="registro_actividad"),

      path('registro_person/', views.registro_person, name="registro_person"),
]
