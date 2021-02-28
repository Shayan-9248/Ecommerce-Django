from django.contrib import admin
from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('user', 'order', 'product', 'variant', 'quantity')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'paid')
    list_filter = ('paid',)
    inlines = (OrderItemInline,)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
