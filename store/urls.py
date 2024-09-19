from django.urls import path

from store.views import (
    index,
    ProductListView,
    ProductDetailView,
    OrderListView,
)


urlpatterns = [
    path("", index, name="index"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("orders/", OrderListView.as_view(), name="order-list"),
]

app_name = "store"
