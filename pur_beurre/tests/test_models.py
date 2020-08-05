# import pprint

from django.test import TestCase
from user import models as usr
from product import models as prd


class UserTestCase(TestCase):
    def setUp(self):
        usr.User.objects.create(
            first_name="Lionel",
            last_name="Lenoil",
            password="123",
            status=1)
        usr.User.objects.create(
            first_name="Catherine",
            last_name="Enirehtac",
            password="456",
            status=0)

    def test_users_are_users(self):
        """Users are correctly identified"""
        lionel = usr.User.objects.get(
            first_name="Lionel",
            last_name="Lenoil",
            password="123",
            status=1)
        catherine = usr.User.objects.get(
            first_name="Catherine",
            last_name="Enirehtac",
            password="456",
            status=0)
        #        pprint.pprint(catherine)
        #        pprint.pprint(lionel)

        self.assertEqual(catherine.last_name, "Enirehtac")
        self.assertEqual(lionel.last_name, "Lenoil")


class ProductTestCase(TestCase):
    def setUp(self):
        prd.Product.objects.create(
            code='0000000000001',
            name='product 001',
            generic_name='product prd 001',
            brands='Brand of prd 001',
            stores='stores001',
            url='url001')

        prd.Product.objects.create(
            code='0000000000002',
            name='product 002',
            generic_name='product prd 002',
            brands='Brand of prd 002',
            stores='stores002',
            url='url002')

    def test_products_are_products(self):
        """Products are correctly identified"""
        prd1 = prd.Product.objects.get(
            code='0000000000001',
            name='product 001',
            generic_name='product prd 001',
            brands='Brand of prd 001',
            stores='stores001',
            url='url001')
        prd2 = prd.Product.objects.get(
            code='0000000000002',
            name='product 002',
            generic_name='product prd 002',
            brands='Brand of prd 002',
            stores='stores002',
            url='url002')

        self.assertEqual(prd1.code, '0000000000001')
        self.assertEqual(prd2.code, '0000000000002')


class CategoryTestCase(TestCase):
    def setUp(self):
        prd.Category.objects.create(
            tag='tg0001',
            name='category 001',
            url='url001')

        prd.Category.objects.create(
            tag='tg0002',
            name='category 002',
            url='url002')

    def test_categories_are_categories(self):
        """categories are correctly identified"""
        cat1 = prd.Category.objects.get(
            tag='tg0001',
            name='category 001',
            url='url001')
        cat2 = prd.Category.objects.get(
            tag='tg0002',
            name='category 002',
            url='url002')

        self.assertEqual(cat1.tag, 'tg0001')
        self.assertEqual(cat2.tag, 'tg0002')
