from django import forms


class FruitMasterResisterForm(forms.Form):
    """果物マスタ登録フォーム"""

    fruit_name = forms.CharField(max_length=100, label="名称")
    price = forms.IntegerField(label="単価")

    def __str__(self):
        return self.cleaned_data.get("fruit_name", "")
