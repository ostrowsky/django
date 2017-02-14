from django.views import generic

# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'about.html'


class WorkView(generic.TemplateView):
    template_name = 'work.html'


class StudyView(generic.TemplateView):
    template_name = 'study.html'
