from django.urls import path

from store.views import (
    index,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    OrderListView,
    OrderDetailView,
    CustomerListView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    BrandListView,
    BrandCreateView,
    BrandUpdateView,
    BrandDeleteView,
    cart_detail,
    empty_cart,
    add_to_cart,
    delete_from_cart,
    update_order_status,
    create_order_from_cart,
)


urlpatterns = [
    path("", index, name="index"),
    # Products
    path("products/", ProductListView.as_view(), name="product-list"),
    path(
        "products/<int:pk>/",
        ProductDetailView.as_view(),
        name="product-detail"
    ),
    path(
        "products/create/",
        ProductCreateView.as_view(),
        name="product-create"
    ),
    path(
        "products/<int:pk>/update/",
        ProductUpdateView.as_view(),
        name="product-update"
    ),
    path(
        "products/<int:pk>/delete/",
        ProductDeleteView.as_view(),
        name="product-delete"
    ),
    # Orders
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("orders/<int:pk>/update/", update_order_status, name="order-update"),
    path("orders/create/", create_order_from_cart, name="order-create"),
    # Customers
    path("customers/", CustomerListView.as_view(), name="customer-list"),
    path(
        "customers/<int:pk>/",
        CustomerDetailView.as_view(),
        name="customer-detail"
    ),
    path(
        "customers/create/",
        CustomerCreateView.as_view(),
        name="customer-create"
    ),
    path(
        "customers/<int:pk>/update/",
        CustomerUpdateView.as_view(),
        name="customer-update",
    ),
    path(
        "customers/<int:pk>/delete/",
        CustomerDeleteView.as_view(),
        name="customer-delete",
    ),
    # Categories
    path(
        "categories/",
        CategoryListView.as_view(),
        name="category-list"
    ),
    path(
        "categories/create/",
        CategoryCreateView.as_view(),
        name="category-create"
    ),
    path(
        "categories/<int:pk>/update/",
        CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "categories/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="category-delete",
    ),
    # Brands
    path("brands/", BrandListView.as_view(), name="brand-list"),
    path(
        "brands/create/",
        BrandCreateView.as_view(),
        name="brand-create"
    ),
    path(
        "brands/<int:pk>/update/",
        BrandUpdateView.as_view(),
        name="brand-update"
    ),
    path(
        "brands/<int:pk>/delete/",
        BrandDeleteView.as_view(),
        name="brand-delete"
    ),
    # Cart
    path("cart/", cart_detail, name="cart-detail"),
    path("cart/empty", empty_cart, name="cart-empty"),
    path(
        "cart/add/<int:product_id>/",
        add_to_cart,
        name="cart-add-product"
    ),
    path(
        "cart/delete/<int:product_id>/",
        delete_from_cart,
        name="cart-delete-product"
    ),
]

app_name = "store"
