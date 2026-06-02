from django.urls import path
from .views import example_list

urlpatterns = [
    path('example/', example_list),
]