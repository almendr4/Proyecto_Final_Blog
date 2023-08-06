from django import forms
from .models import Articulo   
from .models import Comment
# formulario articulo
class ArticuloForm(forms.ModelForm):
    class Meta: 
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria']


# formulario comentario
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']       