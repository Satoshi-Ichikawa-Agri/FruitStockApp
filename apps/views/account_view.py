from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

from apps.forms.account_form import LoginForm, UserCreationForm


def signup(request):
    """User登録画面"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")  # 登録後にリダイレクトするページを指定
    else:
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})


def login(request):
    """ログイン画面"""
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("home")  # ログイン後にリダイレクトするページを指定
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})
