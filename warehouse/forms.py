from django import forms
from django.forms import ModelChoiceField

from .models import SemiFinishedItem, FinishedProduct, Category


class CategoryName(ModelChoiceField):
    def label_from_instance(self, obj):
        return str(obj.name)

class CreateSemiFinishedItemForm(forms.ModelForm):

    category = CategoryName(Category.objects.all())
    def __init__(self, *args, **kwargs):
        super(CreateSemiFinishedItemForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    class Meta:
        model = SemiFinishedItem
        fields = ('name', 'category', 'producer', 'price')
        exclude = ('quantity',)


class SemiFinishedItemEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SemiFinishedItemEditForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = SemiFinishedItem
        fields = ('producer', 'price', 'quantity')
        exclude = ('name', 'category')


class CreateFinishedProduct(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateFinishedProduct, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = FinishedProduct
        fields = ('name', 'price', 'EAN_code')
        exclude = ('quantity',)


class FinishedProductEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FinishedProductEditForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = FinishedProduct
        fields = ('price', 'quantity', 'EAN_code')