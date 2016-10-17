from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import models, forms

# Create your views here.
def user_profile(request, username):
    # Get the viewed user.
    viewed_user = User.objects.get(username=username)
    context = {
        "viewed_user": viewed_user,
        "viewed_user_profile": models.UserProfile.objects.get(user=viewed_user),
    }

    # Get the view user profile and pass it as the context
    return render(request, "users/profile.html", context)

def user_gallery(request, username):
    return HttpResponse("Coming Soon")

def user_favorites(request, username):
    return HttpResponse("Coming Soon")

def user_login(request):
    # If the request was a POST
    if request.method == 'POST':
        # Get the contents of the form
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            # Attempt to log the user in.
            data = form.clean()
            user = authenticate(username=data["username"], password=data["password"])
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.POST.get("next", '/'))
            else:
                form.errors['__all__'] = form.error_class(["Invalid username/password"])
                return render(request, 'users/login.html', {"form": form})

    return render(request, "users/login.html", {"form": forms.LoginForm, "next": request.GET.get("next", '/')})


def user_logout(request):
    # Log out the user and return them to index.
    logout(request)
    return redirect('index')

def user_signup(request):
    # return HttpResponse("Coming Soon")
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        try:
            if form.is_valid():
                data = form.clean()
                user = User(username=data["username"],
                            password=data["password"],
                            email=data["email"])
                user.save()
                HttpResponseRedirect("/")
        except Exception as e:
            form.errors["__all__"] = form.error_class(str(e))
            return render(request, 'users/signup.html', {"form": form})

    else:
        return render(request, 'users/signup.html', {"form": forms.RegisterForm})
