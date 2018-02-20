from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from warehouse.models import SemiFinishedItem
from .list_of_goods import ListGoods
from .forms import AddItemToListGoodsForm


@require_POST
def list_of_goods_add_item(request, item_id):
    list_of_goods = ListGoods(request)
    item = get_object_or_404(SemiFinishedItem, id=item_id)
    #item = SemiFinishedItem.objects.filter(id=item_id)
    form = AddItemToListGoodsForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        list_of_goods.add(item=item, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('list_of_goods_detail')


def list_of_goods_remove_item(request, item_id):
    list_of_goods = ListGoods(request)
    item = get_object_or_404(SemiFinishedItem, id=item_id)
    list_of_goods.remove(item)
    return redirect('list_of_goods_detail')


def list_of_goods_detail(request):
    list_of_goods = ListGoods(request)
    for item in list_of_goods:
        item['update_quantity_form'] = AddItemToListGoodsForm(
            initial={'quantity': item['quantity'], 'update': True}
        )
    return render(request, 'list_of_goods/detail.html', {'list_of_goods': list_of_goods})