from django.conf.urls import url
from . import views


app_name = 'about'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'work/$', views.WorkView.as_view(), name='work'),
    url(r'study/$', views.StudyView.as_view(), name='study'),
    url(r'company/(?P<pk>\d+)/$', views.CompanyView.as_view(), name='company'),
]
