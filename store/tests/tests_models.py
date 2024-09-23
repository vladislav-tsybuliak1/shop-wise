from django.contrib.auth import get_user_model
from django.test import TestCase

from store.models import (
    Category,
    Brand,
    Product,
    Order,
    OrderItem,
    Review,
    ShoppingCart,
    CartItem,
)
from store.tests.mixins import FixtureMixin


class TestCategoryModel(TestCase):
    def test_str(self) -> None:
        category = Category.objects.create(
            name="Test name",
        )
        self.assertEqual(str(category), f"{category.name}")


class TestBrandModel(TestCase):
    def test_str(self) -> None:
        brand = Brand.objects.create(
            name="Test name",
        )
        self.assertEqual(str(brand), f"{brand.name}")


class TestProductModel(FixtureMixin, TestCase):
    def test_str(self) -> None:
        product = Product.objects.get(pk=1)
        self.assertEqual(
            str(product),
            f"{product.name} - {product.unit_value} {product.unit_name}"
        )


class TestOrderModel(FixtureMixin, TestCase):
    def setUp(self) -> None:
        self.order = Order.objects.get(pk=1)

    def test_str(self) -> None:
        self.assertEqual(str(self.order), str(self.order.id))

    def test_total_cost(self) -> None:
        self.assertEqual(
            self.order.total_cost,
            round(
                sum(
                    order_item.total_cost
                    for order_item
                    in self.order.order_items.all()
                ),
                2,
            ),
        )


class TestOrderItemModel(FixtureMixin, TestCase):
    def setUp(self) -> None:
        self.order_item = OrderItem.objects.get(pk=1)

    def test_str(self) -> None:
        self.assertEqual(
            str(self.order_item),
            f"{self.order_item.product}: {self.order_item.quantity}",
        )

    def test_total_cost(self) -> None:
        self.assertEqual(
            self.order_item.total_cost,
            round(
                float(self.order_item.product.price)
                * self.order_item.quantity,
                2
            ),
        )


class TestReviewModel(FixtureMixin, TestCase):
    def test_str(self) -> None:
        review = Review.objects.get(pk=1)
        self.assertEqual(
            str(review),
            f"By {review.customer} on {review.product}"
        )


class TestCartItemModel(FixtureMixin, TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart.objects.get(pk=1)
        self.cart_item = CartItem.objects.create(
            shopping_cart=self.shopping_cart,
            product_id=1,
            quantity=3
        )

    def test_str(self) -> None:
        self.assertEqual(
            str(self.cart_item),
            f"{self.cart_item.product}: {self.cart_item.quantity}"
        )

    def test_total_cost(self) -> None:
        self.assertEqual(
            self.cart_item.total_cost,
            round(
                float(self.cart_item.product.price)
                * self.cart_item.quantity,
                2
            ),
        )


class TestShoppingCartModel(FixtureMixin, TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart.objects.get(pk=1)
        self.cart_item = CartItem.objects.create(
            shopping_cart=self.shopping_cart,
            product_id=1,
            quantity=3
        )

    def test_str(self) -> None:
        self.assertEqual(
            str(self.shopping_cart),
            f"Shopping cart of {self.shopping_cart.customer}"
        )

    def test_total_cost(self) -> None:
        self.assertEqual(
            self.shopping_cart.total_cost,
            round(
                sum(
                    cart_item.total_cost
                    for cart_item in self.shopping_cart.cart_items.all()
                ),
                2,
            ),
        )


class TestCustomerModel(FixtureMixin, TestCase):
    def test_str(self) -> None:
        customer = get_user_model().objects.get(pk=1)
        self.assertEqual(
            str(customer),
            f"{customer.username} ({customer.get_full_name()})"
        )
