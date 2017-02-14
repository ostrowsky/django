from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator


decorators = [login_required(login_url='/accounts/login'), never_cache]


@method_decorator(decorators, name='dispatch')
class ProtectedView(TemplateView):
    pass


class MainView(ProtectedView):
    template_name = 'index.html'
