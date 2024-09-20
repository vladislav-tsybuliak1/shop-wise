from django.urls import path

from store.views import (
    index,
    ProductListView,
    ProductDetailView,
    OrderListView,
    OrderDetailView,
    CustomerListView,
    CustomerDetailView,
    CategoryListView,
    CategoryCreateView,
    BrandListView,
    cart_detail,
    add_to_cart,
)


urlpatterns = [
    path("", index, name="index"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("customers/", CustomerListView.as_view(), name="customer-list"),
    path("customers/<int:pk>/", CustomerDetailView.as_view(), name="customer-detail"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/create/", CategoryCreateView.as_view(), name="category-create"),
    path("brands/", BrandListView.as_view(), name="brand-list"),
    path("cart/", cart_detail, name="cart-detail"),
    path("cart/add/<int:product_id>/", add_to_cart, name="cart-add-product"),
]

app_name = "store"
