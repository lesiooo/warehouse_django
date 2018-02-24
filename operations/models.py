from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from warehouse.models import SemiFinishedItem, FinishedProduct
from django.utils import timezone



OPERATION_CHOICES =(
    ('ER', 'External Goods Receipt'),
    ('IR', 'Internal Receipt Product Movement'),
    ('IS', 'Internal Send Product Movement'),
    ('OD', 'Outbound Delivery')

)


class Operiation(models.Model):
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='warehouse_worker')
    created = models.DateField(auto_now=True)
    operation = models.CharField(max_length=50, choices=OPERATION_CHOICES)
    operation_number = models.CharField(max_length=15)

    def save(self, *args, **kwargs):

        super().save()

    def get_absolute_url(self):
        return reverse('operation_detail', kwargs={'operation_number': self.operation_number,})

class OperationItem(models.Model):
    operation = models.ForeignKey(Operiation, related_name='operation_type')
    item = models.ForeignKey(SemiFinishedItem, related_name='operation_item')
    quantity = models.DecimalField(max_digits=8, decimal_places=2)


class OperationFinishedProduct(models.Model):
    operation = models.ForeignKey(Operiation, related_name='operation_finished_type')
    item = models.ForeignKey(FinishedProduct, related_name='operation_product')
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
