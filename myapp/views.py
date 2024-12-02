from django.shortcuts import render
from .models import *
# Create your views here.

def home_list(request):
    home = Home.objects.all()

    return render(request, 'index.html',{'home':home})
