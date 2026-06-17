from django.urls import path
from . import views

urlpatterns = [
    #   DETAILS
    path('requests/<int:pk>', views.requests_detail, name='requests-details'),
    path('example/<int:pk>/', views.example_detail, name='example-detail'),    
    
    #   QUERIES
    path('users/requestors', views.user_requestors_list, name='users-requestors-list'),
    
    #   LISTS
    path('example/', views.example_list, name='example-list'),
    path('requests/', views.requests_list, name='requests-list'),
]