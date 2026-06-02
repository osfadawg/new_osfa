from django.shortcuts import render

def home(request):
    return render(request, 'info_home/home.html')
