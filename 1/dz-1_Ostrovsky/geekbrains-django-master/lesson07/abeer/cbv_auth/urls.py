from django.conf.urls import url
from .views import LoginView, LogoutView, RegistrationView

app_name = 'cbv_auth'
urlpatterns = [
    url(r'login$', LoginView.as_view(), name='login'),
    url(r'logout$', LogoutView.as_view(), name='logout'),
    url(r'registration$', RegistrationView.as_view(), name='registration'),
]
