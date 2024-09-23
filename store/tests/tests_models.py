from django.test import TestCase

from store.models import Category, Brand, Product, Order


class TestCategoryModel(TestCase):
    def test_str(self) -> None:
        category = Category.objects.create(
            name="Test name",
        )
        self.assertEqual(
            str(category),
            f"{category.name}"
        )


class TestBrandModel(TestCase):
    def test_str(self) -> None:
        brand = Brand.objects.create(
            name="Test name",
        )
        self.assertEqual(
            str(brand),
            f"{brand.name}"
        )


class TestProductModel(TestCase):
    fixtures = ["store/fixtures/shop_wise_db_data.json", ]

    def test_str(self) -> None:
        product = Product.objects.get(pk=1)
        self.assertEqual(
            str(product),
            f"{product.name} - {product.unit_value} {product.unit_name}"
        )


class TestOrderModel(TestCase):
    fixtures = ["store/fixtures/shop_wise_db_data.json", ]

    def test_str(self) -> None:
        order = Order.objects.get(pk=1)
        self.assertEqual(
            str(order),
            str(order.id)
        )



