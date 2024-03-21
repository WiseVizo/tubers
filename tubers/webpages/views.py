from django.shortcuts import render
import os
# Create your views here.
def home(request):
    return render(request, os.path.join("webpages", "home.html"))

def about(request):
    return render(request, os.path.join("webpages", "about.html"))

def services(request):
    return render(request, os.path.join("webpages", "services.html"))

def contact(request):
    return render(request, os.path.join("webpages", "contact.html"))
