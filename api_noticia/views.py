from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import NoticiaSerializer
from entrega3.models import Noticia
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view



# Create your views here.
@api_view(['GET', 'POST'])
def noticias(request):
#     **-----------------------------**
#       LISTANDO TODOS LAS NOTICIAS
#     **-----------------------------** 
    if request.method == 'GET':
       lista_noticia = Noticia.objects.all()
       Serializer = NoticiaSerializer(lista_noticia, many=True) 
       return Response(Serializer.data)
    
#     **-----------------------------**
#       AGREGANDO UNA NOTICIA
#     **-----------------------------** 

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoticiaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     **----------------------------------**
#       AGREGAR UNA ACTUALIZACION ELIMINAR
#     **----------------------------------** 