from django import template

from store.models import Product, ShoppingCart


register = template.Library()


@register.filter
def in_cart_exists(product: Product, shopping_cart: ShoppingCart) -> bool:
    return shopping_cart.cart_items.filter(product=product).exists()


@register.filter
def in_cart_amount(product: Product, shopping_cart: ShoppingCart) -> float:
    return shopping_cart.cart_items.get(product=product).quantity
