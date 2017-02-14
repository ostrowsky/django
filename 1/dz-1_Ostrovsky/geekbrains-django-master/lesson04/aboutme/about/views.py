from django.views.generic import TemplateView
from .models import UserProfile, Work, Education, AboutDescription, Company
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


class MyBaseView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userdata'] = UserProfile.objects.get(pk=1)
        return context


class HomeView(MyBaseView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutDescription.objects.filter(
            user=1).order_by('pk')
        return context


class WorkView(MyBaseView):
    template_name = 'work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Work.objects.filter(user=1).order_by('-end_date')
        return context


class StudyView(MyBaseView):
    template_name = 'study.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['educations'] = Education.objects.filter(
            user=1).order_by('-end_date')
        return context


class CompanyView(MyBaseView):
    template_name = 'company_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=self.kwargs['pk'])
        except ObjectDoesNotExist:
            raise Http404
        return context
