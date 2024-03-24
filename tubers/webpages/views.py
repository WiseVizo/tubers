from django.shortcuts import render
import os
from .models import *
from youtubers.models import Youtuber
# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    our_team = OurTeam.objects.all()
    featured_tubers = Youtuber.objects.order_by("-created_at").filter(is_featured=True)
    all_tubers = Youtuber.objects.all()
    data =  {
        "sliders": sliders, 
        "our_team": our_team,
        "featured_tubers": featured_tubers,
        "youtubers": all_tubers,
    }
    return render(request, os.path.join("webpages", "home.html"), data)

def about(request):
    return render(request, os.path.join("webpages", "about.html"))

def services(request):
    return render(request, os.path.join("webpages", "services.html"))

def contact(request):
    return render(request, os.path.join("webpages", "contact.html"))
