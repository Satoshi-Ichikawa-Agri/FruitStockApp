# Generated by Django 4.2.13 on 2024-06-01 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_fruitmastermodel_fruit_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruitsalesmodel',
            name='sales_date',
            field=models.DateTimeField(default='2024-06-01 22:00:00'),
            preserve_default=False,
        ),
    ]
