
from django.contrib import admin
from django.urls import path
from voluntariado import views

urlpatterns = [
      path('', views.home, name="Home"),
 #     path('home/', views.home, name="Home"),
      path('login/', views.login),
      path('registro/', views.registro),
      path('registro/', views.registrar_voluntario, name='registrar_voluntario'),
      path('registro/', views.registrar_solicitante, name='registrar_solicitante')
]
