from django.urls import path

from store.views import (
    index,
    ProductListView,
    ProductDetailView,
    OrderListView,
    OrderDetailView,
    cart_detail,
)


urlpatterns = [
    path("", index, name="index"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("cart/", cart_detail, name="cart-detail"),
]

app_name = "store"
