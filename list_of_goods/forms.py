from django import forms


class AddItemToListGoodsForm(forms.Form):
    quantity = forms.FloatField()
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
