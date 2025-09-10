from django import forms
from .models import Post


# Nome Aluno: Guilherme Pereira Ruiz da Silva
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
    