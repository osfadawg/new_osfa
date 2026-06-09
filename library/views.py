from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers 

# Create your views here.
@api_view(['GET', 'POST'])
def example_list(request):
     if request.method == 'GET':          
          data = models.ExampleModel.objects.all()
          serializer = serializers.ExampleModelSerializer(data, many=True)
          return Response(serializer.data)
     
     elif request.method == 'POST':
          serializer = serializers.ExampleModelSerializer(data=request.data)
          
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     

@api_view(['GET', 'PUT', 'PATCH'])
def example_detail(request, pk):
     item = get_object_or_404(models.ExampleModel, pk=pk)
     
     if request.method == 'GET':          
          serializer = serializers.ExampleModelSerializer(item)
          return Response(serializer.data)
     
     elif request.method in ['PUT', 'PATCH']:
          partial = (request.method == 'PATCH')
          serializer = serializers.ExampleModelSerializer(item, data=request.data, partial=partial)
          
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)