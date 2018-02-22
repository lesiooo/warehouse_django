from django.test import TestCase
from django.http import HttpRequest
from django.test import Client
from .models import Operiation, OperationItem
from list_of_goods.list_of_goods import ListGoods
from django.contrib.auth.models import User
from warehouse.models import SemiFinishedItem, Category
from .views import operation_view, operation_detail_view

class OperationModuleTest(TestCase):

    def setUp(self):
        super(OperationModuleTest, self).setUp()
        self.client = Client()
        self.user = User.objects.create_user('lesio', 'lesio@mail.com', 'leszek')
        self.login = self.client.login(username='lesio', password='leszek')
        self.category = Category.objects.create(name='Category')
        self.item_1 = SemiFinishedItem.objects.create(
            name='semi-finished item', quantity=20,
            price=12.50, category=self.category)
        self.item_2 = SemiFinishedItem.objects.create(
            name='test item', quantity=40,
            price=8,category=self.category)

    def tearDown(self):
        super(OperationModuleTest, self).tearDown()
        self.user.delete()

    def test_add_adn_remove_item_to_list_item(self):
        self.request = HttpRequest()
        session = self.client.session
        self.request.session = session
        self.list_items = ListGoods(self.request)
        self.list_items.add(self.item_1, 10)

        #if list items is empty == False
        self.assertTrue(self.list_items.list_of_goods)
        self.list_items.remove(self.item_1)
        self.assertFalse(self.list_items.list_of_goods)


    def test_ER_IR_operation_view(self):
        self.request = HttpRequest()
        session = self.client.session
        self.request.session = session
        self.request.user = self.user
        self.list_items = ListGoods(self.request)
        self.list_items.add(self.item_1, 5)
        self.list_items.add(self.item_2, 8)

        self.response = operation_view(self.request, 'ER')

        self.assertEquals(Operiation.objects.count(), 1)
        self.assertEquals(OperationItem.objects.count(), 2)
        operation = Operiation.objects.all()[0]
        self.assertEquals(operation.operation_number, 'ER/0/2018')
        self.item_1 = SemiFinishedItem.objects.get(name='semi-finished item')
        self.item_2 = SemiFinishedItem.objects.get(name='test item')
        self.assertEquals(self.item_1.quantity, 25)
        self.assertEquals(self.item_2.quantity, 48)

    def test_operation_detail_view(self):
        self.request = HttpRequest()
        session = self.client.session
        self.request.session = session
        self.request.user = self.user
        self.list_items = ListGoods(self.request)
        self.list_items.add(self.item_1, 5)
        self.list_items.add(self.item_2, 8)

        self.execute = operation_view(self.request, 'ER')

        self.operation = Operiation.objects.get(operation_number='ER/0/2018')

        self.response = self.client.get(self.operation.get_absolute_url())

        self.assertContains(self.response, 'semi-finished item')
        self.assertContains(self.response, 'test item')
        self.assertContains(self.response, 'ER/0/2018')








