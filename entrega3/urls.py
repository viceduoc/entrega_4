from django.conf.urls import url
from django.urls import path
from .views import agregarNoticia, home, formulario, noticias, eliminarNoticia




# Agregando path's
urlpatterns = [
    path('', home, name="home"),
    path('formulario', formulario, name="formulario"),
    path('noticias', noticias, name='noticias'),
    path('eliminar-noticia/<id>', eliminarNoticia, name="eliminar-noticia"),
    path('agregar-noticia', agregarNoticia, name="agregar-noticia")
]