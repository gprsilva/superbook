from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Villain
from .forms import VillainForm

# def lista_herois(request):
#     herois = Hero.objects.all()  # busca todos os heróis do banco
#     return render(request, "heroes/lista_herois.html", {"herois": herois})

class VillainListView(ListView):
    model = Villain
    template_name = "villains/lista_viloes.html"
    context_object_name = "viloes"


def criar_villain(request):
    if request.method == "POST":
        form = VillainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_viloes')
    else:
        form = VillainForm()

    return render(request, "villains/form_viloes.html", {"form": form})