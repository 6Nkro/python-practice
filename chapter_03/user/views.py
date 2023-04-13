from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse

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
        # user_name = request.POST.get("user_name", None)
        # user_email = request.POST.get("user_email", None)
        # password = request.POST.get("password", None)

        keys = ["user_name", "user_email", "password"]
        [user_name, user_email, password] = [request.POST[key] or None for key in keys]

        if User.objects.filter(user_name=user_name).exists():
            return JsonResponse({"error": "이미 등록된 이름입니다."}, status=409)
        elif User.objects.filter(user_email=user_email).exists():
            return JsonResponse({"error": "이미 등록된 이메일입니다."}, status=409)

        user = User(
            user_name=user_name,
            user_email=user_email,
            password=make_password(password)
        )

        user.save()

        return redirect("/")

