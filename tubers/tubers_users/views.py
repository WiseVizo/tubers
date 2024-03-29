from django.shortcuts import render

# Create your views here.
def login_user(request):
    return render(request, "tubers_users/login.html")

def logout_user(request):
    return render(request, "tubers_users/logout.html")
def register_user(request):
    return render(request, "tubers_users/register.html")

def dashboard(request):
    return render(request, "tubers_users/dashboard.html")
