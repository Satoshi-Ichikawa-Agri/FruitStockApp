from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.forms.fruit_form import (
    FruitMasterResisterForm,
    FruitSalesResisterForm,
)
from apps.models.fruit_master_model import FruitMasterModel, FruitSalesModel


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


# --------------------
@login_required
def fruit_sales_top(request):
    """販売情報管理TOP画面"""
    sales = FruitSalesModel.objects.all().order_by("-sales_date")

    context = {"sales": sales}

    return render(request, "fruit_sales/fruit_sales_top.html", context)


@login_required
def register_fruit_sales(request):
    """販売情報管理登録画面"""

    if request.method == "POST":
        form = FruitSalesResisterForm(request.POST)
        if form.is_valid():
            user = request.user
            fruit_id = form.cleaned_data["fruit"]
            sales_volume = form.cleaned_data["sales_volume"]
            sales_date = form.cleaned_data["sales_date"]

            # FruitMasterModelから選択された果物の情報を取得
            fruit = FruitMasterModel.objects.get(fruit_id=fruit_id)
            fruit_name = fruit.fruit_name
            price = fruit.price
            total_price = price * sales_volume

            # FruitSalesModelにデータを保存
            FruitSalesModel.objects.create(
                fruit_id=fruit_id,
                fruit_name=fruit_name,
                price=price,
                sales_volume=sales_volume,
                total_price=total_price,
                sales_date=sales_date,
                created_user=user.user_name,
                updated_user=user.user_name,
            )

            return redirect("fruit_sales_top")
    else:
        form = FruitSalesResisterForm()

    context = {"form": form}

    return render(request, "fruit_sales/register_fruit_sales.html", context)


def modify_fruit_sales(request, sales_id):
    """販売情報管理修正画面"""

    sales = get_object_or_404(FruitSalesModel, pk=sales_id)
    if request.method == "POST":
        form = FruitSalesResisterForm(request.POST)
        if form.is_valid():
            user = request.user
            fruit_id = form.cleaned_data["fruit"]
            sales_volume = form.cleaned_data["sales_volume"]
            sales_date = form.cleaned_data["sales_date"]

            # FruitMasterModelから選択された果物の情報を取得
            fruit = FruitMasterModel.objects.get(fruit_id=fruit_id)
            sales.fruit_id = fruit.fruit_id
            sales.fruit_name = fruit.fruit_name
            sales.price = fruit.price
            sales.total_price = fruit.price * sales_volume
            sales.sales_date = sales_date
            sales.updated_user = user.user_name
            sales.save()

            return redirect("fruit_sales_top")
    else:
        form = FruitSalesResisterForm(
            initial={
                "fruit_id": sales.fruit_id,
                "sales_volume": sales.sales_volume,
            }
        )

    context = {"form": form}

    return render(request, "fruit_sales/modify_fruit_sales.html", context)


def delete_fruit_sales(request, sales_id):
    """販売情報管理削除処理"""
    fruit = get_object_or_404(FruitSalesModel, pk=sales_id)
    fruit.delete()

    return redirect("fruit_sales_top")
