from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_of_goods_detail, name='list_of_goods_detail'),
    url(r'^add/(?P<item_id>\d+)/$', views.list_of_goods_add_item, name='list_of_goods_add'),
    url(r'^remove/(?P<item_id>\d+)/$', views.list_of_goods_remove_item, name='list_of_goods_remove'),
    url(r'^list-finished/$', views.list_of_finished_product_detail_view, name='list_of_finished_product_detail'),
    url(r'^add-finished/(?P<item_id>\d+)/$', views.list_of_finished_product_add_item, name='list_finished_product_add'),
    url(r'^remove-finished/(?P<item_id>\d+)/$', views.list_of_finished_product_remove_item, name='list_finished_product_remove'),
]