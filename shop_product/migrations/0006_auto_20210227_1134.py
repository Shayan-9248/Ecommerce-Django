# Generated by Django 3.1.7 on 2021-02-27 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_product', '0005_auto_20210227_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s_category', to='shop_product.category'),
        ),
    ]