from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^operation/(?P<type_operation>\w{2})/$', operation_view, name='operation'),
    url(r'^operation-detail/(?P<operation_number>[\/\w]+)', operation_detail_view, name='operation_detail')

]