from django.conf.urls import url
from .views import main, listing, gems, info

urlpatterns = [
    url(r'^$', main),
    url(r'^contacts/$', listing),
    url(r'^gems/(\d+)/$', gems, name='gems'),
    url(r'^info/$', info, name='info')
]