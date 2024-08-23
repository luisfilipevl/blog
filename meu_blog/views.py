from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    eulis = Eu.objects.all() # Select do django
    informacoes = {
        'lista': eulis,
    }
    return render(request, 'index.html',informacoes)

def sobre_me(request):
    sobrelis = Sobre.objects.all() # Select do django
    informacoes_sobre = {
        'lista': sobrelis,
    }
    return render(request, 'sobre.html',informacoes_sobre)