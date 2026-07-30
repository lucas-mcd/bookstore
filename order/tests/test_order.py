from django.test import TestCase

from order.tests.factories import OrderFactory


class OrderModelTest(TestCase):

    def test_create_order(self):
        order = OrderFactory()

        self.assertIsNotNone(order.user)
        self.assertEqual(order.product.count(), 1)