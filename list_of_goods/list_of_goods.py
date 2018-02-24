from decimal import Decimal
from django.conf import settings
from warehouse.models import SemiFinishedItem, FinishedProduct

class ListGoods(object):

    def __init__(self, request):

        self.session = request.session
        list_of_goods = self.session.get(settings.LIST_OF_GOODS_SESION_ID)
        if not list_of_goods:
            list_of_goods = self.session[settings.LIST_OF_GOODS_SESION_ID] = {}
        self.list_of_goods = list_of_goods


    def add(self, item, quantity=1, update_quantity=False):

        item_id = str(item.id)
        if item_id not in self.list_of_goods:
            self.list_of_goods[item_id] = {'quantity': 0}
        if update_quantity:
            self.list_of_goods[item_id]['quantity'] = quantity
        else:
            self.list_of_goods[item_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.LIST_OF_GOODS_SESION_ID] = self.list_of_goods
        self.session.modified = True

    def remove(self, item):
        item_id = str(item.id)
        if item_id in self.list_of_goods:
            del self.list_of_goods[item_id]
            self.save()

    def __iter__(self):
        item_ids = self.list_of_goods.keys()
        items = SemiFinishedItem.objects.filter(id__in=item_ids)
        for item in items:
            self.list_of_goods[str(item.id)]['item'] = item
        for item in self.list_of_goods.values():
            yield item

    def clear(self):
        del self.session[settings.LIST_OF_GOODS_SESION_ID]
        self.session.modified = True


class ListFinishedProducts(object):

    def __init__(self, request):
        self.session = request.session
        list_of_finished_products = self.session.get(settings.LIST_OF_FINISHED_PRODUCTS_SESSION_ID)
        if not list_of_finished_products:
            list_of_finished_products = self.session[settings.LIST_OF_FINISHED_PRODUCTS_SESSION_ID] = {}
        self.list_of_finished_products = list_of_finished_products

    def add(self, item, quantity=1, update_quantity=False):

        item_id = str(item.id)
        if item_id not in self.list_of_finished_products:
            self.list_of_finished_products[item_id] = {'quantity': 0}
        if update_quantity:
            self.list_of_finished_products[item_id]['quantity'] = quantity
        else:
            self.list_of_finished_products[item_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.LIST_OF_FINISHED_PRODUCTS_SESSION_ID] = self.list_of_finished_products
        self.session.modified = True

    def remove(self, item):
        item_id = str(item.id)
        if item_id in self.list_of_finished_products:
            del self.list_of_finished_products[item_id]
            self.save()

    def __iter__(self):
        item_ids = self.list_of_finished_products.keys()
        items = FinishedProduct.objects.filter(id__in=item_ids)
        for item in items:
            self.list_of_finished_products[str(item.id)]['item'] = item
        for item in self.list_of_finished_products.values():
            yield item

    def clear(self):
        del self.session[settings.LIST_OF_FINISHED_PRODUCTS_SESSION_ID]
        self.session.modified = True