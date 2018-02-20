from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from warehouse.models import SemiFinishedItem


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


class OperationItem(models.Model):
    operation = models.ForeignKey(Operiation, related_name='operation_type')
    item = models.ForeignKey(SemiFinishedItem, related_name='operation_item')
    quantity = models.DecimalField(max_digits=8, decimal_places=2)