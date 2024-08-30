from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    eulis = Eu.objects.all() 
    informacoes = {
        'lista': eulis,
    }
    return render(request, 'index.html',informacoes)

def sobre_me(request):
    eulis = Eu.objects.all() 
    informacoes = {
        'lista': eulis,
    }
    return render(request, 'sobre.html',informacoes)
