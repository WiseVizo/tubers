from django.shortcuts import render, get_object_or_404
from .models import Youtuber
# Create your views here.
def youtubers(request):
    tubers = Youtuber.objects.all()
    data = {
        'tubers' : tubers,
    }
    return render(request, "youtubers/youtubers.html", data)

def youtuber_details(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber': tuber,
    }
    return render(request, "youtubers/youtuber_details.html", data)

def search(request):
    pass
