
from django.contrib import admin
from django.urls import path
from voluntariado import views

urlpatterns = [
      path('', views.home, name="Home"),
 #     path('home/', views.home, name="Home"),
      path('registrar_voluntario/', views.registrar_voluntario, name='registrar_voluntario'),
      path('registrar_solicitante/', views.registrar_solicitante, name='registrar_solicitante')
]
