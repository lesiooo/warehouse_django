from django.conf.urls import url
from .views import SemiFinishedItemRUDView, SemiFinishedItemAPIView

urlpatterns = [
    url(r'^(?P<id>\d+)/$', SemiFinishedItemRUDView.as_view(), name='semi-finished_item-create'),
    url(r'^$', SemiFinishedItemAPIView.as_view(), name='semi-finished-item-api')
]