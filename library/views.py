from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ExampleModel
from .serializers import ExampleModelSerializer

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
@api_view(['GET'])
def example_list(request):
     data = ExampleModel.objects.all()
     serializer = ExampleModelSerializer(data, many=True)
     return Response(serializer.data)

def login_view(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          
          user = authenticate(request, username=username, password=password)
          
          if user is not None:
               login(request=request, user=user)
               return redirect('/')
          else:
               return render(request, 'registration/login.html', {'error': 'Invalid Credentials'})

     return render(request, 'registration/login.html')

def logout_view(request):
     logout(request)
     return redirect('/login/')