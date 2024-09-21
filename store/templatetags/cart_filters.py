from typing import Any

from django import template

from store.models import Product, ShoppingCart


register = template.Library()


@register.filter
def get_item(dictionary, key) -> Any:
    return dictionary.get(key)
