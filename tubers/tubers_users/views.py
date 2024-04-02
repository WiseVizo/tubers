from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            messages.success(request, "Logged In Successfully")
            auth.login(request, user)
            return redirect("home")
        messages.error(request, "invalid credintails")
        return redirect("login_user")
    return render(request, "tubers_users/login.html")

@login_required(login_url='login_user')
def logout_user(request):
    logout(request)
    return redirect('home')
    
def register_user(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists(): # check if user already exist
                messages.error(request, f"{first_name} as username is already taken!")
                return redirect("register_user")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                messages.success(request, "account created successfully")
                return redirect("login_user")
        else:
            messages.error(request, "Passwords do not match!")
            return redirect("register_user")

    return render(request, "tubers_users/register.html")
@login_required(login_url='login_user')
def dashboard(request):
    return render(request, "tubers_users/dashboard.html")
