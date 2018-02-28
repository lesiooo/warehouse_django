from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from warehouse.models import SemiFinishedItem, Category, FinishedProduct
from rest_framework.reverse import reverse as api_reverse
from rest_framework_jwt.settings import api_settings

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

class SemiFinishedItemAPITest(APITestCase):

    def setUp(self):
        super(SemiFinishedItemAPITest, self).setUp()
        self.user = User.objects.create_user('lesio', 'lesio@mail.com', 'leszek')
        self.category = Category.objects.create(name='Category')
        self.item = SemiFinishedItem.objects.create(name='Semi finished item', category=self.category,
                                               price=12, quantity=20, producer='Producer')


    def test_get_api_semi_finished_list(self):
        data = {}
        url = api_reverse('api-warehouse:semi-finished-item-api')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_item_api(self):
        item = SemiFinishedItem.objects.first()
        data = {}
        url = item.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_post_api_semi_finished_item(self):
        data = {'name': 'test_api', 'category': self.category.id, 'producer':'Leszek', 'quantity': 11}
        url = api_reverse('api-warehouse:semi-finished-item-api')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401) #HTTP_401_UNAUTHORIZED  User doesn't exist

    def test_post_api_semi_finished_item_with_user(self):
        data = {'name': 'test_api', 'category': self.category.id, 'producer': 'Leszek', 'quantity': 11, 'price':5}
        url = api_reverse('api-warehouse:semi-finished-item-api')

        user = User.objects.first()
        payload = payload_handler(user)
        token = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201) # HTTP_201_CREATED
        self.assertEqual(SemiFinishedItem.objects.count(), 2)

    def test_update_item(self):
        item = SemiFinishedItem.objects.first()
        url = item.get_api_url()
        data = {'name': 'test_update_api', 'category':self.category.id,
                'price':12, 'quantity':20, 'producer':'Producer'}
        user = User.objects.first()
        payload = payload_handler(user)
        token = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 405) # HTTP_405_METHOD_NOT_ALOWED
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)

class FinishedProductAPITest(APITestCase):

    def setUp(self):
        super(FinishedProductAPITest, self).setUp()
        product = FinishedProduct.objects.create(name='test product', price=12, quantity=20, EAN_code=9876543210123)

    def test_get_products_list(self):
        data = {}
        url = api_reverse('api-warehouse:finished-product-api')
        respone = self.client.get(url, data, format='json')
        self.assertEqual(respone.status_code, 200)

    def test_get_product(self):
        product = FinishedProduct.objects.first()
        data = {}
        url = product.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        data = {'name': 'test update product', 'price':30, 'quantity': 20, 'EAN_code': 9876543210123}
        product = FinishedProduct.objects.first()
        url = product.get_api_url()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_update_product_with_user(self):
        user = User.objects.create_user('lesio', 'lesio@mail.com', 'leszek')
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        data = {'name': 'test update product', 'price': 30, 'quantity': 20, 'EAN_code': 9876543210123}
        product = FinishedProduct.objects.first()
        url = product.get_api_url()

        payload = payload_handler(user)
        token = encode_handler(payload)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_post_product(self):
        user = User.objects.create_user('lesio', 'lesio@mail.com', 'leszek')
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        data = {'name': 'test update product', 'price': 30, 'quantity': 20, 'EAN_code': 9876543210123}
        product = FinishedProduct.objects.first()
        url = product.get_api_url()

        payload = payload_handler(user)
        token = encode_handler(payload)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 405) # HTTP_405_METHOD_NOT_ALOWED
