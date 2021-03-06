import weasyprint
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils import timezone

from list_of_goods.list_of_goods import ListGoods, ListFinishedProducts
from .models import Operiation, OperationItem, OperationFinishedProduct
from warehouse.models import SemiFinishedItem, FinishedProduct



"""
    ('ER', 'External Goods Receipt'),
    ('IR', 'Internal Receipt Product Movement from production'),
    ('IS', 'Internal Send Product Movement to production'),
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
            edit_item = SemiFinishedItem.objects.get(id=item['item'].id)
            if type_operation == 'OD' or type_operation == 'IS':
                edit_item.quantity -= item['quantity']
            elif type_operation == 'ER' or type_operation == 'IR':
                edit_item.quantity += item['quantity']
            edit_item.save()
        list_of_goods.clear()
        return render(request, 'operations/operation_success.html',{'list_of_items': list_of_goods, 'type_operation': operation.operation})
    else:
        return redirect('list_of_goods_detail')

def operation_finished_product_view(request, type_operation):
    list_of_finished_products = ListFinishedProducts(request)
    if bool(list_of_finished_products):
        count_operation = Operiation.objects.filter(operation=type_operation).count()
        operation_number = type_operation + '/' + str(count_operation) + '/' + str(timezone.now().year)
        operation = Operiation.objects.create(worker=request.user, operation=type_operation,
                                              operation_number=operation_number)
        for item in list_of_finished_products:
            OperationFinishedProduct.objects.create(
                operation=operation,
                item=item['item'],
                quantity=item['quantity'])
            edit_item = FinishedProduct.objects.get(id=item['item'].id)
            if type_operation == 'OD' or type_operation == 'IS':
                edit_item.quantity -= item['quantity']
            elif type_operation == 'ER' or type_operation == 'IR':
                edit_item.quantity += item['quantity']
            edit_item.save()
        list_of_finished_products.clear()
        return render(request, 'operations/operation_success.html',
                      {'list_of_items': list_of_finished_products, 'type_operation': operation.operation})
    else:
        return redirect('list_of_finished_product_detail')


def operation_detail_view(request, operation_number):
    operation = Operiation.objects.get(operation_number=str(operation_number))
    operation_items = OperationItem.objects.filter(operation=operation)
    operation_finished_items = OperationFinishedProduct.objects.filter(operation=operation)
    return render(request, 'operations/operation_detail.html',
                  {'operation': operation, 'operation_items': operation_items,
                   'operation_finished_products': operation_finished_items})


def generate_pdf_operation(request, operation_number):
    operation = Operiation.objects.get(operation_number=str(operation_number))
    operation_items = OperationItem.objects.filter(operation=operation)
    operation_finished_products = OperationFinishedProduct.objects.filter(operation=operation)
    html = render_to_string('operations/operation_pdf.html',
                            {'operation': operation, 'operation_items': operation_items,
                             'operation_finished_products': operation_finished_products})
    response = HttpResponse(content_type='aplication/pdf')
    response['Content-Disposition'] = 'filename="{}.pdf"'.format(operation.operation_number)
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS('operations/static/pdf_style.css')])
    return response

def generate_stocktaking_list_view(request):
    semi_finished_items = SemiFinishedItem.objects.all().order_by('category__name').order_by('name')
    finished_products = FinishedProduct.objects.all().order_by('name')

    html = render_to_string('operations/stocktaking.html',
                            {'semi_finished_items': semi_finished_items, 'finished_products': finished_products})
    response = HttpResponse(content_type='aplication/pdf')
    response['Content-Disposition'] = 'filename=stocktaking_{}.pdf'.format(timezone.now().date())
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS('operations/static/pdf_style.css')])
    return response