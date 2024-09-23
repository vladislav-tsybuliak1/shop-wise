from django.test import TestCase

from store.models import Category


class TestCategoryModel(TestCase):
    def test_str(self) -> None:
        category = Category.objects.create(
            name="Test name",
        )
        self.assertEqual(
            str(category),
            f"{category.name}"
        )
