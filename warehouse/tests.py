from unittest.mock import patch

from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import Client
from django.test import TestCase
from .models import SemiFinishedItem, FinishedProduct, Category
from .forms import *
from .views import *
from django.contrib.auth.models import User
from django.contrib.auth import login
from .filters import SemiFinishedItemFilter

class ModelClassTest(TestCase):

    def setUp(self):
        super(ModelClassTest, self).setUp()
        self.category = Category.objects.create(name='Category')
        self.user = User.objects.create_user('lesio', 'lesio@mail.com', 'leszek')
        self.client = Client()
        self.login = self.client.login(username='lesio', password='leszek')


    def tearDown(self):
        super(ModelClassTest, self).tearDown()
        self.category.delete()
        self.user.delete()

    def test_home_page(self):
        request = HttpRequest()
        response = home_page(request)

        self.assertEqual(response.status_code, 200)

    def test_saving_category(self):
        self.category = Category.objects.create(name='Category')
        self.assertEqual(self.category.name, 'Category')


    def test_saving_semi_finished_item(self):

        self.semi_finished_item = SemiFinishedItem.objects.create(
            name='semi-finished item', quantity=20,
            price=12.50, category=self.category)


        self.assertEqual(self.semi_finished_item.name, 'semi-finished item')
        self.assertEqual(self.semi_finished_item.slug, 'semi-finished-item')
        self.assertEqual(self.semi_finished_item.category.name, 'Category')
        self.assertEqual(SemiFinishedItem.objects.all().count(),1)

    def test_finished_product(self):
        finished_product = FinishedProduct.objects.create(
            name='finished product', quantity=23, price=33.20)

        self.assertEqual(finished_product.name, 'finished product')
        self.assertEqual(finished_product.slug, 'finished-product')
        self.assertEqual(finished_product.quantity, 23)
        self.assertEqual(finished_product.price, 33.20)

    def test_login(self):

        self.assertTrue(self.login)


    def test_create_semi_finished_item_form(self):
        self.form = CreateSemiFinishedItemForm(data={'name': 'Test Item', 'category': self.category.id,
                                                'producer': 'Producent', 'price':12.50})
        self.form.save()

        self.assertTrue(self.form.is_valid())
        self.assertEqual(SemiFinishedItem.objects.all().count(),1)
        self.assertEqual(SemiFinishedItem.objects.first().name, 'Test Item')
        self.assertEqual(SemiFinishedItem.objects.first().slug, 'test-item')
        self.assertEqual(SemiFinishedItem.objects.first().quantity, 0)
        self.assertEqual(SemiFinishedItem.objects.first().category.name , 'Category')

    def test_create_finished_product_form(self):

        self.form = CreateFinishedProduct(data={'name':' Finished Product', 'price': 12.50, 'EAN_code': '1234567890113'})

        self.assertTrue(self.form.is_valid())
        self.form.save()

        self.assertTrue(FinishedProduct.objects.first().name , 'Finished Product')
        self.assertTrue(FinishedProduct.objects.first().slug , 'finished-product')
        self.assertTrue(FinishedProduct.objects.first().price , 12.50)
        self.assertTrue(FinishedProduct.objects.first().EAN_code, '1234567890113')
        #self.assertTrue(FinishedProduct.objects.first().quantity , 0)


    def test_view_POST_create_semi_item(self):
        self.request = HttpRequest()
        self.request.method = 'POST'
        self.request.POST['name'] = 'New Product'
        self.request.POST['category'] = self.category.id
        self.request.POST['price'] = 12.50
        self.request.POST['producer'] = 'Producent'
        self.request.user = self.user

        self.response = create_semi_finished_item_view(self.request)

        self.assertEqual(SemiFinishedItem.objects.all().count(), 1)
        self.new_item = SemiFinishedItem.objects.first()
        self.assertEqual(self.new_item.name, 'New Product')
        self.assertEqual(self.new_item.slug, 'new-product')
        self.assertEqual(self.new_item.quantity, 0)
        self.assertEqual(self.new_item.category.name, 'Category')



    def test_view_post_create_finished_item(self):
        self.request = HttpRequest()
        self.request.method = 'POST'
        self.request.POST['name'] = 'Finished Product'
        self.request.POST['price'] = 12.50
        self.request.POST['EAN_code'] = '1234567890113'
        self.request.user= self.user

        self.response = create_finished_product_view(self.request)

        self.assertEqual(FinishedProduct.objects.count(),1)
        self.new_product = FinishedProduct.objects.first()
        self.assertEqual(self.new_product.name, 'Finished Product')
        self.assertEqual(self.new_product.slug, 'finished-product')
        self.assertEqual(self.new_product.price , 12.50)
        self.assertEqual(self.new_product.EAN_code , '1234567890113')

    def test_view_semi_finished_item_details(self):
        SemiFinishedItem.objects.create(name='Semi finished item', category=self.category,
                                               price=12, quantity=20, producer='Producer')
        item = SemiFinishedItem.objects.first()
        response = self.client.get(str(item.get_absolute_url()))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Semi finished item')
        self.assertContains(response, 'Producer')
        self.assertContains(response, 20)

    def test_view_finished_product_details(self):
        item = FinishedProduct.objects.create(name='Finished product', price=12.5, EAN_code='1234567890123', quantity=124)

        response = self.client.get(str(item.get_absolute_url()))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Finished product')
        self.assertContains(response, '1234567890123')
        self.assertContains(response, 124)

    def test_edit_semi_finished_item_view(self):
        item = SemiFinishedItem.objects.create(name='Semi finished item', category=self.category,
                                               price=12, quantity=20, producer='Producer')

        self.request = HttpRequest()
        self.request.method = 'POST'
        self.request.POST['price'] = 123
        self.request.POST['quantity'] = 50
        self.request.POST['producer'] = 'Producer'
        self.request.user = self.user

        self.response = semi_finished_item_edit_view(self.request, item.slug)

        self.assertEqual(SemiFinishedItem.objects.count(),1)
        self.assertEqual(SemiFinishedItem.objects.first().name, 'Semi finished item')
        self.assertEqual(SemiFinishedItem.objects.first().price, 123)
        self.assertEqual(SemiFinishedItem.objects.first().quantity, 50)


    def test_edit_finished_product_item_edit(self):
        item = FinishedProduct.objects.create(name='Finished product', price=12.5, EAN_code='1234567890123', quantity=124)
        self.request = HttpRequest()
        self.request.method = 'POST'
        self.request.POST['price'] = 123
        self.request.POST['quantity'] = 50
        self.request.POST['EAN_code'] = '1234567890123'
        self.request.user = self.user

        self.response = finished_product_edit_view(self.request, item.slug)

        self.assertEqual(FinishedProduct.objects.first().price, 123)
        self.assertEqual(FinishedProduct.objects.first().quantity, 50)


    def test_semi_finished_item_filter(self):

        base_url ='/warehouse/semi-finisheditem/search/'
        item = SemiFinishedItem.objects.create(name='Semi finished item', category=self.category,
                                               price=12, quantity=20, producer='Producer')
        item2 = SemiFinishedItem.objects.create(name='test item', category=self.category,
                                               price=1, quantity=210, producer='Producer2')

        self.response = self.client.get(base_url)

        self.assertContains(self.response, 'Semi finished item')
        self.assertContains(self.response, 'Category')
        self.assertContains(self.response, 'test item')

        self.response2 = self.client.get(base_url+'?name=test&producer=Producer&category=')
        self.assertContains(self.response2, 'test item')
        #self.assertNotContains(self.response2, 'Semi finished item')



