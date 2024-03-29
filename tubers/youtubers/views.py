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
    tubers = Youtuber.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        tubers = tubers.filter(description__icontains=keyword)

    # Get all unique city values from the Youtuber model
    cities = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_types = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    categories = Youtuber.objects.values_list('category', flat=True).distinct()

     # Get the selected values from the request GET parameters
    selected_city = request.GET.get('city')
    selected_category = request.GET.get('category')
    selected_camera_type = request.GET.get('camera_type')



    if selected_city:
        tubers = tubers.filter(city=selected_city)
    if selected_category:
        tubers = tubers.filter(category=selected_category)
    if selected_camera_type:
        tubers = tubers.filter(camera_type=selected_camera_type)
    data = {
        'tubers' : tubers,
        'cities': cities,
        'camera_types': camera_types,
        'categories': categories,
    }
    return render(request, "youtubers/search.html", data)
