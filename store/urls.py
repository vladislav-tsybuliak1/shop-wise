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
    CategoryUpdateView,
    CategoryDeleteView,
    BrandListView,
    BrandCreateView,
    BrandUpdateView,
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
    path("categories/<int:pk>/update/", CategoryUpdateView.as_view(), name="category-update"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category-delete"),
    path("brands/", BrandListView.as_view(), name="brand-list"),
    path("brands/create/", BrandCreateView.as_view(), name="brand-create"),
    path("brands/<int:pk>/update/", BrandUpdateView.as_view(), name="brand-update"),
    path("cart/", cart_detail, name="cart-detail"),
    path("cart/add/<int:product_id>/", add_to_cart, name="cart-add-product"),
]

app_name = "store"
