# URL DE APLICACION


from django.urls import path
from .views import posts
from . import views
from .views import ArticuloView



app_name = 'posts'




urlpatterns = [
    # path('articulos', articulos, name='articulo'),
    path('articulos/', ArticuloView.as_view(), name='articulos'),
    path('leer_articulo/<int:id>', views.leer_articulo, name='leer_articulo'),
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    

]

