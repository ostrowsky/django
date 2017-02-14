"""Gems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from mainApp.views import *
from userManagementApp.views import *
from adminApp.views import *

urlpatterns = [
    url(r'^$', main),
]

urlpatterns += [
    url(r'^user/login/$', login),
    url(r'^user/logout/$', logout),
    # url(r'^user/registration/$', registration_low),
    url(r'^user/registration/$', registration),
    url(r'^admin/$', admin_page),
    url(r'^admin/delete/user/(\d+)$', delete_user),

]

# Данный подход нерекомендуется, и будет убран в django 1.10
# urlpatterns = patterns('mainApp.views',
#     url(r'^$', 'main'),
# )
