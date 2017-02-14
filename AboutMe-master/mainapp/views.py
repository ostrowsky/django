from django.shortcuts import render_to_response, Http404, get_object_or_404, loader, render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import datetime
from .models import Work, Study, Hobby, Organization


def main(request):
    name = 'Леонид'
    surname = 'Орлов'
    middlename = 'Александрович'
    city = 'Геленджик'
    birthday = datetime.date(day=2,month=1,year=1988)
    study = 'Высшее'
    info = [
        '''Выпускник физического факультета ПГНИУ.
        На первом курсе начинал, как и многие студенты, с языка c++.
        В дальнейшем понял, что для написания учебных работ понадобится язык более высокого уровня, и познакомился с c#.
        Использовал c# много лет в учебе и в работе.''',
        '''Начал свою карьеру в крупной международной компании Prognoz, создавал проекты для правительства РФ в течение 2-х лет.
        Там познакомился с командной разработкой и системой Tfs.
        После этого работал программистом биллинга на oracle pl/sql в компании "Эр-Телеком Холдинг".
        Сейчас выполняю свою работу удаленно. С 2014 года стал преподавателем и начал передавать свои знания ученикам.
        Также не прекращаю работать удаленно и заниматься своими небольшими проектами на Python и Django.'''
    ]
    return render_to_response("index.html",{'name':name,'surname':surname,'middlename':middlename,'city':city,'birthday':birthday, 'study':study, 'info':info})


def works(request):
    page = 'works'
    work_places = Work.objects.all()
    return render(request,"works.html",{'page':page, 'work_places':work_places})


def learn(request):
    page = 'learns'
    learns = Study.objects.all()
    return render_to_response("learn.html",{'page':page, 'learns':learns})


def organization(request, id):
    page = 'organization'
    '''
    try:
        org = Organization.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404
    '''
    org = get_object_or_404(Organization,id=id)
    return render_to_response('organization.html',{'organization':org})


def get_works(request):
    if request.is_ajax():
        slice = request.POST['slice']
        work_places = Work.objects.all().order_by('organization__name')
        if slice:
            work_places = work_places[:int(slice)]
        html = loader.render_to_string('inc-place_works.html', {'work_places':work_places})
        data = {'html':html}
        return JsonResponse(data)

    raise Http404