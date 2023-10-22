from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    coctel = {"coct" : Coct.objects.all()}
    return render(request, 'drink/index.html', coctel)
