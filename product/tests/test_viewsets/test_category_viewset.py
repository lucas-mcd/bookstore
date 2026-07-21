from rest_framework import status
from rest_framework.test import APITestCase

from product.factories import CategoryFactory
from product.models import Category


class CategoryViewSetTest(APITestCase):

    def test_create_category(self):
        payload = {
            "title": "Eletrônicos",
            "slug": "eletronicos",
            "description": "Produtos eletrônicos",
            "active": True
        }

        response = self.client.post(
            "/bookstore/v1/category/",
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)

    def test_list_categories(self):
        CategoryFactory()
        CategoryFactory()

        response = self.client.get("/bookstore/v1/category/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)