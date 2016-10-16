from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import models

# Create your views here.
def user_profile(request, username):
    viewed_user = User.objects.get(username=username)
    context = {
        "viewed_user": viewed_user,
        "viewed_user_profile": models.UserProfile.objects.get(user=viewed_user),
        "is_user": request.user == viewed_user
    }

    return render(request, "users/profile.html", context)

def user_login(request):
    return HttpResponse("Coming Soon")

def user_logout(request):
    return HttpResponse("Coming Soon")

def user_signup(request):
    return HttpResponse("Coming Soon")
