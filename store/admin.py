from django.contrib import admin

from store.models import Product, Category, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "brand",
        "unit_value",
        "unit_name",
        "stock_quantity",
        "price",
        "category",
    ]
    list_filter = ["brand", "category", ]
    search_fields = ["name", ]
    list_per_page = 10


admin.site.register(Category)
admin.site.register(Brand)
