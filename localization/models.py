from django.db import models
from warehouse.models import SemiFinishedItem


class LocalizationItem(models.Model):
    localization = models.CharField(max_length=8, unique=True)
    item = models.ForeignKey(SemiFinishedItem, related_name='localization_item')
    date_of_placement = models.DateField(auto_now=True, blank=False)

    def __str__(self):
        return self.localization
