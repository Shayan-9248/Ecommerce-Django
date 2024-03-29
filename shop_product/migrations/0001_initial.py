# Generated by Django 3.1.7 on 2021-02-26 18:50

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=177)),
            ],
        ),
        migrations.CreateModel(
            name="Size",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=177)),
            ],
        ),
        migrations.CreateModel(
            name="TimeStamp",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ("updated", django_jalali.db.models.jDateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=177)),
                ("description", models.TextField()),
                ("unit_price", models.PositiveIntegerField()),
                ("amount", models.PositiveIntegerField()),
                ("discount", models.PositiveIntegerField(blank=True, null=True)),
                ("total_price", models.PositiveIntegerField()),
                ("image", models.ImageField(default="1.jpg", upload_to="")),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Color", "color"),
                            ("Size", "size"),
                            ("None", "none"),
                        ],
                        max_length=177,
                    ),
                ),
                ("available", models.BooleanField(default=True)),
            ],
            # bases=('shop_product.timestamp',),
        ),
        migrations.CreateModel(
            name="Variant",
            fields=[
                (
                    "timestamp_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="shop_product.timestamp",
                    ),
                ),
                ("title", models.CharField(max_length=177)),
                ("unit_price", models.PositiveIntegerField()),
                ("amount", models.PositiveIntegerField()),
                ("discount", models.PositiveIntegerField(blank=True, null=True)),
                ("total_price", models.PositiveIntegerField()),
                (
                    "color_variant",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop_product.color",
                    ),
                ),
                (
                    "product_variant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop_product.product",
                    ),
                ),
                (
                    "size_variant",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop_product.size",
                    ),
                ),
            ],
            bases=("shop_product.timestamp",),
        ),
    ]
