from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from list_of_goods.list_of_goods import ListGoods
from .models import Operiation, OperationItem
from warehouse.models import SemiFinishedItem



"""
    ('ER', 'External Goods Receipt'),
    ('IR', 'Internal Receipt Product Movement'),
    ('IS', 'Internal Send Product Movement'),
    ('OD', 'Outbound Delivery')
"""

@login_required
def operation_view(request, type_operation):
    list_of_goods = ListGoods(request)
    if bool(list_of_goods.list_of_goods) :
        count_operation = Operiation.objects.filter(operation=type_operation).count()
        operation_number = type_operation + '/' + str(count_operation) + '/' + str(timezone.now().year)
        operation = Operiation.objects.create(worker=request.user, operation=type_operation, operation_number=operation_number)
        for item in list_of_goods:
            OperationItem.objects.create(
                operation=operation,
                item=item['item'],
                quantity=item['quantity'])
            edit_item = (SemiFinishedItem.objects.filter(id=item['item'].id))[0]
            if type_operation == 'OD' or type_operation == 'IS':
                edit_item.quantity -= item['quantity']
            elif type_operation == 'ER' or type_operation == 'IR':
                edit_item.quantity += item['quantity']
            edit_item.save()
        list_of_goods.clear()
        return render(request, 'operations/operation_success.html',{'list_of_goods': list_of_goods, 'type_operation': operation.operation})
    else:
        return redirect('list_of_goods_detail')


def operation_detail_view(request, operation_number):
    operation = Operiation.objects.get(operation_number=str(operation_number))
    operation_items = OperationItem.objects.filter(operation=operation)
    return render(request, 'operations/operation_detail.html', {'operation': operation, 'operation_items': operation_items})