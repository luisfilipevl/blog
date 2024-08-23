from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    eulis = Eu.objects.all() # Select do django
    informacoes = {
        'lista': eulis,
    }
    return render(request, 'index.html',informacoes)