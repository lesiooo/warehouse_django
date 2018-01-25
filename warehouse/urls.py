from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^semi-finisheditem/new/$', create_semi_finished_item_view, name='create_semifinisheditem'),
    url(r'^finishedproduct/new/$', create_finished_product_view, name='create_finishedproduct'),


]