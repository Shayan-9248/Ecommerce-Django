# Generated by Django 3.1.7 on 2021-03-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop_cart", "0004_compare"),
    ]

    operations = [
        migrations.AlterField(
            model_name="compare",
            name="session_key",
            field=models.CharField(blank=True, max_length=177, unique=True),
        ),
    ]
