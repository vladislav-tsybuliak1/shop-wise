from django.test import TestCase
from django.urls import reverse

ID=1

INDEX_URL = reverse("store:index")

# Products
PRODUCT_LIST_URL = reverse("store:product-list")
PRODUCT_DETAIL_URL = reverse("store:product-detail", args=[ID])
PRODUCT_CREATE_URL = reverse("store:product-create")
PRODUCT_UPDATE_URL = reverse("store:product-update", args=[ID])
PRODUCT_DELETE_URL = reverse("store:product-delete", args=[ID])

# Orders
ORDER_LIST_URL = reverse("store:order-list")
ORDER_DETAIL_URL = reverse("store:order-detail", args=[ID])
ORDER_UPDATE_URL = reverse("store:order-update", args=[ID])
ORDER_CREATE_URL = reverse("store:order-create")

# Customers
CUSTOMER_LIST_URL = reverse("store:customer-list")
CUSTOMER_DETAIL_URL = reverse("store:customer-detail", args=[ID])
CUSTOMER_CREATE_URL = reverse("store:customer-create")
CUSTOMER_UPDATE_URL = reverse("store:customer-update", args=[ID])
CUSTOMER_DELETE_URL = reverse("store:customer-delete", args=[ID])

# Categories
CATEGORY_LIST_URL = reverse("store:category-list")
CATEGORY_CREATE_URL = reverse("store:category-create")
CATEGORY_UPDATE_URL = reverse("store:category-update", args=[ID])
CATEGORY_DELETE_URL = reverse("store:category-delete", args=[ID])

# Brands
BRAND_LIST_URL = reverse("store:brand-list")
BRAND_CREATE_URL = reverse("store:brand-create")
BRAND_UPDATE_URL = reverse("store:brand-update", args=[ID])
BRAND_DELETE_URL = reverse("store:brand-delete", args=[ID])

# Cart
CART_DETAIL_URL = reverse("store:cart-detail")
CART_EMPTY_URL = reverse("store:cart-empty")
CART_ADD_PRODUCT_URL = reverse("store:cart-add-product", args=[ID])
CART_DELETE_PRODUCT_URL = reverse("store:cart-delete-product", args=[ID])


