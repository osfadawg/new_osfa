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
          data = models.ExampleModel.objects.all().order_by('-name')
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
     
@api_view(['GET'])
def requests_list(request):
     data = models.OsfaRequests.objects.all().order_by('-request_date')
     serializer = serializers.OsfaRequestsSerializer(data, many=True)
     return Response(serializer.data)

@api_view(['GET'])
def requests_detail(request, pk):
     item = get_object_or_404(models.OsfaRequests, pk=pk)
     
     if request.method == 'GET':
          serializer = serializers.OsfaRequestsSerializer(item)
          return Response(serializer.data)
     
     return
     
@api_view(['GET'])
def user_requestors_list(request):
     data = models.OsfaUser.objects.filter(isRequestor=1).order_by('first_name')
     serializer = serializers.OsfaUserSerializer(data, many=True)
     return Response(serializer.data)

@api_view(['GET'])
def user_programmers_list(request):
     data = models.OsfaUser.objects.filter(isRequestorProgrammer=1).order_by('first_name')
     serializer = serializers.OsfaUserSerializer(data, many=True)
     return Response(serializer.data)
