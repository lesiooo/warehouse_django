from django.shortcuts import render, get_object_or_404, redirect
from .forms import LocalizationItemForm
from .models import LocalizationItem
from django.views.decorators.http import require_POST
from warehouse.models import SemiFinishedItem

@require_POST
def add_localize_item_view(request, item_id):
    item = get_object_or_404(SemiFinishedItem, id=item_id)
    form = LocalizationItemForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        place = str(cd['label']) + str(cd['place'])
        localization_item_add = LocalizationItem.objects.create(localization=place, item=item)
        localization_item_add.save()
    return redirect(item.get_absolute_url())

def remove_localization_item(request, localization_id):
    localization = get_object_or_404(LocalizationItem, id=localization_id)
    localization.delete()
    return redirect('home_page')