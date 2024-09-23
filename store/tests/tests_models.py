from django.test import TestCase

from store.models import Category, Brand


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
