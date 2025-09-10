from django.urls import path
from .views import VillainListView
from . import views

urlpatterns = [
    path('lista-v/',VillainListView.as_view(), name="lista_viloes"),
    path('novo/', views.criar_villain, name='criar_vilao'),
]