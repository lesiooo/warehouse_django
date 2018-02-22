# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0007_finishedproduct_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OperationItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('quantity', models.DecimalField(max_digits=8, decimal_places=2)),
                ('item', models.ForeignKey(to='warehouse.SemiFinishedItem', related_name='operation_item')),
            ],
        ),
        migrations.CreateModel(
            name='Operiation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateField(auto_now=True)),
                ('operation', models.CharField(max_length=50, choices=[('ER', 'External Goods Receipt'), ('IR', 'Internal Receipt Product Movement'), ('IS', 'Internal Send Product Movement'), ('OD', 'Outbound Delivery')])),
                ('worker', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='warehouse_worker')),
            ],
        ),
        migrations.AddField(
            model_name='operationitem',
            name='operation',
            field=models.ForeignKey(to='operations.Operiation', related_name='operation_type'),
        ),
    ]
