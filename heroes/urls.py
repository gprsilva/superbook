from django.urls import path
from .views import HeroListView
from . import views

urlpatterns = [
    path('cbv-lista/', HeroListView.as_view(), name='cbv_lista_herois'),
    path('lista-h/',HeroListView.as_view(), name="lista_herois"),
    path('contato/', views.contato_view , name='contato'),
    path('novo/', views.criar_heroi, name='criar_heroi'),
]