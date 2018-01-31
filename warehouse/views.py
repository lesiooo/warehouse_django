from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreateFinishedProduct, CreateSemiFinishedItemForm
from django.contrib import messages


def home_page(request):
    return render(request, 'home_page.html')

@login_required
def create_semi_finished_item_view(request):
    if request.method == 'POST':
        create_item_form = CreateSemiFinishedItemForm(request.POST)
        if create_item_form.is_valid():
            create_item_form.save()
            #messages.success(request, 'Add Semi-finished item succesful')
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
            create_item_form.save()
            #messages.success(request, 'Add finished product succesfully')
        else:
            #messages.error(request, 'Add finished product unsuccesfully')
            pass
    else:
        create_item_form = CreateFinishedProduct()

    return render(request, 'products_html/create_finishedproduct.html',
                  {'create_item_form': create_item_form })

