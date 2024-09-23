from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from store.models import Product, Brand, Order
from store.tests.mixins import FixtureMixin, LoginUserMixin

ID=1

# Index
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


class PublicTest(FixtureMixin, TestCase):
    # Index
    def test_index_login_not_required(self) -> None:
        response = self.client.get(INDEX_URL)
        self.assertEqual(response.status_code, 200)

    # Products
    def test_product_list_login_required(self) -> None:
        response = self.client.get(PRODUCT_LIST_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_product_detail_login_required(self) -> None:
        response = self.client.get(PRODUCT_DETAIL_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_product_create_login_required(self) -> None:
        response = self.client.get(PRODUCT_CREATE_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_product_update_login_required(self) -> None:
        response = self.client.get(PRODUCT_UPDATE_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_product_delete_login_required(self) -> None:
        response = self.client.get(PRODUCT_DELETE_URL)
        self.assertNotEqual(response.status_code, 200)

    # Orders
    def test_order_list_login_required(self) -> None:
        response = self.client.get(ORDER_LIST_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_order_detail_login_required(self) -> None:
        response = self.client.get(ORDER_DETAIL_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_order_update_login_required(self) -> None:
        response = self.client.get(ORDER_UPDATE_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_order_create_login_required(self) -> None:
        response = self.client.get(ORDER_CREATE_URL)
        self.assertNotEqual(response.status_code, 200)

    # Customers
    def test_customer_list_login_required(self) -> None:
        response = self.client.get(CUSTOMER_LIST_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_customer_detail_login_required(self) -> None:
        response = self.client.get(CUSTOMER_DETAIL_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_customer_create_login_not_required(self) -> None:
        response = self.client.get(CUSTOMER_CREATE_URL)
        self.assertEqual(response.status_code, 200)

    def test_customer_update_login_required(self) -> None:
        response = self.client.get(CUSTOMER_UPDATE_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_customer_delete_login_required(self) -> None:
        response = self.client.get(CUSTOMER_DELETE_URL)
        self.assertNotEqual(response.status_code, 200)

    # Categories
    def test_category_list_login_required(self) -> None:
        response = self.client.get(CATEGORY_LIST_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_category_create_login_required(self) -> None:
        response = self.client.get(CATEGORY_CREATE_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_category_update_login_required(self) -> None:
        response = self.client.get(CATEGORY_UPDATE_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_category_delete_login_required(self) -> None:
        response = self.client.get(CATEGORY_DELETE_URL)
        self.assertNotEqual(response.status_code, 200)

    # Brands
    def test_brand_list_login_required(self) -> None:
        response = self.client.get(BRAND_LIST_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_brand_create_login_required(self) -> None:
        response = self.client.get(BRAND_CREATE_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_brand_update_login_required(self) -> None:
        response = self.client.get(BRAND_UPDATE_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_brand_delete_login_required(self) -> None:
        response = self.client.get(BRAND_DELETE_URL)
        self.assertNotEqual(response.status_code, 200)

    # Cart
    def test_cart_detail_login_required(self) -> None:
        response = self.client.get(CART_DETAIL_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_cart_empty_login_required(self) -> None:
        response = self.client.get(CART_EMPTY_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_cart_add_product_login_required(self) -> None:
        response = self.client.get(CART_ADD_PRODUCT_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_cart_delete_product_login_required(self) -> None:
        response = self.client.get(CART_DELETE_PRODUCT_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateIndexTest(LoginUserMixin, FixtureMixin, TestCase):
    def test_count_objects(self) -> None:
        num_customers = get_user_model().objects.count()
        num_products = Product.objects.count()
        num_brands = Brand.objects.count()
        num_orders = Order.objects.count()

        response = self.client.get(INDEX_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["num_customers"], num_customers)
        self.assertEqual(response.context["num_products"], num_products)
        self.assertEqual(response.context["num_brands"], num_brands)
        self.assertEqual(response.context["num_orders"], num_orders)

    def test_count_visits(self) -> None:
        visits = 5
        for num_visits in range(1, visits + 1):
            response = self.client.get(INDEX_URL)
            self.assertEqual(response.context["num_visits"], num_visits)
