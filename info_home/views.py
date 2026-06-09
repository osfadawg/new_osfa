from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
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

@login_required
def home(request):
    return render(request, 'info_home/home.html')
