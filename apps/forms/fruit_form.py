from django import forms

from apps.models.fruit_master_model import FruitMasterModel


class FruitMasterResisterForm(forms.Form):
    """果物マスタ登録フォーム"""

    fruit_name = forms.CharField(max_length=100, label="名称")
    price = forms.IntegerField(label="単価")

    def __str__(self):
        return self.cleaned_data.get("fruit_name", "")


class FruitSalesResisterForm(forms.Form):
    """販売登録フォーム"""

    fruit = forms.ChoiceField(choices=[], label="果物")
    sales_volume = forms.IntegerField(label="個数")
    sales_date = forms.DateTimeField(label="販売日時")

    def __init__(self, *args, **kwargs):
        super(FruitSalesResisterForm, self).__init__(*args, **kwargs)
        self.fields["fruit"].choices = [
            (fruit.fruit_id, fruit.fruit_name)
            for fruit in FruitMasterModel.objects.all()
        ]

    def __str__(self):
        return self.cleaned_data.get("fruit_name", "")
