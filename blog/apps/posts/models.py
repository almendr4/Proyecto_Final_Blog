from django.db import models
from django.utils import timezone
# Create your models here.
import random
import os
from functools import partial


#Categoria:
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
# Post
class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoria')
    imagen = models.ImageField(null=True, blank=True, upload_to='post', default='static/post_default.png')
    publicado = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parent = False):
            self.imagen.delete(self.imagen.name)
            super().delete()
    
# Articulo
def get_random_avatar_filename(instance, filename):
    return f'articulo/avatars/{filename}'

def default_avatar():
    return 'articulo/avatar/avatar3_default.jpg'

class Articulo(models.Model):
    # Campos existentes
    titulo = models.CharField(max_length=30, null=False)
    resumen = models.TextField(null=False)
    contenido = models.TextField(null=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='articulo', default='articulo/default_articulo.jpg')
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default=None, limit_choices_to={'nombre__isnull': False})
    publicado = models.DateTimeField(default=timezone.now)
    
    # Nuevos campos
    avatar = models.ImageField(null=True, blank=True, upload_to=get_random_avatar_filename, default=default_avatar)
    nickname = models.CharField(max_length=30, default="Sin Nickname")


    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using=None, keep_parent=False):
        self.imagen.delete()

        if self.avatar: 
            self.avatar.delete()
        super().delete(using=using, keep_parent=keep_parent)
        # super().delete()

# crear comentario
class Comment(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content