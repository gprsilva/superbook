from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('cbv-lista/', PostListView.as_view(), name='cbv-lista_posts'),
    path('lista-p/',PostListView.as_view(), name="lista_posts"),
    path('novo/', PostCreateView.as_view(), name='criar_post'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='editar_post'),
    path('<int:pk>/excluir/', PostDeleteView.as_view(), name='excluir_post'),
]