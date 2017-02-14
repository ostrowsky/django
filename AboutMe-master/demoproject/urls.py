"""demoproject URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from mainapp.views import main, works, learn, organization, get_works

urlpatterns = [
    url(r'^$', main, name='index'),
    url(r'^works/$', works, name='works'),
    url(r'^learns/$', learn, name='learns'),
    url(r'^organization/(\d+)/$', organization, name='organization'),
    url(r'^get_works/$', get_works)
]
