from django.contrib.auth import get_user_model
from django.test import TestCase

from store.forms import ReviewForm, CustomerCreationForm, SearchForm, OrderStatusForm
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


class TestCustomerCreationForm(TestCase):
    def setUp(self) -> None:
        self.form_data = {
            "username": "Testuser",
            "first_name": "Test",
            "last_name": "Test",
            "phone_number": "+380123456789",
            "address": "Some address",
            "password1": "test123test",
            "password2": "test123test"
        }

    def test_form_valid(self) -> None:
        form = CustomerCreationForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data)

    def test_form_invalid_no_first_name(self) -> None:
        del self.form_data["first_name"]
        form = CustomerCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_no_last_name(self) -> None:
        del self.form_data["last_name"]
        form = CustomerCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_no_address(self) -> None:
        del self.form_data["address"]
        form = CustomerCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_no_phone_number(self) -> None:
        del self.form_data["phone_number"]
        form = CustomerCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_username_contains_non_eng_letters_other_than_underscore(self) -> None:
        self.form_data["username"] = "Test test"
        form = CustomerCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_username_starts_with_underscore(self) -> None:
        self.form_data["username"] = "_test"
        form = CustomerCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_username_ends_with_underscore(self) -> None:
        self.form_data["username"] = "Test_"
        form = CustomerCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_first_name_contains_non_eng_letter(self) -> None:
        self.form_data["first_name"] = "Test test"
        form = CustomerCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_last_name_contains_non_eng_letter(self) -> None:
        self.form_data["last_name"] = "Test test"
        form = CustomerCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_phone_number(self) -> None:
        self.form_data["phone_number"] = "+380681"
        form = CustomerCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_address(self) -> None:
        self.form_data["address"] = "Test adress!"
        form = CustomerCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())


class TestSearchForm(TestCase):
    def test_form_valid(self) -> None:
        form_data = {"name": "test name"}
        form = SearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class TestOrderStatusForm(TestCase):
    def test_form_valid(self) -> None:
        form_data = {"status": "RETURNED"}
        form = OrderStatusForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

