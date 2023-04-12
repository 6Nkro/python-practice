from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password

from .forms import LoginForm
from .models import User


# Create your views here.

def home(request):
    return render(request, 'home.html')


def logout(request):
    if request.session.get('user'):
        del (request.session['user'])

    return redirect('/')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        user_name = request.POST.get("user_name", None)
        user_email = request.POST.get("user_email", None)
        password = request.POST.get("password", None)
        re_password = request.POST.get("re_password", None)

        user = User(
            user_name=user_name,
            user_email=user_email,
            password=make_password(password)
        )

        user.save()

        return redirect("/")
