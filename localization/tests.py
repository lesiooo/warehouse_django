from django.http import HttpRequest
from django.test import TestCase
from warehouse.models import SemiFinishedItem, Category
from.models import LocalizationItem
from .views import *


class TestLocalizationItem(TestCase):

    def setUp(self):
        super(TestLocalizationItem, self).setUp()
        self.category = Category.objects.create(name='Category')
        self.item_1 = SemiFinishedItem.objects.create(
            name='semi-finished item', quantity=20,
            price=12.50, category=self.category)

    def test_model_localization_item(self):
        self.localization_item = LocalizationItem.objects.create(localization='L110', item=self.item_1)
        self.assertEqual(LocalizationItem.objects.first().localization, 'L110')
        self.assertEqual(LocalizationItem.objects.first().item, self.item_1)


    def test_localization_add_view(self):
        self.request = HttpRequest()
        self.request.method = 'POST'
        self.request.POST['label'] = 'L'
        self.request.POST['place'] = 110

        self.response = add_localize_item_view(self.request, self.item_1.id)

        self.assertEquals(LocalizationItem.objects.count(), 1)
        localization = LocalizationItem.objects.first()
        self.assertEqual(localization.localization, 'L110')
        self.assertEqual(localization.item, self.item_1)

    def test_remove_localization(self):
        localization = LocalizationItem.objects.create(localization='L110', item=self.item_1)
        localization2 = LocalizationItem.objects.create(localization= 'L215', item=self.item_1)

        self.assertEqual(LocalizationItem.objects.count(), 2)
        self.request = HttpRequest()

        self.response = remove_localization_item(self.request, localization.id)
        self.assertEqual(LocalizationItem.objects.count(),1)
