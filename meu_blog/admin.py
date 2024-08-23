from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Eu)
class EuAdmin (admin.ModelAdmin):
     list_display=('nome','email','foto')

@admin.register(Sobre)
class SobreAdmin (admin.ModelAdmin):
     list_display= ('escola','curso')