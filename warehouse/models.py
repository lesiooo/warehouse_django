from django.db import models


class Category(models.Model):
    name = models.TextField(max_length=50)


class SemiFinishedItem(models.Model):
    name = models.TextField(max_length=255)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category)
    producer = models.TextField(max_length=50)
    price = models.FloatField()


class FinishedProduct(models.Model):
    name = models.TextField(max_length=255)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()






# Create your models here.
