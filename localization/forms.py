from django import forms
from .models import LocalizationItem


class LocalizationItemForm(forms.ModelForm):
    label = forms.CharField(max_length=2)
    place = forms.IntegerField()

    class Meta:
        model = LocalizationItem
        fields = ('label', 'place')
        exclude=('localization', 'item', 'date_of_placement')
