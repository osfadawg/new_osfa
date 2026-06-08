from django.urls import path
from .views import example_list
from .views import login_view, logout_view

urlpatterns = [
    path('example/', example_list),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]