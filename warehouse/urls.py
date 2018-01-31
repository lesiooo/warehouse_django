from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^semi-finisheditem/new/$', create_semi_finished_item_view, name='create_semifinisheditem'),
    url(r'^finishedproduct/new/$', create_finished_product_view, name='create_finishedproduct'),


]