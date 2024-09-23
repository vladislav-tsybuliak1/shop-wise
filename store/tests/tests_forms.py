from django.contrib.auth import get_user_model
from django.test import TestCase

from store.forms import ReviewForm
from store.models import Product
from store.tests.mixins import FixtureMixin


class TestReviewForm(FixtureMixin, TestCase):
    def setUp(self) -> None:
        self.customer = get_user_model().objects.get(pk=1)
        self.product = Product.objects.get(pk=1)

    def test_form_valid(self) -> None:
        form_data = {
            "customer": self.customer,
            "product": self.product,
            "content": "Some content"
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(
            form.cleaned_data["content"],
            form_data["content"]
        )

    def test_form_invalid_no_content(self) -> None:
        form_data = {
            "customer": self.customer,
            "product": self.product,
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())


