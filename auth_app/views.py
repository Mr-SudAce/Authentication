from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from .models import *


# register
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


# login
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session.set_expiry(3600)
                return redirect("home")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


# logout
def logout_view(request):
    auth_logout(request)
    return redirect("login")


# dashboard
@login_required
def dashboard(request):
    pp = CustomUser.objects.all()

    item = {"pp": pp}
    return render(request, "dashboard.html", item)
