
from django.contrib import admin
from django.urls import path
from voluntariado import views

urlpatterns = [
      path('', views.home, name="Home"),
      path('home/', views.home, name="Home"),
      path('solicitante/', views.solicitud, name ="solicitante")
]
