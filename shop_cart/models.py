# Core Django imports
from django.db import models
from django.conf import settings

# Local imports
from shop_product.models import (
    Product,
    Variant,
    TimeStamp,
)


class Cart(TimeStamp):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(
        Variant, on_delete=models.CASCADE, null=True, blank=True
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"


class Compare(TimeStamp):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=177, unique=True, blank=True, null=True)

    def __str__(self):
        return self.product.title
