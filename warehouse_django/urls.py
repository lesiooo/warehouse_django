"""warehouse_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from warehouse.views import home_page

urlpatterns = [
    url(r'^$', home_page, name='home_page'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^warehouse/', include('warehouse.urls')),
    url(r'list-of-goods/', include('list_of_goods.urls')),
    url(r'^operations/', include('operations.urls')),
    url(r'^localization/', include('localization.urls')),
    url(r'^api/semi-finished-item/', include('warehouse.api.urls', namespace='api-semi-item')),
]
