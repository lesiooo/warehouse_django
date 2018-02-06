from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^semi-finisheditem/new/$', create_semi_finished_item_view, name='create_semifinisheditem'),
    url(r'^semi-finisheditem/(?P<slug>[-\w]+)/details/$', semi_finished_item_detail, name='semi_finished_item_detail'),
    url(r'^semi-finisheditem/(?P<slug>[-\w]+)/edit/$', semi_finished_item_edit_view, name='semi_finished_item_edit'),

    url(r'^finishedproduct/new/$', create_finished_product_view, name='create_finishedproduct'),
    url(r'^finishedproduct/(?P<slug>[-\w]+)/details/$', finished_product_details, name='finished_item_details'),
    url(r'^finishedproduct/(?P<slug>[-\w]+)/edit/$', finished_product_edit_view, name='finished_item_edit'),

]