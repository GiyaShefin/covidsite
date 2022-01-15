from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import City
def covidreg(request,c_slug=None):


    return render(request,"cities.html")

