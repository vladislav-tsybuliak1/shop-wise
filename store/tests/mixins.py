from django.contrib.auth import get_user_model
from django.test import TestCase


class FixtureMixin(TestCase):
    fixtures = ["store/fixtures/shop_wise_db_data.json", ]


class LoginUserMixin(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.get(id=1)
        self.client.force_login(self.user)

