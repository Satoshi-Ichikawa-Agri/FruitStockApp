from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.forms.fruit_form import FruitMasterResisterForm
from apps.models.fruit_master_model import FruitMasterModel


@login_required
def fruit_master_top(request):
    """果物管理マスタTOP画面"""
    fruits = FruitMasterModel.objects.all().order_by("-updated_at")

    context = {"fruits": fruits}

    return render(request, "fruit_master/fruit_master_top.html", context)


@login_required
def register_fruit_master(request):
    """果物管理マスタ登録画面"""

    if request.method == "POST":
        form = FruitMasterResisterForm(request.POST)
        if form.is_valid():
            user = request.user
            fruit = FruitMasterModel(
                fruit_name=form.cleaned_data["fruit_name"],
                price=form.cleaned_data["price"],
                created_user=user.user_name,
                updated_user=user.user_name,
            )
            fruit.save()
            return redirect("fruit_master_top")
    else:
        form = FruitMasterResisterForm()

    context = {"form": form}

    return render(request, "fruit_master/register_fruit_master.html", context)


def modify_fruit_master(request, fruit_id):
    """果物管理マスタ修正画面"""

    fruit = get_object_or_404(FruitMasterModel, pk=fruit_id)
    if request.method == "POST":
        form = FruitMasterResisterForm(request.POST)
        if form.is_valid():
            fruit.fruit_name = form.cleaned_data["fruit_name"]
            fruit.price = form.cleaned_data["price"]
            fruit.save()
            return redirect("fruit_master_top")
    else:
        form = FruitMasterResisterForm(
            initial={"fruit_name": fruit.fruit_name, "price": fruit.price}
        )

    context = {"form": form}

    return render(request, "fruit_master/modify_fruit_master.html", context)


def delete_fruit_master(request, fruit_id):
    """果物管理マスタ削除処理"""
    fruit = get_object_or_404(FruitMasterModel, pk=fruit_id)
    fruit.delete()

    return redirect("fruit_master_top")
