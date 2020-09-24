from django import forms
from .models import Ponto


class PontoForm(forms.ModelForm):
    class Meta:
        model = Ponto
        fields = ['matricula', 'aves', 'foto', 'latitude', 'longitude']
