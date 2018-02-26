from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^add/(?P<item_id>\d+)/$', add_localize_item_view, name='add_localization_item'),
    url(r'^remove/(?P<localization_id>\d+)/$', remove_localization_item, name='remove_localization'),

]