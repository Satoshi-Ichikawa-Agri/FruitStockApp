"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from apps.views.pages.account_view import (
    signup,
    login,
    logout,
    home,
)
from apps.views.pages.fruit_stock import (
    fruit_master_top,
    register_fruit_master,
    modify_fruit_master,
    delete_fruit_master,
)


urlpatterns = [
    # account
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("home/", home, name="home"),
    # Fruit_Master
    path("fruit_master_top/", fruit_master_top, name="fruit_master_top"),
    path(
        "register_fruit_master/",
        register_fruit_master,
        name="register_fruit_master",
    ),
    path(
        "modify_fruit_master/<int:fruit_id>/",
        modify_fruit_master,
        name="modify_fruit_master",
    ),
    path(
        "delete_fruit_master/<int:fruit_id>/",
        delete_fruit_master,
        name="delete_fruit_master",
    ),
]
