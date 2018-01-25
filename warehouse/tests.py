from django.test import TestCase
from .models import SemiFinishedItem, FinishedProduct, Category
from .forms import *

class ModelClassTest(TestCase):

    def test_saving_category(self):
        self.category = Category.objects.create(name='Category')
        self.assertEqual(self.category.name, 'Category')


    def test_saving_self_finished_item(self):
        category = Category.objects.create(name='Category')

        self.semi_finished_item = SemiFinishedItem.objects.create(
            name='Semi-finished item', quantity=20,
            price=12.50, category=category)


        self.assertEqual(self.semi_finished_item.name, 'Semi-finished item')
        self.assertEqual(self.semi_finished_item.category.name, 'Category')
        self.assertEqual(SemiFinishedItem.objects.all().count(),1)

    def test_finished_product(self):
        finished_product = FinishedProduct.objects.create(
            name='finished product', quantity=23, price=33.20)

        self.assertEqual(finished_product.name, 'finished product')
        self.assertEqual(finished_product.quantity, 23)
        self.assertEqual(finished_product.price, 33.20)

    def test_create_semi_finished_item_form(self):
        category = Category.objects.create(name='Category')
        self.form = CreateSemiFinishedItemForm(data={'name': 'Item', 'category': category.id,
                                                'producer': 'Producent', 'price':12.50})
        self.form.save()

        self.assertTrue(self.form.is_valid())
        self.assertEqual(SemiFinishedItem.objects.all().count(),1)
        self.assertEqual(SemiFinishedItem.objects.first().name, 'Item')
        self.assertEqual(SemiFinishedItem.objects.first().quantity, 0)
        self.assertEqual(SemiFinishedItem.objects.first().category.name , 'Category')

    def test_create_finished_product_form(self):

        self.form = CreateFinishedProduct(data={'name':'Item', 'price': 12.50})

        self.assertTrue(self.form.is_valid())
        self.form.save()

        self.assertTrue(FinishedProduct.objects.first().name , 'Item')
        self.assertTrue(FinishedProduct.objects.first().price , 12.50)
        #self.assertTrue(FinishedProduct.objects.first().quantity , 0)





