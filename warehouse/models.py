from django.core.urlresolvers import reverse
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.db import models
from rest_framework.reverse import reverse as api_reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SemiFinishedItem(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category)
    producer = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SemiFinishedItem, self).save(*args, **kwargs)

    def get_edit_url(self):
        return reverse('semi_finished_item_edit', kwargs={'slug': self.slug,})

    def get_absolute_url(self):
        return reverse('semi_finished_item_detail', kwargs={'slug': self.slug,})

    def get_api_url(self, request=None):
        return api_reverse('api-semi-item:semi-finished-item-rud', kwargs={'id': self.id}, request=request)


class FinishedProduct(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=0)
    EAN_code = models.CharField(max_length=13, default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save()

    def get_edit_url(self):
        return reverse('finished_item_edit', kwargs={'slug': self.slug,})

    def get_absolute_url(self):
        return reverse('finished_item_details', kwargs={'slug': self.slug,})


