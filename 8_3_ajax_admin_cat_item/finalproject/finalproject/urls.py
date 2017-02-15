"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from spigen.views import main, login, logout, registration_low, registration_form, catalog, item
from myadmin.views import admin_page, delete_user,get_user_form, create_user, admin_cat, admin_cat_create, admin_cat_delete, get_cat_info, admin_item, admin_item_create, admin_item_delete, get_item_info, get_item_by_cat


urlpatterns = [
    url(r'^admin/$', admin_page),
    url(r'^admin_django/', admin.site.urls),
    url(r'^$', main, name='main'),
    url(r'^user/login/$', login),
    url(r'^user/logout/$', logout),
    url(r'^user/registration/$', registration_form),
    url(r'^admin/delete/user/(\d+)$', delete_user),
    url(r'^admin/get_user_form/(\d+)$', get_user_form),
    url(r'^admin/create/user/(\d*)$', create_user),
]

urlpatterns += [
    url(r'^admin/cat/', admin_cat, name='admin_cat'),
    url(r'^admin/create/cat/(\d*)$', admin_cat_create, name='admin_cat_create'),
    url(r'^delete/cat/(\d+)$', admin_cat_delete, name='cat_delete'),
    #url(r'^admin/update/cat/(\d+)$', admin_cat_update, name='cat_update'),
    #url(r'^admin/detail/cat/(\d+)$', admin_cat_detail, name='admin_cat_detail'),
    url(r'^admin/get_cat_info/(\d+)$', get_cat_info),
    url(r'^admin/item/$', admin_item, name='admin_item'),
    url(r'^admin/create/item/(\d*)$', admin_item_create, name='admin_item_create'),
    url(r'^delete/item/(\d+)$', admin_item_delete, name='item_delete'),
    url(r'^admin/get_item_info/(\d+)$', get_item_info, name='get_item_info'),


]

urlpatterns += [
    url(r'^cat/(\S+)/', catalog, name='catalog'),
    url(r'^goods/(\d+)$', item, name='item'),
    url(r'^admin/get_item_by_cat/(\d+)$', get_item_by_cat, name='get_item_by_cat')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)