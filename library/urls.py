from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.example_list, name='example=list'),
    path('example/<int:pk>/', views.example_detail, name='example-detail')
]