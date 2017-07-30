from django.test import TestCase
from django.core.urlresolvers import resolve
from views import all_products

# Create your tests here.
class productPageTest(TestCase):
    def test_products_page_resolves(self):
        products_page = resolve('/products/')
        self.assertEqual(products_page.func, all_products)

