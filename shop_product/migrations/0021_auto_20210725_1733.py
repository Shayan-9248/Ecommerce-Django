# Generated by Django 3.2.5 on 2021-07-25 17:33

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ("shop_product", "0020_auto_20210725_1732"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ("-created",)},
        ),
        migrations.AddField(
            model_name="comment",
            name="created",
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="updated",
            field=django_jalali.db.models.jDateTimeField(auto_now=True, null=True),
        ),
    ]
