from django.shortcuts import render
from .models import Youtuber
# Create your views here.
def youtubers(request):
    tubers = Youtuber.objects.all()
    data = {
        'tubers' : tubers,
    }
    return render(request, "youtubers/youtubers.html", data)

def youtuber_details(request, id):
    pass

def search(request):
    pass
