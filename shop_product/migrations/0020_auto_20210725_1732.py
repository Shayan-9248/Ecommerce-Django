# Generated by Django 3.2.5 on 2021-07-25 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop_product", "0019_auto_20210725_1731"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={},
        ),
        migrations.RemoveField(
            model_name="comment",
            name="created",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="updated",
        ),
    ]
