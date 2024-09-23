from django.test import TestCase


class FixtureMixin(TestCase):
    fixtures = ["store/fixtures/shop_wise_db_data.json", ]
