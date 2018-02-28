from django.conf.urls import url
from .views import SemiFinishedItemRUDView, SemiFinishedItemAPIView, FinishedProductRUDView,FinishedProductAPIView

urlpatterns = [
    url(r'^semi-finished-item/(?P<id>\d+)/$', SemiFinishedItemRUDView.as_view(), name='semi-finished-item-rud'),
    url(r'^semi-finished-item/$', SemiFinishedItemAPIView.as_view(), name='semi-finished-item-api'),
    url(r'^finished-product/(?P<id>\d+)/$', FinishedProductRUDView.as_view(), name='finished-product-rud'),
    url(r'^finished-product/$', FinishedProductAPIView.as_view(), name='finished-product-api'),
]