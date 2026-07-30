from rest_framework import status
from rest_framework.test import APITestCase

from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class ProductViewSetTest(APITestCase):

    def test_create_product(self):
        category = CategoryFactory()

        payload = {
            "title": "Notebook",
            "description": "Notebook Gamer",
            "price": 5000,
            "active": True,
            "categories_id": [category.id]
        }

        response = self.client.post(
            "/bookstore/v1/product/",
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_list_products(self):
        category = CategoryFactory()

        ProductFactory(category=[category])
        ProductFactory(category=[category])

        response = self.client.get("/bookstore/v1/product/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)