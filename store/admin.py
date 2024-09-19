from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from store.models import Product, Category, Brand, Customer, Order, OrderItem, Review


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


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        "phone_number",
        "address",
    )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("phone_number", "address",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("phone_number", "address",)}),)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ["customer__username", ]


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Review)
