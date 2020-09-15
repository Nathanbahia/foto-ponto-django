from django.contrib import admin
from .models import Ponto


@admin.register(Ponto)
class PontoAdmin(admin.ModelAdmin):
    list_display = ['data', 'nome', 'foto']
