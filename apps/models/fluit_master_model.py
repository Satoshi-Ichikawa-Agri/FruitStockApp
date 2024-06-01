from django.db import models

from apps.models.mixin import BaseMixin


class FluitMasterModel(BaseMixin):
    """果物マスタテーブル"""

    fluit_id = models.AutoField(primary_key=True)
    fluit_name = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = "m_fluit"

    def __str__(self):
        return self.fluit_name
