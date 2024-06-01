from django.db import models

from apps.models.mixin import BaseMixin


class FruitMasterModel(BaseMixin):
    """果物マスタテーブル"""

    fruit_id = models.AutoField(primary_key=True)
    fruit_name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()

    class Meta:
        db_table = "m_fruit"

    def __str__(self):
        return self.fruit_name


class FruitSalesModel(BaseMixin):
    """果物販売テーブル"""

    sales_id = models.AutoField(primary_key=True)
    fruit_id = models.IntegerField()
    fruit_name = models.CharField(max_length=100)
    price = models.IntegerField()
    sales_volume = models.IntegerField()
    total_price = models.IntegerField()
    sales_date = models.DateTimeField()

    class Meta:
        db_table = "t_fruit_sales"

    def __str__(self):
        return self.fruit_name
