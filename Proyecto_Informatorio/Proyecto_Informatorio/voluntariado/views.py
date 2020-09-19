from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):

	return render(request, "voluntariado/home.html")

def solicitud(request):

	return render(request, "voluntariado/solicitante.html")
