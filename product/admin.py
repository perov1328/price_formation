from django.contrib import admin
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Админка для Товаров платформы
    """
    list_display = ('title', 'salesman', 'total_price', 'sale',)
    list_filter = ('salesman', 'sale',)
    search_fields = ('title',)
