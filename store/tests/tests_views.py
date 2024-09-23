from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db.models import Case, When, IntegerField
from django.test import TestCase
from django.urls import reverse

from store.models import Product, Brand, Order, Category, CartItem
from store.tests.mixins import FixtureMixin, LoginUserMixin


ID = 1
PAGINATION = 5

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


class PrivateProductTest(LoginUserMixin, FixtureMixin, TestCase):
    def test_list_pagination(self) -> None:
        response = self.client.get(PRODUCT_LIST_URL)
        self.assertEqual(len(response.context["product_list"]), PAGINATION)

    def test_list_retrieve_data(self) -> None:
        response = self.client.get(PRODUCT_LIST_URL)
        products = Product.objects.annotate(
            available=Case(
                When(stock_quantity__gt=0, then=1),
                default=0,
                output_field=IntegerField(),
            )
        ).order_by("-available", "name")[:PAGINATION]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["product_list"]),
            list(products)
        )

    def test_search(self) -> None:
        search_str = "milka"
        response = self.client.get(PRODUCT_LIST_URL + f"?name={search_str}")
        self.assertEqual(
            len(response.context["product_list"]),
            len(Product.objects.filter(name__icontains=search_str)),
        )

    def test_filter_brand_only(self) -> None:
        brand = Brand.objects.get(pk=ID)
        response = self.client.get(PRODUCT_LIST_URL + f"?brand={brand.id}")
        self.assertEqual(
            len(response.context["product_list"]),
            len(Product.objects.filter(brand=brand)),
        )

    def test_filter_category_only(self) -> None:
        category = Category.objects.get(pk=5)
        response = self.client.get(
            PRODUCT_LIST_URL
            + f"?category={category.id}"
        )
        self.assertEqual(
            len(response.context["product_list"]),
            len(Product.objects.filter(category=category)),
        )

    def test_filter_and_category(self) -> None:
        brand = Brand.objects.get(pk=1)
        category = Category.objects.get(pk=2)
        response = self.client.get(
            PRODUCT_LIST_URL
            + f"?category={category.id}"
            + f"&?brand={brand.id}"
        )
        self.assertEqual(
            list(response.context["product_list"]),
            list(Product.objects.filter(category=category, brand=brand)),
        )

    def test_detail(self) -> None:
        product = Product.objects.get(id=ID)
        response = self.client.get(PRODUCT_DETAIL_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["product"].name, product.name)
        self.assertEqual(
            response.context["product"].category,
            product.category
        )
        self.assertEqual(response.context["product"].brand, product.brand)
        self.assertEqual(
            response.context["product"].stock_quantity,
            product.stock_quantity
        )

    def test_create(self) -> None:
        form_data = {
            "name": "Test name",
            "unit_value": 1,
            "unit_name": "KG",
            "stock_quantity": 10,
            "price": Decimal("9.99"),
            "brand": 1,
            "category": 1,
        }
        response = self.client.post(PRODUCT_CREATE_URL, data=form_data)
        new_product = Product.objects.filter(name=form_data["name"]).first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(new_product.name, form_data["name"])
        self.assertEqual(
            new_product.stock_quantity,
            form_data["stock_quantity"]
        )
        self.assertEqual(new_product.price, form_data["price"])
        self.assertEqual(new_product.brand.id, form_data["brand"])
        self.assertEqual(new_product.category.id, form_data["category"])

    def test_update(self) -> None:
        form_data = {
            "stock_quantity": 11,
            "price": Decimal("10.99"),
        }
        response = self.client.post(PRODUCT_UPDATE_URL, data=form_data)
        updated_product = Product.objects.get(pk=ID)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_product.price, form_data["price"])
        self.assertEqual(
            updated_product.stock_quantity,
            form_data["stock_quantity"]
        )

    def test_delete(self) -> None:
        response = self.client.post(PRODUCT_DELETE_URL)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Product.objects.filter(id=ID).exists())

    def test_add_to_cart(self) -> None:
        product = Product.objects.get(pk=ID)
        response = self.client.get(CART_ADD_PRODUCT_URL)
        self.assertEqual(response.status_code, 302)
        self.assertIn(
            product.name,
            list(
                self.user.shopping_cart.cart_items.values_list(
                    "product__name", flat=True
                )
            ),
        )

    def test_delete_from_cart(self) -> None:
        product = Product.objects.get(pk=ID)
        CartItem.objects.create(
            shopping_cart=self.user.shopping_cart, product=product, quantity=1
        )
        self.assertIn(
            product.name,
            list(
                self.user.shopping_cart.cart_items.values_list(
                    "product__name", flat=True
                )
            ),
        )

        response = self.client.get(CART_DELETE_PRODUCT_URL)
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(
            product.name,
            list(
                self.user.shopping_cart.cart_items.values_list(
                    "product__name", flat=True
                )
            ),
        )
