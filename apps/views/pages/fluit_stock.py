from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def fruit_master_top(request):
    """果物管理マスタTOP画面"""
    context = {}
    return render(request, "fruit_master/fruit_master_top.html", context)


@login_required
def register_fruit_master(request):
    """果物管理マスタ登録画面"""
    context = {}
    return render(request, "fruit_master/register_fruit_master.html", context)
