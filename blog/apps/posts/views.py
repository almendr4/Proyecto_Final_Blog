from django.shortcuts import render
from .models import Articulo, Post
from django.views import View
from .forms import ArticuloForm


# Create your views here.


def posts(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts' : posts})

# # Vista basada en funcion
# def articulos(request):
#     articulos = Articulo.objects.all()
#     return render(request, 'articulo.html', {'articulos' : articulos})



# vista basada en clases
class ArticuloView(View):
    template_name= 'articulo.html'

    def get(self, request):
        articulos = Articulo.objects.all()
        return render(request, 'articulo.html', {'articulos' : articulos})


def existe_articulo(id):
    for i in Articulo:
        if i.id == id:
            return i
    return None

# leer articulo
def leer_articulo(request, id):
    articulo = Articulo.objects.filter(id = id).first()
        


    context = {
        'articulos': articulo,
    }

    return render (request, 'articulo_individual.html', context)

# crear articulo!

def crear_articulo(request):
     if request.method == 'POST':
         form = ArticuloForm(request.POST, request.FILES)
         if form.is_valid():
          form.save()
         return render (request, 'articulo.html') 
     else: 
         form = ArticuloForm()
         return render(request, 'publicar.html', {'form' : form})        
     
