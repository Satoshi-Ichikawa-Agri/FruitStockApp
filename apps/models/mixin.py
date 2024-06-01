from django.db import models


class BaseMixin(models.Model):
    """Originalモデルの基底クラス"""

    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=100)

    class Meta:
        abstract = True
