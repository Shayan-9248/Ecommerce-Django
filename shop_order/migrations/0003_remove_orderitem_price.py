# Generated by Django 3.1.7 on 2021-02-28 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop_order", "0002_auto_20210228_1304"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderitem",
            name="price",
        ),
    ]
