# Generated by Django 3.1.7 on 2021-02-27 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop_product", "0004_variant"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("is_sub", models.BooleanField(default=False)),
                ("title", models.CharField(max_length=177)),
                ("slug", models.SlugField(unique=True)),
                (
                    "sub_cat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="s_category",
                        to="shop_product.category",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ManyToManyField(blank=True, to="shop_product.Category"),
        ),
    ]
