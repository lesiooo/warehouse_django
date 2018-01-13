from django.test import TestCase
from .models import SemiFinishedItem, FinishedProduct, Category

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





