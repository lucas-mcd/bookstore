from django.test import TestCase

from product.tests.factories import ProductFactory


class ProductModelTest(TestCase):

    def test_create_product(self):
        product = ProductFactory()

        self.assertEqual(product.title, product.title)
        self.assertIsNotNone(product.price)