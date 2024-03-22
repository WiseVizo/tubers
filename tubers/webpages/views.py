from django.shortcuts import render
import os
from .models import *
# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    our_team = OurTeam.objects.all()
    data =  {
        "sliders": sliders, 
        "our_team": our_team,
    }
    return render(request, os.path.join("webpages", "home.html"), data)

def about(request):
    return render(request, os.path.join("webpages", "about.html"))

def services(request):
    return render(request, os.path.join("webpages", "services.html"))

def contact(request):
    return render(request, os.path.join("webpages", "contact.html"))
