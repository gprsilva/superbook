from django.urls import path
from .views import PostListView

urlpatterns = [
    path('cbv-lista/', PostListView.as_view(), name='cbv-lista_posts'),
    path('lista-p/',PostListView.as_view(), name="lista_posts")
]