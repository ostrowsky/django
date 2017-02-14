from django.views.generic import TemplateView, View, CreateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from .forms import RegistrationForm
from .models import UserProfile


class LoginView(TemplateView):
    success_url = '/'
    template_name = 'login.html'

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(self.success_url)
        return redirect(settings.LOGIN_URL)

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class RegistrationView(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    model = UserProfile
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        if obj.password1 and obj.password2 and obj.password1 == obj.password2:
            obj.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            if new_user is not None:
                if new_user.is_active:
                    login(self.request, new_user)
                    redirect(self.success_url)
        return redirect(reverse_lazy('cbv_auth:registration', kwargs={'form': form}))


class LogoutView(View):

    def post(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)
