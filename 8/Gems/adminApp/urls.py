from django.conf.urls import url, include
from .views import admin_page, delete_user, get_user_form, create_user, admin_gems, admin_gems_create, \
    admin_gems_delete, admin_gems_detail, admin_gems_update

urlpatterns = [
    url(r'gems/$', admin_gems, name='admin_gems'),
    url(r'^gems/create/$', admin_gems_create, name='gems_create'),
    url(r'^gems/delete/(\d+)/$', admin_gems_delete, name='gems_delete'),
    url(r'^gems/update/(\d+)/$', admin_gems_update, name='gems_update'),
    url(r'^gems/detail/(\d+)/$', admin_gems_detail, name='gems_detail'),
    url(r'^$', admin_page, name='admin_users'),
    url(r'^delete/user/(\d+)/$', delete_user),
    url(r'^get_user_form/(\d+)/$', get_user_form),
    url(r'^create/user/(\d*)/$', create_user)
]
