from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_of_goods_detail, name='list_of_goods_detail'),
    url(r'^add/(?P<item_id>\d+)/$', views.list_of_goods_add_item, name='list_of_goods_add'),
    url(r'^remove/(?P<item_id>\d+)/$', views.list_of_goods_remove_item, name='list_of_goods_remove'),
]