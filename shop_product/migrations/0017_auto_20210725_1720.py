# Generated by Django 3.2.5 on 2021-07-25 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop_product", "0016_auto_20210725_1718"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={},
        ),
        migrations.RemoveField(
            model_name="product",
            name="created",
        ),
        migrations.RemoveField(
            model_name="product",
            name="updated",
        ),
    ]
