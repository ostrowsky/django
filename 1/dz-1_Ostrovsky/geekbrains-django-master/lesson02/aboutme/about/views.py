from django.views.generic import TemplateView
from .models import UserProfile, Work, Education

# Create your views here.


class MyBaseView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = UserProfile.objects.get(pk=1)
        return context


class HomeView(MyBaseView):
    template_name = 'about.html'


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
