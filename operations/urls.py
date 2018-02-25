from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^operation/(?P<type_operation>\w{2})/$', operation_view, name='operation'),
    url(r'^operation-detail/(?P<operation_number>[\/\w]+)', operation_detail_view, name='operation_detail'),
    url(r'^operation-finished-product/(?P<type_operation>\w{2})/$', operation_finished_product_view, name='operation_finished_product'),
    url(r'^operation-pdf/(?P<operation_number>[\/\w]+)', generate_pdf_operation, name='operation_pdf'),
    url(r'^stocktaking/$', generate_stocktaking_list_view, name='stocktaking'),


]