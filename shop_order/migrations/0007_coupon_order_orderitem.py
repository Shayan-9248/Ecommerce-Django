# Generated by Django 3.1.7 on 2021-03-02 18:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop_product', '0013_auto_20210302_1024'),
        ('shop_order', '0006_auto_20210302_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=177, unique=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('active', models.BooleanField(default=False)),
                ('discount', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('paid', models.BooleanField(default=False)),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('discount', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='shop_order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_product.variant')),
            ],
        ),
    ]
