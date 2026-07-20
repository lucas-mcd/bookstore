from django.test import TestCase

from product.tests.factories import CategoryFactory


class CategoryModelTest(TestCase):

    def test_create_category(self):
        category = CategoryFactory()

        self.assertEqual(category.title, category.title)
        self.assertIsNotNone(category.slug)
        self.assertIn(category.active, [True, False])