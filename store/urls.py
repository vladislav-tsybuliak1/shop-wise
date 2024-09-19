from django.urls import path

from store.views import (
    index,
    ProductListView,
)


urlpatterns = [
    path("", index, name="index"),
    path("products/", ProductListView.as_view(), name="product-list"),
]

app_name = "store"
