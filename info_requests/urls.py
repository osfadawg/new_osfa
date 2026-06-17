from django.urls import path
from .views import home, form

urlpatterns = [
    path('form/<str:action>/<int:id>', form), 
    path('', home),
]
