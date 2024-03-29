from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "app_site\home.html")

def historia(request):
    return render(request, "app_site\historia.html")

def tipos(request):
    return render(request, "app_site\\tipos.html")

def campeonatos(request):
    return render(request, "app_site\campeonatos.html")