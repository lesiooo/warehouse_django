from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


class SemiFinishedItem(models.Model):
    name = models.TextField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category)
    producer = models.CharField(max_length=50)
    price = models.FloatField()


class FinishedProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=0)
