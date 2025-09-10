from django import forms
from .models import Villain


# Nome Aluno: Guilherme Pereira Ruiz da Silva

class VillainForm(forms.ModelForm):
    class Meta:
        model = Villain
        fields = ['codinome', 'nome_real', 'poder_principal' ,'cidade', 'historia']
    