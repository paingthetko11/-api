from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_list,name='home_list'),
]
