# Generated by Django 3.2.5 on 2021-07-29 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop_product", "0032_alter_product_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="brand",
            name="created",
        ),
        migrations.RemoveField(
            model_name="brand",
            name="updated",
        ),
        migrations.RemoveField(
            model_name="color",
            name="created",
        ),
        migrations.RemoveField(
            model_name="color",
            name="updated",
        ),
        migrations.RemoveField(
            model_name="size",
            name="created",
        ),
        migrations.RemoveField(
            model_name="size",
            name="updated",
        ),
    ]
