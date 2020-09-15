
from django.contrib import admin
from django.urls import path
from voluntariado import views

urlpatterns = [
      path('', views.home ),

      path('Home', views.home, name = "Home"),
 #     path('home/', views.home, name="Home"),
<<<<<<< HEAD
      path('login/', views.login),
      path('registro/', views.registro),
      path('registro/', views.registrar_voluntario, name='registrar_voluntario'),
      path('registro/', views.registrar_solicitante, name='registrar_solicitante')
=======

 	  path('login/', views.login, name ="login"),

      path('registro/', views.registro, name ="registro"),     

      path('registrar_voluntario/', views.registrar_voluntario, name="registrar_voluntario"),
      
      path('registrar_solicitante/', views.registrar_solicitante, name ="solicitante"),

      path('Historiadefavores/', views.Historiadefavores, name="Historial"),  

      path('contacto/', views.contacto, name="Contacto"),  

      path('donaciones/', views.donaciones, name="donaciones"),  

      

>>>>>>> origin
]
