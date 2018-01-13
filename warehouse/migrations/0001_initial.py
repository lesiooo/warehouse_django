# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FinishedProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField(max_length=255)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SemiFinishedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('producer', models.TextField(max_length=50)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(to='warehouse.Category')),
            ],
        ),
    ]
