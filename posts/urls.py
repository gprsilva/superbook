from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('cbv-lista/', PostListView.as_view(), name='cbv-lista_posts'),
    path('lista-p/',PostListView.as_view(), name="lista_posts"),
    path('novo/', views.criar_post, name='criar_post'),
]