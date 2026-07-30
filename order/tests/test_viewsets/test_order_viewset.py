from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from order.models import Order
from product.factories import CategoryFactory, ProductFactory


class OrderViewSetTest(APITestCase):

    def test_create_order(self):
        category = CategoryFactory()

        product1 = ProductFactory(category=[category])
        product2 = ProductFactory(category=[category])

        user = User.objects.create_user(
            username="lucas",
            password="123456"
        )

        payload = {
            "user": user.id,
            "products_id": [
                product1.id,
                product2.id
            ]
        }

        response = self.client.post(
            "/bookstore/v1/order/",
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

        order = Order.objects.first()
        self.assertEqual(order.product.count(), 2)
        self.assertEqual(order.user, user)

    def test_list_orders(self):
        category = CategoryFactory()

        product = ProductFactory(category=[category])

        user = User.objects.create_user(
            username="lucas",
            password="123456"
        )

        order = Order.objects.create(user=user)
        order.product.add(product)

        response = self.client.get("/bookstore/v1/order/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)