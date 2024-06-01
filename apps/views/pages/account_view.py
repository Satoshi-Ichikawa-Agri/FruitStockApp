from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.forms.account_form import LoginForm, UserCreationForm


def signup(request):
    """User登録画面"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})


def login(request):
    """ログイン画面"""
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("home")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


@login_required
def logout(request):
    """ログアウト処理"""
    auth_logout(request)
    return redirect("login")


@login_required
def home(request):
    """HOME画面"""
    return render(request, "accounts/home.html")
