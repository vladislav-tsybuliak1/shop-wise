from itertools import product

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from store.models import Product, Category, Brand, Customer, Order, OrderItem, Review, ShoppingCart, CartItem


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
    list_display = ["pk", "customer", "total_cost", "created_at", "status", ]
    search_fields = ["customer__username", "customer__first_name", "customer__last_name", ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["customer", "product", "content", "created_at", ]


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(OrderItem)
admin.site.register(ShoppingCart)
admin.site.register(CartItem)
