from .models import Category, SemiFinishedItem, FinishedProduct
from django import forms
import django_filters


def get_category_names():
    category_names = ()
    category = Category.objects.all()
    for item in category:
        category_names += (item.id, item.name),
    return category_names


class SemiFinishedItemFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')
    producer = django_filters.CharFilter(lookup_expr='icontains')
    test = Category.objects.all()
    category = django_filters.ChoiceFilter(
        choices=get_category_names, label='Category')



    class Meta:
        model = SemiFinishedItem
        fields = ['name', 'category', 'producer']


class FinishedProductFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')
    EAN_code = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = FinishedProduct
        fields = ['name', 'EAN_code']
