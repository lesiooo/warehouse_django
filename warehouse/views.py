from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateFinishedProduct, CreateSemiFinishedItemForm, SemiFinishedItemEditForm, FinishedProductEditForm
from django.contrib import messages
from .models import SemiFinishedItem, FinishedProduct
from .filters import SemiFinishedItemFilter, FinishedProductFilter
from list_of_goods.forms import AddItemToListGoodsForm
from operations.models import OperationItem

def home_page(request):
    semi_finished_items = FinishedProduct.objects.all()
    return render(request, 'home_page.html', {'semi_finished_items': semi_finished_items})

@login_required
def create_semi_finished_item_view(request):
    if request.method == 'POST':
        create_item_form = CreateSemiFinishedItemForm(request.POST)
        if create_item_form.is_valid():
            item = create_item_form.save()
            #messages.success(request, 'Add Semi-finished item succesful')
            return redirect(item.get_absolute_url())
        else:
            #messages.error(request, 'Add semi-finished item unsuccesfully')
            pass

    else:
        create_item_form = CreateSemiFinishedItemForm()

    return render(request, 'products_html/create_semifinisheditem.html',
                     {'create_item_form':create_item_form})


@login_required
def create_finished_product_view(request):
    if request.method == 'POST':
        create_item_form = CreateFinishedProduct(request.POST)
        if create_item_form.is_valid():
            item = create_item_form.save()
            #messages.success(request, 'Add finished product succesfully')
            return redirect(item.get_absolute_url())
        else:
            #messages.error(request, 'Add finished product unsuccesfully')
            pass

    else:
        create_item_form = CreateFinishedProduct()

    return render(request, 'products_html/create_finishedproduct.html',
                     {'create_item_form': create_item_form })

def semi_finished_item_detail(request, slug):
    item = SemiFinishedItem.objects.get(slug=slug)
    list_of_goods_item_form = AddItemToListGoodsForm()
    operations = OperationItem.objects.filter(item=item).order_by('-operation__created')
    return render(request, 'products_html/semi_finished_item_detail.html',
                  {'item': item, 'add_item_form': list_of_goods_item_form, 'operations': operations})

@login_required
def semi_finished_item_edit_view(request, slug):
    item = SemiFinishedItem.objects.get(slug=slug)
    if request.method == 'POST':
        edit_item_form = SemiFinishedItemEditForm(instance=item, data=request.POST)
        if edit_item_form.is_valid():
            edit_item_form.save()
            return redirect(item.get_absolute_url())
    else:
        edit_item_form = SemiFinishedItemEditForm(instance=item)
    return render(request, 'products_html/semi_finished_item_edit.html', {'edit_item_form': edit_item_form})


def finished_product_details(request, slug):
    item = FinishedProduct.objects.get(slug=slug)
    list_of_goods_item_form = AddItemToListGoodsForm()
    return render(request, 'products_html/finished_product_details.html',
                  {'item': item,'add_item_form': list_of_goods_item_form})

@login_required
def finished_product_edit_view(request, slug):
    item = FinishedProduct.objects.get(slug=slug)

    if request.method == 'POST':
        edit_product_form = FinishedProductEditForm(instance=item, data=request.POST)
        if edit_product_form.is_valid():
            edit_product_form.save()
            return redirect(item.get_absolute_url())
    else:
        edit_product_form = FinishedProductEditForm(instance=item)
    return render(request, 'products_html/finished_product_edit.html', {'edit_product_form': edit_product_form})

def search_semi_finished_item_view(request):
    item_list = SemiFinishedItem.objects.all()
    item_filter = SemiFinishedItemFilter(request.GET, queryset=item_list)
    return render(request, 'products_html/semi_finished_item_search.html', {'filter':item_filter})

def search_finished_product_view(request):
    product_list = FinishedProduct.objects.all()
    product_filter = FinishedProductFilter(request.GET, queryset=product_list)
    return render(request, 'products_html/finished_product_search.html', {'filter': product_filter})